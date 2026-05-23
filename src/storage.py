import json
from pathlib import Path


def clear_jsonl(output_path: str = "data/processos.jsonl") -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("", encoding="utf-8")


def save_jsonl(data: dict, output_path: str = "data/processos.jsonl") -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("a", encoding="utf-8") as file:
        file.write(json.dumps(data, ensure_ascii=False) + "\n")
