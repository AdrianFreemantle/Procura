import gradio as gr

from agents.chat_manager import ChatManager
#from agents.markdown_agent import MarkdownAgent
from utils.logging_config import init_logging

# Initialize logging as early as possible
init_logging()

chat_manager = ChatManager()
#markdown_agent = MarkdownAgent()

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

        # --- Helpers & State ---
        def _context_label(ctx: dict) -> str:
            # Example: "3 • 2025-08-08 16:10:12 (active)"
            return f"{ctx['context_id']} • {ctx['context_name']} ({ctx['context_status']})"

        def _build_choices():
            ctxs = chat_manager.list_contexts()
            current_id = chat_manager.current_context_id
            labels = []
            mapping = {}
            selected = None
            for c in ctxs:
                label = _context_label(c)
                labels.append(label)
                mapping[label] = c["context_id"]
                if current_id is not None and c["context_id"] == current_id:
                    selected = label
            return labels, selected, mapping

        mapping_state = gr.State({})

        # --- Events ---    

        def send_message(message, chat_history):
            # Process the message and return updated chat
            for updated_chat in chat_manager.chat(message):
                chat_history = updated_chat
            return chat_history

        # Step 1: Clear input, store message in state
        def prep_message(user_input, chat_history):
            new_message = {"role": "user", "content": user_input}
            chat_history.append(new_message)
            return "", user_input, chat_history

        message_state = gr.State()

        # Initialize sidebar with context list on app load
        def init_sidebar():
            labels, selected, mapping = _build_choices()
            # Do not auto-select or load any previous chat on load.
            # Show a blank new chat until the user selects or creates one.
            return gr.update(choices=labels, value=None), mapping, []

        demo.load(
            fn=init_sidebar,
            inputs=[],
            outputs=[chat_selector, mapping_state, chatbot]
        )

        # New Chat: create and persist, then refresh list and clear chat UI
        def on_new_chat(mapping):
            ctx = chat_manager.create_new_context()
            chat_manager.save_context(ctx)  # assign ID, remains 'empty' until first message
            labels, selected, new_map = _build_choices()
            # Select the newly created (current) chat in the sidebar
            return gr.update(choices=labels, value=selected), new_map, []

        new_chat_btn.click(
            fn=on_new_chat,
            inputs=[mapping_state],
            outputs=[chat_selector, mapping_state, chatbot]
        )

        # Selecting a chat: switch and load its conversation history
        def on_select_chat(selected_label, mapping):
            if not selected_label:
                return []
            ctx_id = mapping.get(selected_label)
            if ctx_id is None:
                # Mapping might be stale; rebuild once
                labels, selected, new_map = _build_choices()
                if selected_label in new_map:
                    ctx_id = new_map[selected_label]
                else:
                    return []
            ctx = chat_manager.switch_context(ctx_id)
            if ctx is None:
                return []
            return ctx.conversation_history

        chat_selector.change(
            fn=on_select_chat,
            inputs=[chat_selector, mapping_state],
            outputs=[chatbot]
        )

        send_btn.click(
            fn=prep_message,
            inputs=[user_input, chatbot],
            outputs=[user_input, message_state, chatbot],
        ).then(
            fn=send_message,
            inputs=[message_state, chatbot],
            outputs=[chatbot],
        )

        user_input.submit(
            fn=prep_message,
            inputs=[user_input, chatbot],
            outputs=[user_input, message_state, chatbot],
        ).then(
            fn=send_message,
            inputs=[message_state, chatbot],
            outputs=[chatbot],
        )        

        def handle_markdown_generation():
            """Wrapper to convert agent output to gr.update format for proper markdown rendering"""
            buffer = ""
            for content in chat_manager.draft():
                buffer += content
                yield gr.update(value=buffer)

        draft_btn.click(handle_markdown_generation, inputs=[], outputs=markdown_output)

    return demo
