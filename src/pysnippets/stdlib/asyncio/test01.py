import os
import asyncio
import logging
import warnings

# Run asyncio in debug mode for easier development
# https://docs.python.org/3/library/asyncio-dev.html#debug-mode-of-asyncio
os.putenv('PYTHONASYNCIODEBUG', '1')
logging.basicConfig(level=logging.DEBUG)
warnings.filterwarnings(ResourceWarning)

async def hello_world():
    print("Hello world!")

hello_world()