import logging

from crawler import ProcessCrawler
from parser import process_identification, process_list
from storage import clear_jsonl, save_jsonl

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


PROCESS_NUMBERS = [
    "0000881-39.2016.4.05.0000",
    "0013996-35.2011.4.05.8300",
    "0000007-41.2011.4.05.8403",
    "0009865-80.2014.4.05.0000",
    "0014481-40.2010.4.05.0000",
    "0005037-07.2013.4.05.8300",
]

PROCESS_CNPJ = "34.020.354/0001-10"

PARTY_NAME = "CAIXA SEGURADORA SA"

MAX_CNPJ_PAGES = 2


def search_number(
    crawler: ProcessCrawler,
    numbers: list[str],
    processed_numbers: set[str],
) -> None:
    for process_number in numbers:
        logging.info("Buscar processo: %s", process_number)

        process_html = crawler.search_process_number(
            process_number,
        )

        if not process_html:
            break

        process_data = process_identification(
            process_html,
        )

        if process_data["numero_processo"] in processed_numbers:
            logging.info(
                "Processo %s já processado. Ignorando.",
                process_data["numero_processo"],
            )
            continue

        processed_numbers.add(
            process_data["numero_processo"],
        )

        process_data["origem_busca"] = "numero_processo"
        process_data["termo_busca"] = process_number

        save_jsonl(process_data)

        logging.info(
            "Processo %s salvo com %s partes envolvidas e %s movimentações.",
            process_data["numero_processo"],
            len(process_data["envolvidos"]),
            len(process_data["movimentacoes"]),
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

        process_html = crawler.search_process_cnpj_page(cnpj, page)

        if not process_html:
            break

        process_numbers = process_list(process_html)

        if not process_numbers:
            logging.info("Nenhum processo encontrado na página %s.", page)
            break

        logging.info(
            "Foram encontrados %s processos na página %s.",
            len(process_numbers),
            page,
        )

        for process_number in process_numbers:
            logging.info(
                "Buscando detalhes do processo: %s",
                process_number,
            )

            process_html = crawler.search_process_number(
                process_number,
            )

            if not process_html:
                continue

            process_data = process_identification(
                process_html,
            )

            if process_data["numero_processo"] in processed_numbers:
                logging.info(
                    "Processo %s já processado. Ignorando.",
                    process_data["numero_processo"],
                )
                continue

            processed_numbers.add(
                process_data["numero_processo"],
            )

            process_data["origem_busca"] = "cnpj"
            process_data["termo_busca"] = cnpj

            save_jsonl(process_data)

            logging.info(
                "Processo %s salvo com %s partes envolvidas e %s movimentações.",
                process_data["numero_processo"],
                len(process_data["envolvidos"]),
                len(process_data["movimentacoes"]),
            )

    logging.info("Busca por CNPJ finalizada.")


def search_party_name(
    crawler: ProcessCrawler, party_name: str, processed_numbers: set[str]
) -> None:

    logging.info(
        "Buscando processo por nome da parte: %s",
        party_name,
    )

    process_html = crawler.search_process_party_name(party_name)

    if not process_html:
        return

    process_numbers = process_list(process_html)

    logging.info(
        "Foram encontrados %s processos.",
        len(process_numbers),
    )

    for process_number in process_numbers:
        logging.info("Busca detalhes do processo: %s", process_number)

        process_html = crawler.search_process_number(
            process_number,
        )
        if not process_html:
            continue

        process_data = process_identification(process_html)

        if process_data["numero_processo"] in processed_numbers:
            logging.info(
                "Processo %s já processado. Ignorando",
                process_data["numero_processo"],
            )
            continue

        processed_numbers.add(process_data["numero_processo"])
        process_data["origem_busca"] = "nome_parte"
        process_data["termo_busca"] = party_name

        save_jsonl(process_data)

        logging.info(
            "Parte do processo %s salvo com %s partes envolvidas e %s movimentações.",
            process_data["numero_processo"],
            len(process_data["envolvidos"]),
            len(process_data["movimentacoes"]),
        )

    logging.info("Busca por nome da parte finalizada.")


def main() -> None:
    crawler = ProcessCrawler()

    if not crawler.is_available():
        return

    processed_numbers = set()

    clear_jsonl()
    logging.info("Arquivo de saída limpo.")

    search_number(
        crawler,
        PROCESS_NUMBERS,
        processed_numbers,
    )

    search_cnpj(
        crawler,
        PROCESS_CNPJ,
        processed_numbers,
    )

    search_party_name(
        crawler,
        PARTY_NAME,
        processed_numbers,
    )


if __name__ == "__main__":
    main()
