import zipfile
import xml.etree.ElementTree as ET
import sys

def extract_text_from_docx(docx_path):
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    text = []
    try:
        with zipfile.ZipFile(docx_path) as docx:
            xml_content = docx.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            for p in tree.findall('.//w:p', ns):
                texts = [node.text for node in p.findall('.//w:t', ns) if node.text]
                if texts:
                    text.append(''.join(texts))
        return '\n'.join(text)
    except Exception as e:
        return str(e)

with open('TP1_extracted.txt', 'w', encoding='utf-8') as f:
    f.write(extract_text_from_docx('TP1.docx'))
