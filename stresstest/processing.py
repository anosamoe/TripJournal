import multiprocessing as mp
import random
import string
import logging
import subprocess
from createStories import *

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

# create a file handler

handler = logging.FileHandler('multiprocessing.log')
handler.setLevel(logging.INFO)
# write logs to the file "multiprocessing.log"
logger.addHandler(handler)

logger.info('Start execution of program')


# Define an output queue
output = mp.Queue()


# Setup a list of processes that we want to run
with open('script.sh', 'rb') as file:
    script = file.read()


with open('script2.sh', 'rb') as file:
    script = file.read()

rc = subprocess.call(createStories.publish_story, shell=True)
rc = subprocess.call(script, shell=True)

# Run processes

# Exit the completed processes

# Get process results from the output queue

logger.info('finish')