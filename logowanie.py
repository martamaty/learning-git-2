""" 
import logging
logging.warn("warning!")
logging.debug("debug")
"""

#zmiana poziomu logowania
import logging
logging.basicConfig(level=logging.DEBUG)
logging.warn("warning!")
logging.debug("debug")