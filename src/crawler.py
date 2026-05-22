import requests
import time


BASE_URL = "https://www5.trf5.jus.br/cp/"
SEARCH_URL = "https://cp.trf5.jus.br/cp/cp.do"



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

    def search_process(self, process_number: str) -> str:
            data = {
                "navigation": "Netscape",
                "filtroCpfRequest": "",
                "tipo": "xmlproc",
                "filtro": process_number,
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

            response = self.session.post(
                SEARCH_URL,
                data=data,
                timeout=30,
            )

            response.raise_for_status()

            time.sleep(self.delay)

            return response.text
