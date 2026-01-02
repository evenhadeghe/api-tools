API Tool – CLI-program i Python
Beskrivning

Detta projekt är ett enkelt CLI-verktyg (Command Line Interface) som är byggt i Python.
Programmet hämtar data från olika API:er och kan:

Visa aktuellt kryptopris

Visa ett slumpmässigt citat

Visa väderdata för en vald stad

Projektet är uppdelat i flera moduler och använder en virtuell miljö.

Projektstruktur
api_tools/
│
├── .venv/                # Virtuell miljö
├── api_tool/             # Python-paket
│   ├── __init_.py
│   ├── main.py           # Huvudprogram
│   ├── crypto.py         # Kryptopriser
│   ├── quotes.py         # Citat
│   ├── weather.py        # Väder
│   └── utils.py          # Logger
│
├── requirements.txt
├── pyproject.toml
└── README.md

Installation

Klona eller ladda ner projektet

Navigera till projektets root-mapp

Skapa och aktivera en virtuell miljö

python -m venv .venv
source .venv/bin/activate   # Mac/Linux


Installera externa bibliotek

pip install -r requirements.txt


Installera projektet lokalt

pip install -e .

Användning

När projektet är installerat kan CLI-verktyget köras i terminalen:

api-tool crypto
api-tool quote
api-tool weather Stockholm


Exempel:

api-tool weather Madrid
Madrid: ☁️ +11°C

Felhantering och logging

Programmet använder logging för att:

Visa information om vad programmet gör

Hantera fel utan att programmet kraschar

Underlätta felsökning vid problem

Sammanfattning

Projektet innehåller:

Ett huvudprogram (main.py)

Flera separata moduler

Importer mellan filer

Felhantering

Virtuell miljö (.venv)

Externa bibliotek via requirements.txt

CLI-kommando via pyproject.toml