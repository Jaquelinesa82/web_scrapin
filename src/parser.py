from bs4 import BeautifulSoup


def clean_text(value: str | None) -> str:
    if not value:
        return ""

    return " ".join(value.split())


def process_identification(html: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    page_text = clean_text(soup.get_text(" "))

    numero_processo = ""
    numero_legado = ""
    data_autuacao = ""
    relator = ""

    if "PROCESSO Nº" in page_text:
        process_part = page_text.split("PROCESSO Nº")[1]
        numero_processo = process_part.strip().split(" ")[0]

    if "PROC. ORIGINÁRIO Nº:" in page_text:
        legacy_part = page_text.split("PROC. ORIGINÁRIO Nº:")[1]
        numero_legado = legacy_part.strip().split(" ")[0]

    if "AUTUADO EM" in page_text:
        autuacao_part = page_text.split("AUTUADO EM")[1]
        data_autuacao = autuacao_part.strip().split(" ")[0]

    if "RELATOR" in page_text:
        relator_part = page_text.split("RELATOR")[1]
        relator = relator_part.replace(":", "").strip().split("42/")[0].strip()

    if not numero_processo:
        numero_processo = numero_legado

    return {
        "numero_processo": numero_processo,
        "numero_legado": numero_legado,
        "data_autuacao": data_autuacao,
        "relator": relator,
    }
