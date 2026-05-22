from crawler import ProcessCrawler
from parser import process_identification
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main():
    crawler = ProcessCrawler()
    process_number = "0000881-39.2016.4.05.0000"
    
    logging.info(f"Searching process: {process_number}")

    html = crawler.search_process(process_number)
    
    process_data = process_identification(html)
    
    logging.info(process_data)
    
    with open("data/process_response.html", "w", encoding="utf-8") as file:
        file.write(html)
    
    logging.info("HTML salvo em data/home_page.html")


if __name__ == "__main__":
    main()