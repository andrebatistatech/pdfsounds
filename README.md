
# PDFSounds

> Conversor profissional de PDFs em áudio (.mp3), com ajuste de texto e integração com serviços de TTS de alta qualidade.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## ✨ Funcionalidades

- Leitura de PDFs e extração de texto
- Pipeline de limpeza e ajuste de texto para fluência de leitura
- Geração de áudio `.mp3` com voz natural
    - `gTTS` (Google Translate TTS — simples, gratuito)
    - Suporte preparado para **Amazon Polly** (voz neural profissional)
- Estrutura modular e extensível
- Projetado para uso offline ou em pipelines de conteúdo

---

## 🗂 Estrutura do projeto

```
pdfsounds/
├── data/               # PDFs de entrada
├── output/             # Áudios gerados (.mp3)
├── src/
│   ├── generate_audio.py            # versão com gTTS
│   ├── generate_audio_pdfminer.py   # versão com pdfminer + gTTS
│   └── generate_audio_polly.py      # (futuro) versão com Amazon Polly
├── requirements.txt    # dependências do projeto
├── README.md           # este arquivo
├── CHANGELOG.md        # changelog do projeto
└── .gitignore          # arquivos ignorados
```

---

## 🚀 Como usar

### 1️⃣ Instalação

Clone o projeto:

```bash
git clone https://github.com/seuusuario/pdfsounds.git
cd pdfsounds
```

Crie e ative um ambiente virtual (recomendado):

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
# ou
.venv\Scripts\activate      # Windows
```

Instale as dependências:

```bash
uv pip install -r requirements.txt
```

---

### 2️⃣ Conversão de PDF → áudio com `gTTS`

Coloque o PDF na pasta `data/`.

Rode o script com `gTTS`:

```bash
cd src
python generate_audio.py
```

Resultado: arquivo `.mp3` gerado em `output/`.

---

### 3️⃣ Alternativa com `pdfminer.six`

Se estiver usando Windows ou se desejar evitar dependências nativas, use:

```bash
cd src
python generate_audio_pdfminer.py
```

---

### 4️⃣ (Opcional) Integração com Amazon Polly

**Pré-requisitos**:

- Conta AWS ativa
- IAM user com permissão `AmazonPollyFullAccess`
- `AWS_ACCESS_KEY_ID` e `AWS_SECRET_ACCESS_KEY` configurados (via env ou CLI)
- `boto3` instalado

Instale:

```bash
uv pip install boto3
```

Rode (quando `generate_audio_polly.py` estiver implementado):

```bash
python generate_audio_polly.py
```

Resultado: áudio com voz neural, altamente natural.

---

## 🎙️ Roadmap

- [x] Suporte básico com `gTTS`
- [x] Alternativa robusta com `pdfminer.six`
- [ ] Suporte completo com **Amazon Polly**
- [ ] Modularização do pipeline (ex: opções de pronúncia por dicionário)
- [ ] Suporte a Google Cloud TTS (voz natural)
- [ ] CLI para uso simples via terminal

---

## 💻 Exemplos de commit (conventional commits)

```bash
feat: implementa conversão de PDFs em áudio com TTS
fix: corrige problema de extração de texto no Windows
docs: adiciona README completo com instruções
chore: atualiza requirements.txt e .gitignore
```

---

## 📜 Licença

Este projeto é licenciado sob a licença MIT — veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 🤝 Contribuição

Contribuições são bem-vindas! Abra uma issue ou um pull request. 🚀
