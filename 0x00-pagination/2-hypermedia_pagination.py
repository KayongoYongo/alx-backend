#!/usr/bin/env python3
"""simple pagination"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def index_range(page: int, page_size: int) -> tuple:
        """Calculates the range of the page and returns a range
        """
        start_index = (page - 1) * page_size

        # Calculate the end index
        end_index = page * page_size

        return (start_index, end_index)

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a dataset for a given range
        """
        assert type(page_size) is int and page_size > 0
        assert type(page) is int and page > 0

        dataset = self.dataset()
        data_length = len(dataset)

        try:
            pages = index_range(page, page_size)
            return dataset[pages[0]:pages[1]]
        except Exception:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns a page of the dataset.
        """
        total_pages = len(self.dataset()) // page_size + 1
        data = self.get_page(page, page_size)
        info = {
            "page": page,
            "page_size": page_size if page_size <= len(data) else len(data),
            "total_pages": total_pages,
            "data": data,
            "prev_page": page - 1 if page > 1 else None,
            "next_page": page + 1 if page + 1 <= total_pages else None
        }
        return info
