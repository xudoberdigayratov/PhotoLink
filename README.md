# PhotoLink

Python PhotoLink API wrapper

[//]: # (- [Documentation]&#40;https://python-telegraph.readthedocs.io/en/latest/&#41;)

```bash
$ python3 -m pip install photolink
# with asyncio support
$ python3 -m pip install 'photolink[aio]'
```

## Example
```python
from photolink import PhotoLink

photolink = PhotoLink()
upload = photolink.upload_image(file_path='doppi.png')

print(upload)

```

## Async Example
```python
import asyncio
from photolink.aio import PhotoLink

async def main():
    photolink = PhotoLink()
    print(await photolink(file_path='doppi.png'))


asyncio.run(main())
```
