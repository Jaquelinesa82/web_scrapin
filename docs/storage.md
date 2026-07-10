---
title: Storage
---

# Storage

O módulo `storage.py` é responsável por persistir os dados extraídos em formato JSON Lines.

## Funções principais

### `clear_jsonl(output_path: str = "data/processos.jsonl") -> None`

- Cria o diretório `data/` caso não exista.
- Limpa o conteúdo do arquivo `processos.jsonl`.
- É usado no início da execução para começar uma nova coleta de dados.

### `save_jsonl(data: dict, output_path: str = "data/processos.jsonl") -> None`

- Garante que o diretório de destino existe.
- Abre o arquivo em modo append (`a`).
- Escreve cada registro como uma linha JSON separada.

## Formato de saída

O arquivo `data/processos.jsonl` contém um registro JSON por linha, com campos como:

- `numero_processo`
- `numero_legado`
- `data_autuacao`
- `relator`
- `envolvidos`
- `movimentacoes`
- `origem_busca`
- `termo_busca`

## Observações

- O formato JSON Lines é útil para pós-processamento e ingestão em ferramentas que leem grandes volumes de dados.
- A limpeza inicial garante que cada execução comece com dados novos, evitando duplicações de execuções anteriores.
