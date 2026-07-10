---
title: Início
---

# TRF5 Process Crawler

Projeto para consulta processual no portal do TRF5. Permite buscar processos por número, CPF/CNPJ ou nome da parte, extrair informações e persistir em formato JSON Lines.

## Principais funcionalidades

- Busca interativa por número do processo, CPF/CNPJ e nome da parte
- Extração e normalização de dados (partes, movimentações, identificação)
- Paginação na busca por CNPJ
- Persistência em `data/processos.jsonl`

## Começando rápido

1. Veja as instruções de instalação: [Instalação](installation.md)
2. Siga o guia rápido: [Início Rápido](quick-start.md)
3. Leia a arquitetura do sistema: [Arquitetura](architecture.md)
4. Consulte a documentação dos módulos: [Crawler](crawler.md), [Parser](parser.md), [Services](services.md), [Storage](storage.md)
5. Veja as regras de negócio: [Regras de Negócio](business-rules.md)

## Exemplos rápidos

Executar o programa interativo:

```bash
python src/main.py
```

Rodar o servidor de documentação local:

```bash
mkdocs serve
```

---
