#!/usr/bin/env python3
"""
Module for filtering log data.
"""

import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message using regex substitution.

    Args:
        fields (List[str]): List of strings representing fields to obfuscate.
        redaction (str): String representing the obfuscation for the fields.
        message (str): Log line message.
        separator (str): Character separating all fields in the log line.

    Returns:
        str: Log message with specified fields obfuscated.
    """
    pattern = '|'.join(map(re.escape, fields))
    return re.sub(fr'(?<=^|{re.escape(separator)})({pattern})=[^;]+', f'\\1={redaction}', message)

if __name__ == "__main__":
    fields = ["password", "date_of_birth"]
    messages = [
        "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;",
        "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"
    ]

    for message in messages:
        print(filter_datum(fields, 'xxx', message, ';'))
