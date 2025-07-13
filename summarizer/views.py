from bs4 import BeautifulSoup
import requests
from docling.document_converter import DocumentConverter
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import os
from weasyprint import HTML, CSS
import markdown2
from django.shortcuts import render
from django.conf import settings






def scrape_and_generate_pdf(request):

    # 1. Capture the URL
    url = request.POST.get('url_web')
    

    # 2. Basic scraping
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # 3. Convert content to Markdown with docling
    converter = DocumentConverter()
    result = converter.convert(url)
    docling_txt = result.document.export_to_markdown()

    # 4. Load Mistral key from .env
    load_dotenv()

    # Instantiate the LLM
    llm = ChatMistralAI(model='mistral-medium-latest')
    user_prompt = request.POST.get('ia_prompt')
    prompt = user_prompt + "\n\n{text}"
    
    


    # Invoke the LLM with the prompt
    llmresponse = llm.invoke(prompt.format(entry_prompt=prompt, text=docling_txt))
    # Text that goes in the PDF
    texto = llmresponse.content

    html_body = markdown2.markdown(texto)

    html_template = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <title>Resumo Profissional</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Playfair+Display:wght@400;700&display=swap');
        
        body {{
            font-family: 'Roboto', sans-serif;
            margin: 0;
            background: #f5f7fa;
            color: #2d3748;
            line-height: 1.6;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }}
        h1, h2, h3 {{
            font-family: 'Playfair Display', serif;
        }}

        /* Estilo para o conteúdo convertido do Markdown */
        .markdown-body h1, .markdown-body h2, .markdown-body h3 {{
            color: #2c5282;
            margin-top: 1.5rem;
        }}

        .markdown-body ul, .markdown-body ol {{
            padding-left: 1.5rem;
            margin-bottom: 1rem;
        }}

        .markdown-body pre, .markdown-body code {{
            background: #edf2f7;
            font-family: monospace;
            padding: 6px 10px;
            border-radius: 6px;
            display: block;
            margin: 1rem 0;
            white-space: pre-wrap;
        }}

        .markdown-body p {{
            margin-bottom: 1rem;
        }}
    </style>        
</head>
<body>
    <div class="container">
        <h1>Resumo Profissional</h1>
        <div class="markdown-body">{html_body}</div>
    </div>  
</body>
</html>
"""

    # 6. Generate PDF from HTML
    file_name = request.POST.get('file_name_tag')
    relative_path = f'pdfs/{file_name}.pdf'
    full_path = os.path.join(settings.MEDIA_ROOT, relative_path)

    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    HTML(string=html_template).write_pdf(full_path, stylesheets=[
    CSS(string='@page { size: A4; margin: 1cm; }')])

    return f'{settings.MEDIA_URL}{relative_path}'

def summarizer(request):
    if request.method == 'GET':
        return render(request, 'summarizer/summarizer.html')
    elif request.method == 'POST':
        if request.POST.get('url_web'):
            pdf_file = scrape_and_generate_pdf(request)
            return render(request, 'summarizer/summarizer.html', {'pdf_file': pdf_file})
        else:
            return render(request, 'summarizer/summarizer.html', {'error': 'Please provide a valid URL.'})
        



