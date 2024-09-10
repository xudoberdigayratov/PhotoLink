import os

import httpx

from .exceptions import *
from .utils import *


class PhotoLink:
    """ PhotoLink API Client

    :param client_id: client_id
    :type client_id: str

    :param domain: domain (e.g. alternative mirror cdn.photolink.uz)
    """

    def __init__(self, client_id='lSeA0sSUgd', domain='photolink.uz'):
        self.client_id = client_id
        self.domain = domain
        self.session = httpx.AsyncClient()

    async def upload_image(self, file_path):
        """ Accepts an uploaded file and only accepts image files (JPEG, PNG, WEBP).

        :param file_path: path to the image file
        """
        if not self.client_id:
            raise InvalidClientIdException(errors['InvalidClientID'])
        if not os.path.exists(file_path):
            raise FileNotFoundException(errors['FileNotFoundError'])

        file_size = os.path.getsize(file_path)
        if file_size > 1024 * 1024:
            raise FileTooLargeException(errors['FILE_SIZE_ERROR'])

        extension = file_path.rsplit('.', 1)[1].lower()

        content_type = mime_types.get(extension)
        if content_type is None:
            raise InvalidFileTypeException(errors['INVALID_CONTENT_TYPE'])

        with open(file_path, 'rb') as f:
            response = (await self.session.post(
                "https://api.{}/upload-image/".format(self.domain),
                params={'client_id': self.client_id},
                files={'file': (file_path, f, content_type)}
            )).json()
            if response['error']:
                if response['error_type'] == 'InvalidClientID':
                    raise InvalidClientIdException(errors['InvalidClientID'])
                elif response['error_type'] == 'INVALID_CONTENT_TYPE':
                    raise InvalidFileTypeException(errors['INVALID_CONTENT_TYPE'])
                elif response['error_type'] == 'FILE_SIZE_ERROR':
                    raise FileTooLargeException(errors['FILE_SIZE_ERROR'])
                elif response['error_type'] == 'FileNotFoundError':
                    raise FileNotFoundException(errors['FileNotFoundError'])
                elif response['error_type'] == 'NoCredentialsError':
                    raise InvalidClientIdException(errors['NoCredentialsError'])
                elif response['error_type'] == 'UNEXPECTED_ERROR':
                    raise UnexpectedUploadError(errors['UNEXPECTED_ERROR'])
                else:
                    raise UnexpectedUploadError(errors['UNEXPECTED_ERROR'])
            else:
                return dict(message="Fayl muvaffaqiyatli yuklandi.", file_url=response['file_url'])
