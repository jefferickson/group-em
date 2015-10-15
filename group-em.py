#! /usr/bin/env python3

import itertools
import collections

def find_addends(target, n):
    assert target >= n, 'target must be greater than or equal to n.'

    addends = []

    def helper(target, n, precede = []):
        if n == 1:
            addends.append(precede + [target])
            return None

        max_addend = target - n + 1
        for i in range(1, max_addend + 1):
            helper(target - i, n - 1, precede + [i])

    helper(target, n)
    return addends

def find_groups(objects, num_of_groups):
    groups = []
    groupings = find_addends(len(objects), num_of_groups)
    for perm in itertools.permutations(objects):
        for grouping in groupings:
            current_group = []
            perm_queue = collections.deque(perm)
            for num_in_subset in grouping:
                subset = []
                for i in range(num_in_subset):
                    subset.append(perm_queue.popleft())
                current_group.append(subset)
            groups.append(current_group)

    return groups

if __name__ == '__main__':
    groups = find_groups(range(5), 3)

    for group in groups:
        print(group)