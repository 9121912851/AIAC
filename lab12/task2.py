import time

# Static book dataset
static_books = [
    {'title': 'The Hitchhiker\'s Guide to the Galaxy', 'author': 'Douglas Adams'},
    {'title': 'The Restaurant at the End of the Universe', 'author': 'Douglas Adams'},
    {'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
    {'title': 'So Long, and Thanks for All the Fish', 'author': 'Douglas Adams'},
    {'title': 'Mostly Harmless', 'author': 'Douglas Adams'},
    {'title': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien'},
    {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien'},
    {'title': 'A Brief History of Time', 'author': 'Stephen Hawking'},
    {'title': 'Cosmos', 'author': 'Carl Sagan'},
    {'title': 'Contact', 'author': 'Carl Sagan'},
    {'title': '1984', 'author': 'George Orwell'},
    {'title': 'Animal Farm', 'author': 'George Orwell'},
    {'title': 'Dune', 'author': 'Frank Herbert'},
    {'title': 'The Foundation Trilogy', 'author': 'Isaac Asimov'},
    {'title': 'I, Robot', 'author': 'Isaac Asimov'},
    {'title': 'Fahrenheit 451', 'author': 'Ray Bradbury'},
    {'title': 'Brave New World', 'author': 'Aldous Huxley'},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
    {'title': 'Pride and Prejudice', 'author': 'Jane Austen'},
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'}
]

def linear_search(books, keyword):
    keyword = keyword.lower()
    return [book for book in books if keyword in book['title'].lower() or keyword in book['author'].lower()]

def binary_search_optimized(books, keyword):
    keyword = keyword.lower()
    books_sorted = sorted(books, key=lambda x: x['title'].lower())
    results = []

    # Binary search is not ideal for partial match.
    # So here, we'll just use binary search to locate a match, and expand from there.
    left, right = 0, len(books_sorted) - 1
    while left <= right:
        mid = (left + right) // 2
        title = books_sorted[mid]['title'].lower()
        if keyword in title:
            # Found partial match, scan neighbors
            i = mid
            while i >= 0 and keyword in books_sorted[i]['title'].lower():
                results.append(books_sorted[i])
                i -= 1
            i = mid + 1
            while i < len(books_sorted) and keyword in books_sorted[i]['title'].lower():
                results.append(books_sorted[i])
                i += 1
            break
        elif keyword < title:
            right = mid - 1
        else:
            left = mid + 1
    return results

def build_hash_index(books):
    index = {}
    for book in books:
        for word in book['title'].lower().split():
            index.setdefault(word, []).append(book)
        for word in book['author'].lower().split():
            index.setdefault(word, []).append(book)
    return index

def hash_search(index, keyword):
    return index.get(keyword.lower(), [])

def compare_searches(books, keyword):
    print(f"\n--- Comparing Search Algorithms for '{keyword}' ---")

    start = time.perf_counter()
    linear_results = linear_search(books, keyword)
    linear_time = time.perf_counter() - start
    print(f"Linear Search: {len(linear_results)} result(s) found in {linear_time:.6f} seconds.")

    start = time.perf_counter()
    binary_results = binary_search_optimized(books, keyword)
    binary_time = time.perf_counter() - start
    print(f"Binary Search: {len(binary_results)} result(s) found in {binary_time:.6f} seconds.")

    start = time.perf_counter()
    index = build_hash_index(books)
    hash_results = hash_search(index, keyword)
    hash_time = time.perf_counter() - start
    print(f"Hash Search:   {len(hash_results)} result(s) found in {hash_time:.6f} seconds (including index build).")

if __name__ == "__main__":
    SEARCH_KEYWORD = "Douglas"
    compare_searches(static_books, SEARCH_KEYWORD)
