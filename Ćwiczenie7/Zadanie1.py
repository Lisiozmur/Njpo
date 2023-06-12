import requests
from tqdm import tqdm
import logging

logging.basicConfig(level=logging.ERROR)


def download_image(url, destination):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        total_size = int(response.headers.get("Content-Length", 0))
        progress_bar = tqdm(total=total_size, unit='B', unit_scale=True)

        with open(destination, "wb") as file:
            for data in response.iter_content(1024):
                file.write(data)
                progress_bar.update(len(data))

        progress_bar.close()
        logging.info(f"Zdjęcie pobrano ze strony: {url} to {destination}")

    except Exception as e:
        logging.error(f"Bąd pobierania {url}: {str(e)}")


url = "https://pl.wikipedia.org/wiki/Plik:Lesser.malay.mouse.deer.arp.jpg"
destination = "kanczyl.jpg"

download_image(url, destination)
