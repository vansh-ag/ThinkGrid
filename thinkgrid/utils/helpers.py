from pathlib import Path


def sanitize_filename(text: str) -> str:
    return (
        text.replace(" ", "_")
        .replace("/", "_")
        .replace("\\", "_")
        .lower()
    )


def ensure_directory(path: str):
    Path(path).mkdir(
        parents=True,
        exist_ok=True
    )