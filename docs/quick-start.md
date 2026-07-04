---
title: Quick Start
---

# Quick Start

Esta página apresenta um exemplo rápido de uso do projeto após a instalação.

## Executar o projeto

1. Ative o ambiente virtual criado:

```bash
source .venv/bin/activate
```

2. Execute o programa interativo:

```bash
python src/main.py
```

3. Escolha o tipo de busca desejado:

- `1` para número do processo
- `2` para CPF/CNPJ
- `3` para nome da parte ou advogado
- `0` para sair

## Exemplo de fluxo

Suponha que você queira buscar por número de processo:

```text
Tipos de busca:
1 - Número do processo
2 - CPF/CNPJ
3 - Nome da parte ou advogado
0 - Sair

Escolha o tipo de busca: 1
Digite o número do processo: 0000000-00.0000.0.00.0000
```

O sistema fará a consulta, processará os detalhes do processo e salvará o resultado em `data/processos.jsonl`.

## Localizar a documentação

- [Instalação](installation.md)
- [Arquitetura](architecture.md)
- [Crawler](crawler.md)
- [Parser](parser.md)
- [Services](services.md)
- [Storage](storage.md)
- [Regras de Negócio](business-rules.md)
