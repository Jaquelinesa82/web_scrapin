import requests
import time
import logging
from parser import only_digits

BASE_URL = "https://www5.trf5.jus.br/cp/"
CP_BASE_URL = "https://cp.trf5.jus.br"
SEARCH_URL = "https://cp.trf5.jus.br/cp/cp.do"


PROCESS_SEARCH_TYPE = "xmlproc"
CNPJ_SEARCH_TYPE = "xmlcpf"
PARTY_NAME_SEARCH_TYPE = "xmlnomparte"


class ProcessCrawler:
    def __init__(self, delay: float = 1.0):
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0",
                "Referer": BASE_URL,
                "Origin": "https://www5.trf5.jus.br",
            }
        )

    def is_available(self) -> bool:
        try:
            response = self.session.get(BASE_URL, timeout=10)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException:
            logging.warning("Portal TRF5 indisponível no momento.")
            return False

    def search_process(self, search_type: str, value: str) -> str:
        data = {
            "navigation": "Netscape",
            "filtroCpfRequest": "",
            "tipo": search_type,
            "filtro": "",
            "filtroCPF2": "",
            "tipoproc": "T",
            "filtroRPV_Precatorios": "",
            "uf_rpv": "PE",
            "numOriginario": "",
            "numRequisitorio": "",
            "numProcessExec": "",
            "uf_rpv_OAB": "PE",
            "filtro_processo_OAB": "",
            "filtro_CPFCNPJ": "",
            "campo_data_de": "",
            "campo_data_ate": "",
            "vinculados": "true",
            "ordenacao": "D",
            "ordenacao cpf": "D",
        }

        if search_type == PROCESS_SEARCH_TYPE:
            data["filtro"] = value

        if search_type == CNPJ_SEARCH_TYPE:
            data["filtroCPF2"] = value

        if search_type == PARTY_NAME_SEARCH_TYPE:
            data["filtro"] = value
            data["exata"] = "on"

        try:
            response = self.session.post(
                SEARCH_URL,
                data=data,
                timeout=30,
            )
            response.raise_for_status()
            time.sleep(self.delay)

            return response.text

        except requests.exceptions.RequestException:
            logging.warning("Falha na conexão com o portal TRF5.")

            return ""

    def search_process_number(self, process_number: str) -> str:
        return self.search_process(PROCESS_SEARCH_TYPE, process_number)

    def search_process_cnpj(self, cnpj: str) -> str:
        return self.search_process(CNPJ_SEARCH_TYPE, cnpj)

    def search_process_party_name(self, party_name: str) -> str:
        return self.search_process(PARTY_NAME_SEARCH_TYPE, party_name)

    def search_process_cnpj_page(self, cnpj: str, page: int) -> str:
        cnpj_digits = only_digits(cnpj)

        url = f"{CP_BASE_URL}/processo/cpf/porData/ativos/" f"{cnpj_digits}/{page}"

        try:
            response = self.session.get(
                url,
                timeout=30,
            )

            response.raise_for_status()
            time.sleep(self.delay)

            return response.text

        except requests.exceptions.RequestException:
            logging.warning("Falha na conexão com a página de resultados do CNPJ.")

            return ""
