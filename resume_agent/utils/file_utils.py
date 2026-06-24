import re
from pathlib import Path
from playwright.sync_api import sync_playwright

def md_to_html(md_text):
    """Converts a basic Markdown string into a styled HTML document."""
    # Convert headers
    html = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', md_text, flags=re.MULTILINE)
    html = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    
    # Convert bold
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    
    # Convert bullet lists
    # Group consecutive lines starting with - or * and wrap them in <ul>
    lines = html.split('\n')
    in_list = False
    for i, line in enumerate(lines):
        match = re.match(r'^[-\*]\s+(.*?)$', line)
        if match:
            content = match.group(1)
            if not in_list:
                lines[i] = '<ul>\n<li>' + content + '</li>'
                in_list = True
            else:
                lines[i] = '<li>' + content + '</li>'
        else:
            if in_list:
                lines[i] = '</ul>\n' + line
                in_list = False
    if in_list:
        lines.append('</ul>')
    html = '\n'.join(lines)
    
    # Wrap standard paragraphs (lines that don't start with tags)
    paragraphs = []
    for para in html.split('\n\n'):
        para = para.strip()
        if not para:
            continue
        if any(para.startswith(tag) for tag in ['<h1>', '<h2>', '<h3>', '<ul>', '<li>', '<div>']):
            paragraphs.append(para)
        else:
            paragraphs.append(f'<p>{para}</p>')
    
    body_content = '\n'.join(paragraphs)
    
    # Beautiful modern stylesheet for CV/Resume
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                color: #2c3e50;
                line-height: 1.5;
                margin: 40px;
                font-size: 14px;
            }}
            h1 {{
                font-size: 26px;
                color: #2c3e50;
                border-bottom: 2px solid #3498db;
                padding-bottom: 8px;
                margin-top: 0;
            }}
            h2 {{
                font-size: 18px;
                color: #2980b9;
                border-bottom: 1px solid #ecf0f1;
                padding-bottom: 4px;
                margin-top: 20px;
                margin-bottom: 10px;
            }}
            h3 {{
                font-size: 15px;
                color: #34495e;
                margin-top: 15px;
                margin-bottom: 5px;
            }}
            p {{
                margin-top: 0;
                margin-bottom: 10px;
                text-align: justify;
            }}
            ul {{
                margin-top: 0;
                margin-bottom: 10px;
                padding-left: 20px;
            }}
            li {{
                margin-bottom: 5px;
            }}
            strong {{
                color: #1a252f;
            }}
            @media print {{
                body {{
                    margin: 20px;
                }}
            }}
        </style>
    </head>
    <body>
        {body_content}
    </body>
    </html>
    """
    return styled_html

def convert_md_to_pdf(md_path, pdf_path=None):
    """Converts a markdown resume to a professional PDF file using Playwright."""
    md_path = Path(md_path)
    if pdf_path is None:
        pdf_path = md_path.with_suffix('.pdf')
    else:
        pdf_path = Path(pdf_path)
        
    md_text = md_path.read_text(encoding='utf-8')
    html_content = md_to_html(md_text)
    
    # Save a temporary HTML file
    temp_html_path = md_path.with_suffix('.html')
    temp_html_path.write_text(html_content, encoding='utf-8')
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            # Navigate to the local file URL
            file_url = temp_html_path.absolute().as_uri()
            page.goto(file_url)
            page.wait_for_load_state("networkidle")
            
            # Print page to PDF with nice margins
            page.pdf(
                path=str(pdf_path),
                format="A4",
                margin={
                    "top": "0.6in",
                    "bottom": "0.6in",
                    "left": "0.6in",
                    "right": "0.6in"
                },
                print_background=True
            )
            browser.close()
    finally:
        # Clean up temporary HTML file
        if temp_html_path.exists():
            temp_html_path.unlink()
            
    return pdf_path
