"""Task 3: find the minimum cost of connecting all network cables."""

from __future__ import annotations

import heapq


def min_connection_cost(cable_lengths: list[int | float]) -> int | float:
    """Return the minimum total cost for connecting all cables.

    At every step the two shortest available cables are joined. This greedy
    choice is implemented with a min-heap.
    """
    if len(cable_lengths) < 2:
        return 0
    if any(length < 0 for length in cable_lengths):
        raise ValueError("Довжини кабелів не можуть бути від'ємними.")

    heap = list(cable_lengths)
    heapq.heapify(heap)
    total_cost: int | float = 0

    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        joined_length = first + second
        total_cost += joined_length
        heapq.heappush(heap, joined_length)

    return total_cost


if __name__ == "__main__":
    cables = [8, 4, 6, 12]
    print(f"Мінімальна вартість з'єднання: {min_connection_cost(cables)}")
