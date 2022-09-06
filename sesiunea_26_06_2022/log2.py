import sys
import logging

# configuram root logger pentru a scrie in fisier
logging.basicConfig(filename="log2.log", level=logging.DEBUG)

logging.info("Starting...")

logging.debug(f"Running on Python: {sys.version}")


logging.info("Job done. Exiting...")