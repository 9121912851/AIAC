import random
def linear_search(arr, target, sorted=False):

    comparisons = 0
    for i, v in enumerate(arr):
        comparisons += 1
        if v == target:
            return i, comparisons
        if sorted and v > target:
            return -1, comparisons
    return -1, comparisons

def main():
    lst = sorted(random.sample(range(1, 201), 20))
    print("List (20 elements):", lst)
    present_target = lst[10]               # guaranteed present
    small_absent_target = lst[0] - 1       # absent and smaller than smallest -> early exit quickly
    large_absent_target = max(lst) + 1     # absent and larger than all -> full scan

    for target in (present_target, small_absent_target, large_absent_target):
        idx, comps = linear_search(lst, target, sorted=True)
        if idx >= 0:
            print(f"Search for {target}: found at index {idx}, comparisons = {comps}")
        else:
            print(f"Search for {target}: not found, comparisons = {comps}")

if __name__ == "__main__":
    main()