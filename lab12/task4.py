import random
import time
import heapq

def generate_stock_data(num_stocks=100):
    stock_data = []
    for i in range(num_stocks):
        symbol = f"STK{i:03d}"
        open_price = round(random.uniform(100, 1000), 2)
        close_price = round(open_price * (1 + random.uniform(-0.1, 0.1)), 2)
        stock_data.append({
            'symbol': symbol,
            'open': open_price,
            'close': close_price
        })
    return stock_data

def percentage_change(stock):
    return ((stock['close'] - stock['open']) / stock['open']) * 100

def heap_sort_stocks(stock_data):
    heap = [(-percentage_change(stock), stock) for stock in stock_data]
    heapq.heapify(heap)
    sorted_stocks = [heapq.heappop(heap)[1] for _ in range(len(heap))]
    return sorted_stocks

def build_stock_lookup(stock_data):
    return {stock['symbol']: stock for stock in stock_data}

def search_stock(symbol, stock_lookup):
    return stock_lookup.get(symbol, "Stock not found")

def compare_sorting(stock_data):
    print("\n--- Sorting Performance Comparison ---")
    start = time.time()
    sorted_heap = heap_sort_stocks(stock_data)
    heap_sort_time = time.time() - start
    print(f"Heap Sort Time:     {heap_sort_time:.6f} seconds")
    start = time.time()
    sorted_builtin = sorted(stock_data, key=percentage_change, reverse=True)
    builtin_sort_time = time.time() - start
    print(f"Built-in Sort Time: {builtin_sort_time:.6f} seconds")
    print("Top stock (Heap Sort):    ", sorted_heap[0]['symbol'], f"{percentage_change(sorted_heap[0]):.2f}%")
    print("Top stock (Built-in sort):", sorted_builtin[0]['symbol'], f"{percentage_change(sorted_builtin[0]):.2f}%")

def compare_searching(stock_data, test_symbol):
    print("\n--- Searching Performance Comparison ---")
    stock_lookup = build_stock_lookup(stock_data)
    start = time.time()
    result_hash = search_stock(test_symbol, stock_lookup)
    hash_time = time.time() - start
    print(f"Hash Map Lookup Time: {hash_time:.10f} seconds")
    print(f"Found (Hash Map): {result_hash}")
    start = time.time()
    result_linear = next((s for s in stock_data if s['symbol'] == test_symbol), "Stock not found")
    linear_time = time.time() - start
    print(f"Linear Search Time:   {linear_time:.10f} seconds")
    print(f"Found (Linear): {result_linear}")

if __name__ == "__main__":
    stock_data = generate_stock_data(1000)
    test_symbol = "STK500"
    compare_sorting(stock_data)
    compare_searching(stock_data, test_symbol)
