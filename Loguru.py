'''
If you want just the file output but no console, you can add this line:
    # Remove default handler (stdout)
    logger.remove()
before logger.add(...) 
'''

from loguru import logger

# Add a file sink (this is where logs go)
logger.add(
    "output.log",              # file name
    rotation="500 KB",         # rotate if >500 KB
    retention="7 days",        # keep logs for 7 days
    level="DEBUG",             # capture all logs from DEBUG upward
    # level is for keeping the alignment
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {message}"
)

logger.debug(f"Debug message")
logger.info(f"Checking value against even, odd, multiple of 5")
for i in range(20):
    if i % 2 == 0:
        logger.success(f"Value even {i}")
    elif i % 5 == 0:
        logger.warning(f"Value multiple of 5: {i}")
    else:
        logger.error(f"Error message {i}")
