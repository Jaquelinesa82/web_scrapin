# TRF5 Process Crawler

Crawler desenvolvido para consulta processual no portal do TRF5.

O projeto permite buscar processos por:

- Número do processo;
- CPF/CNPJ;
- Nome da parte.

A execução é feita de forma interativa pelo terminal, permitindo escolher o tipo de busca e informar o termo desejado.

---

# Tecnologias utilizadas

- Python 3
- requests
- BeautifulSoup4
- lxml

---
## Requisitos

- Python 3.11.9
- pip

---

# Qualidade de código

O projeto utiliza ferramentas de qualidade e formatação:

```bash
flake8
black 
```
---

# Estrutura do projeto

```text
src/
├── crawler.py
├── parser.py
├── storage.py
├── main.py
└── services/
    └── search.py
```

---

# Responsabilidades

## crawler.py

Responsável pelas requisições HTTP e comunicação com o portal do TRF5.

## parser.py

Responsável pela extração, tratamento e normalização dos dados HTML utilizando BeautifulSoup4.

## storage.py

Responsável pela persistência dos dados em arquivo JSON Lines.

## services/search.py

Responsável pelos fluxos de busca, processamento dos processos encontrados, deduplicação e persistência.

## main.py

Responsável pela interface interativa no terminal e pela orquestração da execução.

---

# Funcionalidades implementadas

- Busca por número do processo;
- Busca por CNPJ;
- Busca por nome da parte;
- Paginação na busca por CNPJ;
- Persistência em JSON Lines;
- Controle de duplicidade de processos;
- Tratamento de falha de conexão;
- Validação de disponibilidade do portal;
- Execução interativa via terminal;
- Separação de responsabilidades por módulo.

---

# Como executar o projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/Jaquelinesa82/web_scrapin

```
## Criar ambiente virtual

```bash
python -m venv .venv
```

## Ativar ambiente virtual

### Linux/macOS

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

## Instalar dependências

```bash
pip install -r requirements.txt
```

## Executar o projeto

```bash
python src/main.py
```

---

# Estrutura dos dados persistidos

Os dados são persistidos em:

```text
data/processos.jsonl
```

Cada linha contém um JSON com:

- número do processo;
- numero legado;
- data de autuação;
- relator;
- envolvidos;
- movimentações;

Os arquivos extraídos em `data/` estão configurados no `.gitignore`.

---

# Decisões de implementação

O projeto foi estruturado buscando simplicidade, legibilidade e separação de responsabilidades.

As responsabilidades foram divididas em módulos independentes:

- `crawler.py` → requisições HTTP e disponibilidade do portal;
- `parser.py` → extração e normalização dos dados;
- `storage.py` → persistência em JSON Lines;
- `services/search.py` → fluxos de busca, deduplicação e persistência;
- `main.py` → interface interativa e orquestração.

A busca por CNPJ implementa paginação para descoberta de múltiplos processos.

Foi implementado controle de duplicidade para evitar persistência repetida de processos encontrados em diferentes tipos de busca.

O crawler também realiza validação de disponibilidade do portal antes da execução, evitando limpar arquivos anteriores em caso de indisponibilidade do sistema.

---

# Dificuldades encontradas

## Paginação da busca por CNPJ

A busca por CNPJ possui paginação própria no portal do TRF5.

Foi necessário analisar o padrão das URLs de paginação para implementar a navegação entre páginas de resultados.

---

## Tratamento de indisponibilidade do portal

Durante os testes, foram identificados cenários de falha de conexão e indisponibilidade temporária do portal.

Para evitar perda de dados persistidos anteriormente, foi implementada uma validação de disponibilidade do portal antes da limpeza do arquivo de saída.

---

# Possíveis melhorias futuras

- Persistência em banco de dados;
- Exportação PDF;
- Testes automatizados;
- Dockerização do projeto.

---
