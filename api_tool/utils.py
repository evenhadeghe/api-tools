import logging

# Skapa logger
logger = logging.getLogger("api_tool")
logger.setLevel(logging.DEBUG)  # Alla nivåer loggas

# Skapa formatter för snygg utskrift
formatter = logging.Formatter("[%(levelname)s] %(message)s")

# Skapa konsol-hanterare
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Lägg till hanterare till loggern
logger.addHandler(console_handler)