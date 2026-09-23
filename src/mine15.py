
import requests
import logging
logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s: - %(name)s: %(message)s'
                    )
logger = logging.getLogger()

URL= 'https://jsonplaceholder.typicode.com/photos'

def get_photo_from_album(album_id: int, limit: int = 100) -> None:
    '''Скачать фото по альбому'''
    logger.info('Starting app')
    response = requests.get(URL)
    if response.status_code != 200:
        logger.error(f'Error fetching data: {response.status_code}')
        return
    counter = 0
    logger.info(f'Getting photo from album {album_id}')
    for item in response.json():
        if item.get('albumId') == album_id:
            image_url = item.get('url')
            image_data = requests.get(image_url)
            counter += 1
            logger.info(f'Saving image {counter} to photos/{album_id}-{counter}.png')
            with open(f'E:/Digital/bakend_programm/Project13/photos/{album_id}-{counter}.png', 'wb') as image_file:
                image_file.write(image_data.content)
                if counter >= limit:
                    logger.info(f'Finished saving {counter} photos.')
                    break
    logger.info(f'Total images saved: {counter}')







if __name__ == '__main__':
    get_photo_from_album(album_id=1, limit=5)