def process_scores(scores):
    if not scores:
        print("The list of scores is empty.")
        return
    total = 0
    highest = scores[0]
    lowest = scores[0]
    for s in scores:
        total += s
        if s > highest:
            highest = s
        if s < lowest:
            lowest = s
    avg = total / len(scores)
    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)

my_scores = [85, 92, 78, 65, 95, 88, 70]
process_scores(my_scores)