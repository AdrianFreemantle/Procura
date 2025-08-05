import gradio as gr

from agents.facts_agent import ChatManager
from agents.markdown_agent import MarkdownAgent

chat_manager = ChatManager()
markdown_agent = MarkdownAgent()

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
                choices=["Current Chat", "Previous Chat 1", "Previous Chat 2", "Previous Chat 3"],
                label="Chat History"
            )

        # --- Main: Chat Column + Markdown Output ---
        with gr.Row(elem_id="main_row"):
            with gr.Column(scale=2):
                chatbot = gr.Chatbot(
                    label=None,
                    elem_id="chatbot",
                    container=True,
                    type="messages",
                    value=[{"role": "assistant", "content": "Hello! I am here to assist you in gathering information to draft an NEC4 Supply Short Contract."}]
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

        # --- Events ---    
        send_btn.click(chat_manager.chat, inputs=user_input, outputs=chatbot).then(lambda: "", outputs=user_input)
        user_input.submit(chat_manager.chat, inputs=user_input, outputs=chatbot).then(lambda: "", outputs=user_input)
        
        #new_chat_btn.click(fn=chat_agent.reset, outputs=[], show_progress=False)
        #new_chat_btn.click(fn=lambda: [], outputs=chatbot, show_progress=False)

        def handle_markdown_generation():
            """Wrapper to convert agent output to gr.update format for proper markdown rendering"""
            for content in markdown_agent.generate():
                yield gr.update(value=content)

        draft_btn.click(handle_markdown_generation, inputs=[], outputs=markdown_output)

    return demo
