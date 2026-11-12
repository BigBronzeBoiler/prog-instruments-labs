import re

PATTERNS = {
    "telephone": re.compile(r"\+7-\([0-9]{3}\)-[0-9]{3}-[0-9]{2}-[0-9]{2}"),
    "snils": re.compile(r"[0-9]{11}"),
    "height": re.compile(r"[0-9]\.[0-9]{2}"),
    "identifier": re.compile(r"[0-9]{2}-[0-9]{2}/[0-9]{2}"),
    "blood_type": re.compile(r"(?:O|A|B|AB)[+−]"),
    "issn": re.compile(r"[0-9]{4}-[0-9]{4}"),
    "occupation": re.compile(r"[A-Za-zА-Яа-яЁё]+(?:[ -][A-Za-zА-Яа-яЁё]+)*"),
    "locale_code": re.compile(r"[a-z]{2}(?:-[a-z]{2})?"),
    "date": re.compile(r"[0-9]{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])"),
    "longitude": re.compile(
        r"-?(?:180(?:\.0+)?|(?:1[0-7][0-9]|[1-9]?[0-9])(?:\.[0-9]+)?)"
    ),
}
csv_path = "28.csv"
