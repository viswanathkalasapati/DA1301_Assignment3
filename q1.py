from collection import deque
from typing import List


def printer_queue_order(pages: List[int]) -> List[int]:
    """
    Problem 1: Round-robin printer.

    Given the number of pages for each document (in submission order),
    simulate round-robin printing (one page at a time, front of queue
    to back of queue) and return the document indices in the order
    they finish printing.

    Args:
        pages: pages[i] is the number of pages in document i.

    Returns:
        List of document numbers in the order they finish printing.
    """

    queue = deque()
    result = []

    for i, p in enumerate(pages):
        if p > 0:
            queue.append([i, p])

    while queue:
        doc_idx, pages_left = queue.popleft()
        pages_left -= 1
        if pages_left == 0:
            result.append(doc_idx)
        else:
            queue.append([doc_idx, pages_left])

    return result


if __name__ == "__main__":
    # Example sanity check (see test.py for the real test cases)
    print(printer_queue_order([1, 1, 1]))  # expected: [0, 1, 2]
