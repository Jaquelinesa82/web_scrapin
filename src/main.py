from crawler import ProcessCrawler
from parser import process_identification
import logging
from storage import save_jsonl, clear_jsonl

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


def main() -> None:
    clear_jsonl()
    logging.info("Arquivo de saída limpo.")

    crawler = ProcessCrawler()

    for process_number in PROCESS_NUMBERS:
        logging.info("Buscar processo: %s", process_number)

        html = crawler.search_process(process_number)
        process_data = process_identification(html)

        process_data["origem_busca"] = "numero_processo"
        process_data["termo_busca"] = process_number

        save_jsonl(process_data)

    logging.info(
        "Processo %s foi salvo com %s partes envolvidas e %s movimentações.",
        process_data["numero_processo"],
        len(process_data["envolvidos"]),
        len(process_data["movimentacoes"]),
    )


if __name__ == "__main__":
    main()
