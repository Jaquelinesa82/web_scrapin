# TRF5 Process Crawler

Crawler desenvolvido para consulta processual no portal do TRF5.

O projeto permite buscar processos por:

- Número do processo;
- CNPJ/CPF;
- Nome da parte.

Os dados extraídos são persistidos em arquivo JSON Lines (`.jsonl`).

---

# Tecnologias utilizadas

- Python 3.9.11
- requests
- BeautifulSoup4

---

# Estrutura do projeto

```text

src/
├── crawler.py
├── parser.py
├── storage.py
└── main.py

```

---

# Responsabilidades

## crawler.py

Responsável pelas requisições HTTP e comunicação com o portal do TRF5.

## parser.py

Responsável pela extração, tratamento e normalização dos dados HTML utilizando BeautifulSoup4.

## storage.py

Responsável pela persistência dos dados em arquivo JSON Lines.

## main.py

Responsável pela orquestração do fluxo de execução das buscas.

---

# Funcionalidades implementadas

- Busca por número do processo;
- Busca por CNPJ/CPF;
- Busca por nome da parte;
- Paginação na busca por CNPJ;
- Persistência em JSON Lines;
- Controle de duplicidade de processos;
- Tratamento de falha de conexão;
- Validação de disponibilidade do portal;
- Logs de execução;
- Separação de responsabilidades por módulo.

---

# Como executar

## Criar ambiente virtual

```bash
python -m venv .venv
```

## Ativar ambiente virtual

### Linux/macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

## Instalar dependências

```bash
pip install -r requirements.txt
```

## Executar projeto

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

---

# Decisões de implementação

O projeto foi estruturado buscando simplicidade, legibilidade e separação de responsabilidades.

As responsabilidades foram divididas em módulos independentes:

- crawler → requisições HTTP;
- parser → extração e tratamento de dados;
- storage → persistência;
- main → orquestração do fluxo.

A busca por CNPJ implementa paginação para descoberta de múltiplos processos.

Foi implementado controle de duplicidade para evitar persistência repetida de processos encontrados em diferentes tipos de busca.

O crawler também realiza validação de disponibilidade do portal antes da execução, evitando limpar arquivos anteriores em caso de indisponibilidade do sistema.

---

# Tratamento de erros

O projeto possui tratamento para:

- falha de conexão;
- timeout;
- respostas vazias;
- interrupção controlada do fluxo.

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
