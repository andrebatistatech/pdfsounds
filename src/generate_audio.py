from pdfminer.high_level import extract_text
from gtts import gTTS
import re
import os

# 1️⃣ Caminho do seu PDF
pdf_path = os.path.join(
    "..",
    "data",
    "C:/Users/andre/Downloads/curso/mod-1-al-18.pdf"
)

# 2️⃣ Extrair texto do PDF
def extract_text_from_pdf(pdf_path):
    text = extract_text(pdf_path)
    return text

# 3️⃣ Limpeza básica do texto
def clean_text(text):
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(
        r'Perguntas para Reflexão.*?Na próxima aula.*?',
        '',
        text,
        flags=re.DOTALL
    )
    text = re.sub(r'Recursos Complementares.*', '', text, flags=re.DOTALL)
    return text

# 4️⃣ Ajustes para leitura profissional
def adjust_for_reading(text):
    replacements = {
        "RDD": "erre dê dê",
        "DAG": "dáguê",
        "maxOffsetsPerTrigger": "máximo de offsets por trigger",
        "SQL": "esse quê ele",
        "HDFS": "agá dê efe esse",
        "API": "a p i",
        "ML": "eme ele",
        "GPU": "gê pê u",
        "ETL": "e tê ele",
    }
    for target, replacement in replacements.items():
        text = text.replace(target, replacement)
    return text

# Pipeline completo
print("📖 Lendo PDF...")
raw_text = extract_text_from_pdf(pdf_path)

print("🧹 Limpando texto...")
cleaned_text = clean_text(raw_text)

print("🎙️ Ajustando texto para leitura...")
final_text = adjust_for_reading(cleaned_text)

os.makedirs(os.path.join("..", "output"), exist_ok=True)
output_path = os.path.join(
    "..",
    "output",
    "arquitetura_spark_profissional.mp3"
)

print("🔊 Gerando áudio...")
tts = gTTS(text=final_text, lang='pt-br')
tts.save(output_path)

print(f"✅ Áudio gerado com sucesso: {output_path}")
