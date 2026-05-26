import logging

from crawler import ProcessCrawler
from parser import normalize_party_name, process_identification, process_list
from storage import save_jsonl

MAX_CNPJ_PAGES = 2


def process_and_save(
    crawler: ProcessCrawler,
    process_number: str,
    processed_numbers: set[str],
    search_origin: str,
    search_term: str,
) -> None:
    logging.info(
        "Buscando detalhes do processo: %s",
        process_number,
    )

    process_html = crawler.search_process_number(
        process_number,
    )

    if not process_html:
        return

    process_data = process_identification(
        process_html,
    )

    if not process_data["numero_processo"]:
        logging.info(
            "O processo %s é inexistente ou tramita em segredo de justiça.",
            process_number,
        )
        return

    if process_data["numero_processo"] in processed_numbers:
        logging.info(
            "Processo %s já processado. Ignorando.",
            process_data["numero_processo"],
        )
        return

    processed_numbers.add(
        process_data["numero_processo"],
    )

    process_data["origem_busca"] = search_origin
    process_data["termo_busca"] = search_term

    save_jsonl(process_data)

    logging.info(
        "Processo %s salvo com %s partes envolvidas e %s movimentações.",
        process_data["numero_processo"],
        len(process_data["envolvidos"]),
        len(process_data["movimentacoes"]),
    )


def search_number(
    crawler: ProcessCrawler,
    numbers: list[str],
    processed_numbers: set[str],
) -> None:
    for process_number in numbers:
        process_and_save(
            crawler,
            process_number,
            processed_numbers,
            "numero_processo",
            process_number,
        )

    logging.info("Busca por número de processo finalizada.")


def search_cnpj(
    crawler: ProcessCrawler,
    cnpj: str,
    processed_numbers: set[str],
) -> None:
    for page in range(MAX_CNPJ_PAGES):
        logging.info(
            "Buscando processos por CNPJ: %s na página %s",
            cnpj,
            page,
        )

        process_html = crawler.search_process_cnpj_page(
            cnpj,
            page,
        )

        if not process_html:
            break

        process_numbers = process_list(process_html)

        if not process_numbers:
            logging.info(
                "Nenhum processo encontrado na página %s.",
                page,
            )
            break

        logging.info(
            "Foram encontrados %s processos na página %s.",
            len(process_numbers),
            page,
        )

        for process_number in process_numbers:
            process_and_save(
                crawler,
                process_number,
                processed_numbers,
                "cnpj",
                cnpj,
            )

    logging.info("Busca por CNPJ finalizada.")


def search_party_name(
    crawler: ProcessCrawler,
    party_name: str,
    processed_numbers: set[str],
) -> None:

    party_name = normalize_party_name(
        party_name,
    )
    logging.info(
        "Buscando processo por nome da parte: %s",
        party_name,
    )

    process_html = crawler.search_process_party_name(
        party_name,
    )

    if not process_html:
        return

    process_numbers = process_list(process_html)

    logging.info(
        "Foram encontrados %s processos.",
        len(process_numbers),
    )

    for process_number in process_numbers:
        process_and_save(
            crawler,
            process_number,
            processed_numbers,
            "nome_parte",
            party_name,
        )

    logging.info("Busca por nome da parte finalizada.")
