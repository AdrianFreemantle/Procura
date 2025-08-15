import gradio as gr
import requests
import json
from utils.logging_config import init_logging

# Initialize logging as early as possible
init_logging()

API_URL = "http://127.0.0.1:8000"

# -----------------------------------------------------------------------------
# Gradio UI --------------------------------------------------------------------
# -----------------------------------------------------------------------------

CSS = """
.gradio-container {
  display: flex !important;
  flex-direction: column !important;
  height: 100vh !important;
  max-width: 100% !important;
}
#main_row {
  flex: 1 1 auto !important;
  display: flex !important;
}
#chatbot, #doc_output {
  flex: 1 1 auto !important;
  overflow: auto !important;
  height: calc(100vh - 260px) !important;
}
#doc_output {
  background-color: #2d2d2d !important;
  border: 1px solid #ddd !important;
  padding: 1rem !important;
  border-radius: 6px !important;
  font-family: system-ui, sans-serif !important;
  overflow: auto !important;
  min-height: 100px !important;
}
"""

def create_interface() -> gr.Blocks:
    with gr.Blocks(css=CSS, title="Procura – NEC4 Copilot") as demo:
        gr.Markdown("## 🏗️ Procura\nYour Personal NEC4 Assistant & Document Drafting Copilot")

        # --- Sidebar with Chat Selector ---
        with gr.Sidebar():
            new_chat_btn = gr.Button("New Chat", variant="secondary")
            chat_selector = gr.Radio(
                choices=[],
                label="Chat History"
            )

        # --- Main: Chat Column + Markdown Output ---
        with gr.Row(elem_id="main_row"):
            with gr.Column(scale=2):
                chatbot = gr.Chatbot(
                    label=None,
                    elem_id="chatbot",
                    container=True,
                    type="messages"
                )
            with gr.Column(scale=2):
                markdown_output = gr.Markdown(
                    value="*No document drafted yet.*",
                    elem_id="doc_output",
                    container=True,
                    show_copy_button=True
                )

        # --- Bottom: Message Input and Draft Button ---
        with gr.Row():
            with gr.Column(scale=3):
                user_input = gr.Textbox(
                    placeholder="Ask me anything...",
                    lines=1,
                    max_lines=5,
                    show_label=False,
                    submit_btn=True
                )
            with gr.Column(scale=1):
                send_btn = gr.Button("💬 Send Message")
                draft_btn = gr.Button("📄 Draft Document", variant="secondary")

        # --- State Management ---
        mapping_state = gr.State({})  # Maps UI labels to context IDs
        context_id_state = gr.State(None)  # Stores the currently active context ID
        message_state = gr.State()  # Stores the user message before sending to API

        # --- Helpers ---
        def _context_label(ctx: dict) -> str:
            return f"{ctx['context_id']} • {ctx['context_name']} ({ctx['context_status']})"

        def _build_choices(current_context_id=None):
            params = {}
            if current_context_id:
                params['current_context_id'] = current_context_id

            try:
                response = requests.get(f"{API_URL}/contexts", params=params)
                response.raise_for_status()
                ctxs = response.json()
            except (requests.RequestException, json.JSONDecodeError) as e:
                gr.Warning(f"Error fetching contexts: {e}")
                return [], None, {}

            labels = []
            mapping = {}
            selected = None
            for c in ctxs:
                label = _context_label(c)
                labels.append(label)
                mapping[label] = c["context_id"]
                if current_context_id is not None and c["context_id"] == current_context_id:
                    selected = label
            return labels, selected, mapping

        # --- Event Handlers ---

        def init_sidebar():
            labels, _, mapping = _build_choices()
            return gr.update(choices=labels, value=None), mapping, [], None

        demo.load(
            fn=init_sidebar,
            inputs=[],
            outputs=[chat_selector, mapping_state, chatbot, context_id_state]
        )

        def on_new_chat():
            try:
                response = requests.post(f"{API_URL}/contexts", json={"name": None})
                response.raise_for_status()
                new_ctx = response.json()
                new_ctx_id = new_ctx['context_id']
            except requests.RequestException as e:
                gr.Warning(f"Error creating new chat: {e}")
                return gr.update(), gr.update(), gr.update(), gr.update()

            labels, selected, new_map = _build_choices(current_context_id=new_ctx_id)
            history = new_ctx.get('conversation_history', [])
            return gr.update(choices=labels, value=selected), new_map, history, new_ctx_id

        new_chat_btn.click(
            fn=on_new_chat,
            inputs=[],
            outputs=[chat_selector, mapping_state, chatbot, context_id_state]
        )

        def on_select_chat(selected_label, mapping):
            if not selected_label:
                return [], None

            ctx_id = mapping.get(selected_label)
            if ctx_id is None:
                gr.Warning(f"Could not find chat ID for '{selected_label}'.")
                return gr.update(), gr.update()

            try:
                response = requests.get(f"{API_URL}/contexts/{ctx_id}")
                response.raise_for_status()
                ctx = response.json()
            except requests.RequestException as e:
                gr.Warning(f"Error loading chat: {e}")
                return gr.update(), gr.update()

            return ctx.get('conversation_history', []), ctx_id

        chat_selector.change(
            fn=on_select_chat,
            inputs=[chat_selector, mapping_state],
            outputs=[chatbot, context_id_state]
        )

        def prep_message(user_input_text, chat_history):
            if not user_input_text.strip():
                return "", None, chat_history
            new_message = {"role": "user", "content": user_input_text}
            chat_history.append(new_message)
            return "", user_input_text, chat_history

        def send_message(message, context_id, chat_history):
            if context_id is None:
                chat_history.append({"role": "assistant", "content": "Please create or select a chat first."})
                yield chat_history
                return

            try:
                response = requests.post(
                    f"{API_URL}/contexts/{context_id}/chat",
                    json={"message": message},
                    stream=True,
                    timeout=120
                )
                response.raise_for_status()

                for line in response.iter_lines():
                    if line.startswith(b'data:'):
                        data_str = line.decode('utf-8')[5:].strip()
                        if data_str:
                            updated_chat = json.loads(data_str)
                            yield updated_chat

            except requests.RequestException as e:
                error_message = {"role": "assistant", "content": f"Error: Could not connect to the assistant. {e}"}
                chat_history.append(error_message)
                yield chat_history

        send_btn.click(
            fn=prep_message,
            inputs=[user_input, chatbot],
            outputs=[user_input, message_state, chatbot],
        ).then(
            fn=send_message,
            inputs=[message_state, context_id_state, chatbot],
            outputs=[chatbot],
        )

        user_input.submit(
            fn=prep_message,
            inputs=[user_input, chatbot],
            outputs=[user_input, message_state, chatbot],
        ).then(
            fn=send_message,
            inputs=[message_state, context_id_state, chatbot],
            outputs=[chatbot],
        )

        def handle_markdown_generation(context_id):
            if context_id is None:
                yield "*Please create or select a chat first.*"
                return

            buffer = ""
            try:
                response = requests.get(f"{API_URL}/contexts/{context_id}/draft", stream=True, timeout=120)
                response.raise_for_status()

                for line in response.iter_lines():
                    if line.startswith(b'data:'):
                        data_str = line.decode('utf-8')[5:].strip()
                        if data_str:
                            data = json.loads(data_str)
                            buffer += data.get('content', '')
                            yield gr.update(value=buffer)
            except requests.RequestException as e:
                yield f"*Error generating document: {e}*"

        draft_btn.click(
            handle_markdown_generation,
            inputs=[context_id_state],
            outputs=markdown_output
        )

    return demo
