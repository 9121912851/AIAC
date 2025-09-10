def process_scores(scores):
    if not scores:
        return print("The list of scores is empty.")
    total = sum(scores)
    avg = total / len(scores)
    print("Average:", avg)
    print("Highest:", max(scores))
    print("Lowest:", min(scores))

my_scores = [85, 92, 78, 65, 95, 88, 70]
process_scores(my_scores)
