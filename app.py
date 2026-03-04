from dotenv import load_dotenv

load_dotenv()

import gradio as gr
from doc_splitter import process_and_store_document
from retriever import setup_qa_chain, get_answer

def handle_upload(file_path):
    if file_path is None:
        return "Please upload a PDF file."
    try:
        process_and_store_document(file_path)
        return "Successfully processed and embedded the document."
    except Exception as e:
        return f"Error processing file: {str(e)}"

def handle_chat(message, history):
    try:
        rag_chain = setup_qa_chain()
        response = get_answer(rag_chain, message)
        return response
    except Exception as e:
        return f"Error: {str(e)}. Make sure a document is uploaded"

with gr.Blocks(title="Smart Assistant") as demo:
    gr.Markdown("## Smart QA Assistant")
    
    with gr.Tab("Upload Document"):
        file_input = gr.File(label="Upload PDF", file_types=[".pdf",".docx"], type="filepath")
        upload_button = gr.Button("Process Document")
        upload_status = gr.Textbox(label="Status", interactive=False)
        
        upload_button.click(
            fn=handle_upload,
            inputs=file_input,
            outputs=upload_status
        )
        
    with gr.Tab("Chat"):
        gr.ChatInterface(fn=handle_chat)

if __name__ == "__main__":
    demo.launch()