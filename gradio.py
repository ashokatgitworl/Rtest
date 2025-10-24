import gradio as gr
from service import get_ai_response,chatbot_interface

def create_interface():
    with gr.Blocks(theme=gr.themes.Soft()) as demo:
        gr.Markdown("# 🤖 AI Chatbot Assistant")
        gr.Markdown("Ask me anything and I'll help you with intelligent responses!")

        chatbot = gr.Chatbot(
            value=[],
            height=400,
            label="Chat History",
            show_copy_button=True,
            type="messages"  # new Gradio format
        )

        msg = gr.Textbox(
            placeholder="Type your message here...",
            label="Your Message",
            lines=2
        )

        with gr.Row():
            submit_btn = gr.Button("Send", variant="primary")
            clear_btn = gr.Button("Clear Chat", variant="secondary")

        submit_btn.click(chatbot_interface, inputs=[msg, chatbot], outputs=[chatbot, msg])
        msg.submit(chatbot_interface, inputs=[msg, chatbot], outputs=[chatbot, msg])
        clear_btn.click(lambda: ([], ""), inputs=[], outputs=[chatbot, msg])

        gr.Markdown("---")
        gr.Markdown("💡 Built with Gradio + LangChain + Groq")

    return demo

if __name__ == "__main__":
    demo = create_interface()
    demo.launch(
        share=True,
        server_name="127.0.0.1",
        server_port=7860,
        show_error=True
    )