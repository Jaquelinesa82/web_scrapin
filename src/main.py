import logging
from crawler import ProcessCrawler
from services.search import search_cnpj, search_number, search_party_name
from storage import clear_jsonl

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main() -> None:
    crawler = ProcessCrawler()

    if not crawler.is_available():
        return

    clear_jsonl()

    processed_numbers = set()

    while True:
        print("\nTipos de busca:")
        print("1 - Número do processo")
        print("2 - CPF/CNPJ")
        print("3 - Nome da parte ou advogado")
        print("0 - Sair")

        option = input("\nEscolha o tipo de busca: ").strip()

        if option == "1":
            process_number = input("Digite o número do processo: ").strip()

            process_numbers = [
                number.strip() for number in process_number.split(",") if number.strip()
            ]

            search_number(
                crawler,
                process_numbers,
                processed_numbers,
            )

        elif option == "2":
            cnpj = input("Digite o CPF/CNPJ: ").strip()

            search_cnpj(
                crawler,
                cnpj,
                processed_numbers,
            )

        elif option == "3":
            party_name = input("Digite o nome da parte ou advogado: ").strip()

            search_party_name(
                crawler,
                party_name,
                processed_numbers,
            )

        elif option == "0":
            print("\nEncerrando execução.")
            break

        else:
            print("Opção inválida.")
            continue

        while True:
            new_search = input("\nDeseja realizar outra busca? (s/n): ").strip().lower()

            if new_search == "s":
                break

            if new_search == "n":
                print("\nEncerrando execução.")
                return

            print("Opção inválida. Digite apenas 's' ou 'n'.")


if __name__ == "__main__":
    main()
