#!/usr/bin/env python3
''' Implementing a method named get_page '''


import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    ''' return a tuple containing a start and end indexies '''
    end: int = page_size * page
    start: int = end - page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

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
        """Returns page with needed data size
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        lst = self.dataset()
        start, end = index_range(page, page_size)
        return lst[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return page with needed data size in dict
        """
        dicti = {}
        dicti['page_size'] = page_size
        dicti['page'] = page
        dicti['data'] = self.get_page(page, page_size)
        tot_num = int(len(self.__dataset)) / page_size
        dicti['total_pages'] = math.ceil(tot_num)
        dicti['next_page'] = None
        dicti['prev_page'] = None
        if dicti['page'] >= 1 and dicti['page'] < dicti['total_pages']:
            dicti['next_page'] = int(dicti['page']) + 1
        if dicti['page'] > 1:
            dicti['prev_page'] = int(dicti['page']) - 1
        return dicti
