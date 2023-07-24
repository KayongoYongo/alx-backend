#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page: int, page_size: int) -> tuple:
    "Claculates the range of the page and returns a range"""
    start_index = (page - 1) * page_size

    # Calculate the end index
    end_index = page * page_size

    return (start_index, end_index)
