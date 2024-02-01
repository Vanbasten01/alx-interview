#!/usr/bin/python3
"""This module provides functions for text processing."""
from typing import List

def validUTF8(data: List[int]) -> bool:
    """Process the given text by removing special characters
    and converting to lowercase."""
    num_bytes = 0
    mask = 1 << 7
    for byte in data:
        if not num_bytes:
            while byte & mask:
                num_bytes += 1
                mask >>= 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
        num_bytes -= 1
    return num_bytes == 0
