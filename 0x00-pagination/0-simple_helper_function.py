#!/usr/bin/env python3
''' akes two integer arguments page and page_size '''


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    ''' return a tuple containing a start and end indexies '''
    end: int = page_size * page
    start: int = end - page_size
    return start, end
