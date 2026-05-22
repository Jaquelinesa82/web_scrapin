from crawler import ProcessCrawler
from parser import process_identification
import logging
from storage import save_jsonl

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main():
    crawler = ProcessCrawler()
    process_number = "0000881-39.2016.4.05.0000"

    html = crawler.search_process(process_number)

    process_data = process_identification(html)
    save_jsonl(process_data)

    logging.info("Dados processados com sucesso.")

    logging.info(f"Encontrada {len(process_data['envolvidos'])} partes envolvidas.")

    logging.info(f"Encontrado {len(process_data['movimentacoes'])} movimentos.")

    with open("data/process_response.html", "w", encoding="utf-8") as file:
        file.write(html)

    logging.info("HTML salvo em data/home_page.html")


if __name__ == "__main__":
    main()
