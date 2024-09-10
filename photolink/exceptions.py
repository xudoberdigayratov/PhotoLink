class PhotoLinkException(Exception):
    """Barcha PhotoLink xatoliklari uchun asosiy istisno."""

    pass


class FileTooLargeException(PhotoLinkException):
    """Fayl hajmi cheklovdan oshganda chiqariladi."""

    pass


class InvalidClientIdException(PhotoLinkException):
    """Noto'g'ri client ID mavjud bo'lganda chiqariladi."""

    pass


class InvalidFileTypeException(PhotoLinkException):
    """Noto'g'ri fayl turi bo'lganda chiqariladi."""

    pass


class FileNotFoundException(PhotoLinkException):
    """Fayl topilmasa chiqariladi."""

    pass


class UnexpectedUploadError(PhotoLinkException):
    """Yuklashda kutilmagan xatolik yuzaga kelganda chiqariladi."""

    pass
