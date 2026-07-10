---
title: Parser
---

# Parser

O módulo `parser.py` é responsável por extrair e normalizar os dados obtidos do HTML retornado pelo portal do TRF5.

## Funções principais

### `normalize_party_name(value: str) -> str`

Remove caracteres especiais e mantém apenas letras, números e espaços.

### `only_digits(value: str) -> str`

Retorna apenas os dígitos de uma string, útil para normalizar CNPJ antes de construir URLs.

### `clean_text(value: str | None) -> str`

Normaliza espaços e quebras de linha no texto extraído do HTML.

## Extração de identificação

### `process_identification(html: str) -> dict`

Converte o HTML em objeto `BeautifulSoup`, extrai campos-chave da página e devolve um dicionário com:

- `numero_processo`
- `numero_legado`
- `data_autuacao`
- `relator`
- `envolvidos`
- `movimentacoes`

A função utiliza o texto bruto da página para localizar padrões como `PROCESSO Nº`, `PROC. ORIGINÁRIO Nº:` e `AUTUADO EM`.

## Extração dos envolvidos

### `involved_parties(soup: BeautifulSoup) -> list[dict]`

Percorre tabelas HTML em busca de pares de colunas que representem papel e nome dos envolvidos.

Critérios usados:

- apenas linhas com exatamente duas colunas são consideradas
- ignoram-se campos de `FASE ATUAL`, `COMPLEMENTO`, `ÚLTIMA LOCALIZAÇÃO` e `RELATOR`
- só adiciona envolvidos quando há tag `<b>` indicando destaque no HTML

O retorno é uma lista de objetos com:

- `papel`
- `nome`

## Extração de movimentações

### `parse_movements(soup: BeautifulSoup) -> list[dict]`

Encontra links com atributo `name` iniciando em `mov_` e busca a tabela pai de cada movimento.

Para cada movimento, extrai:

- `data`: data da movimentação
- `texto`: texto consolidado das células restantes da tabela

## Processamento de listas de processos

### `process_list(html: str) -> list[str]`

Busca links com a classe `linkar` dentro do HTML de resultados.

Para cada link que contém `/processo/` no `href`, extrai o número do processo e retorna uma lista única de números.
