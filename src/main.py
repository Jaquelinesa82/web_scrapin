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

    logging.info("Busca por número de processo finalizada..")


def search_cnpj(
    crawler: ProcessCrawler,
    cnpj: str,
    processed_numbers: set[str],
) -> None:
    logging.info(
        "Buscando processos por CNPJ: %s",
        cnpj,
    )

    html = crawler.search_process_cnpj(cnpj)

    process_numbers = process_list(html)

    logging.info(
        "Foram encontrados %s processos na primeira página.",
        len(process_numbers),
    )

    for process_number in process_numbers:
        logging.info(
            "Buscando detalhes do processo: %s",
            process_number,
        )

        process_html = crawler.search_process_number(
            process_number,
        )

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


def main() -> None:
    clear_jsonl()

    logging.info("Arquivo de saída limpo.")

    crawler = ProcessCrawler()

    processed_numbers = set()

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


if __name__ == "__main__":
    main()
