---
title: Instalação
---

# Instalação

Siga os passos abaixo para preparar o ambiente e executar o projeto localmente.

## Requisitos

- Python 3.11+
- pip
- Git (opcional)

## Passos

1. Clone o repositório (ou baixe o código):

```bash
git clone https://github.com/Jaquelinesa82/web_scrapin
cd web_scrapin
```

2. Crie e ative um ambiente virtual:

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

3. Instale as dependências do projeto e de documentação:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

4. Executar o projeto:

```bash
python src/main.py
```

5. Rodar a documentação localmente (opcional):

```bash
mkdocs serve
```

6. Construir o site estático da documentação:

```bash
mkdocs build
```

## Observações

- Os dados extraídos são salvos em `data/processos.jsonl`.
- Se o comando `mkdocs` não for encontrado, verifique se o ambiente virtual está ativado e se `mkdocs` está instalado em `requirements-dev.txt`.
