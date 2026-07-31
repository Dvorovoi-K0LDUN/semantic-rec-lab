from pathlib import Path
from urllib.request import urlretrieve
from zipfile import ZipFile


DATASET_URL = (
    "https://files.grouplens.org/datasets/movielens/ml-100k.zip"
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
ARCHIVE_PATH = RAW_DATA_DIR / "ml-100k.zip"


def main() -> None:
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    print("Project root:", PROJECT_ROOT)
    print("Raw data directory:", RAW_DATA_DIR)

    # TODO 1:
    # Проверить, существует ли архив.
    # Если существует — не скачивать его повторно.
    if ARCHIVE_PATH.exists():
        print(ARCHIVE_PATH)
    else:
        print("Downloading dataset ?")
        accept = input(" Do you want to download the dataset? (y/n): ")
    


    # TODO 2:
    # Скачать DATASET_URL в ARCHIVE_PATH.

    # TODO 3:
    # Распаковать архив в RAW_DATA_DIR.


if __name__ == "__main__":
    main()