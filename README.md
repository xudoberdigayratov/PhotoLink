# PhotoLink

Python PhotoLink API wrapper

- [Documentation](https://photolink.uz);

```bash
$ python3 -m pip install photolink
# with asyncio support
$ python3 -m pip install 'photolink[aio]'
```

## Example
```python
from photolink import PhotoLink

photolink = PhotoLink(client_id='lSeA0sSUgd')
upload = photolink.upload_image(file_path='doppi.png')

print(upload)

```

## Async Example
```python
import asyncio
from photolink.aio import PhotoLink

async def main():
    photolink = PhotoLink(client_id='lSeA0sSUgd')
    print(await photolink.upload_image(file_path='doppi.png'))


asyncio.run(main())
```
