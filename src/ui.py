import gradio as gr

from agents.chat_agent import ChatAgent
from agents.markdown_agent import MarkdownAgent
from agents.agent import Agent

chat_agent = ChatAgent()
markdown_agent = MarkdownAgent()
agent = Agent()

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
                    type="messages"
                )
            with gr.Column(scale=2):
                markdown_output = gr.Code(
                    label=None,
                    language="markdown",
                    value="Click '📄 Draft Document' to generate a sample markdown document.",
                    elem_id="doc_output"
                )

        # --- Bottom: Message Input and Draft Button ---
        with gr.Row():
            with gr.Column(scale=3):
                user_input = gr.Textbox(
                    placeholder="Ask me anything...",
                    lines=3,
                    max_lines=5,
                    show_label=False
                )
            with gr.Column(scale=1):
                send_btn = gr.Button("💬 Send Message")
                draft_btn = gr.Button("📄 Draft Document", variant="secondary")

        # --- Events ---
        send_btn.click(agent.chat, inputs=user_input, outputs=chatbot)
        user_input.submit(agent.chat, inputs=user_input, outputs=chatbot)

        new_chat_btn.click(fn=agent.reset, outputs=[], show_progress=False)
        new_chat_btn.click(fn=lambda: [], outputs=chatbot, show_progress=False)

        draft_btn.click(markdown_agent.generate, inputs=[], outputs=markdown_output)

    return demo
