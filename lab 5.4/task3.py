import random

# Sample product catalog with categories
PRODUCTS = [
    {"id": 1, "name": "Wireless Mouse", "category": "Electronics"},
    {"id": 2, "name": "Yoga Mat", "category": "Fitness"},
    {"id": 3, "name": "Cookbook", "category": "Books"},
    {"id": 4, "name": "Bluetooth Speaker", "category": "Electronics"},
    {"id": 5, "name": "Running Shoes", "category": "Fitness"},
    {"id": 6, "name": "Mystery Novel", "category": "Books"},
    {"id": 7, "name": "Coffee Maker", "category": "Home"},
    {"id": 8, "name": "Desk Lamp", "category": "Home"},
    {"id": 9, "name": "Water Bottle", "category": "Fitness"},
    {"id": 10, "name": "Graphic T-Shirt", "category": "Fashion"},
    {"id": 11, "name": "Sunglasses", "category": "Fashion"},
    {"id": 12, "name": "Travel Backpack", "category": "Travel"},
]

def get_user_history():
    print("Enter product IDs you have purchased/interested in (comma separated):")
    print("Available products:")
    for p in PRODUCTS:
        print(f"{p['id']}: {p['name']} ({p['category']})")
    ids = input("Product IDs: ")
    try:
        selected_ids = set(int(i.strip()) for i in ids.split(",") if i.strip().isdigit())
    except ValueError:
        selected_ids = set()
    user_history = [p for p in PRODUCTS if p["id"] in selected_ids]
    return user_history

def recommend_products(user_history, products, num_recommendations=5):
    history_categories = set(item["category"] for item in user_history)
    recommendations = []
    explained = []
    familiar_products = [p for p in products if p["category"] in history_categories and p not in user_history]
    new_categories = set(p["category"] for p in products) - history_categories
    diverse_products = [p for p in products if p["category"] in new_categories]
    random.shuffle(familiar_products)
    random.shuffle(diverse_products)
    for p in familiar_products[:num_recommendations//2]:
        recommendations.append(p)
        explained.append(f"Recommended '{p['name']}' because you have shown interest in {p['category']} products.")
    for p in diverse_products[:num_recommendations - len(recommendations)]:
        recommendations.append(p)
        explained.append(f"Recommended '{p['name']}' to introduce you to the {p['category']} category for more variety.")
    return recommendations, explained

def main():
    user_history = get_user_history()
    if not user_history:
        print("No valid user history entered. Showing random recommendations.")
        user_history = []
    recommendations, explanations = recommend_products(user_history, PRODUCTS)
    print("\nProduct Recommendations:")
    for rec, exp in zip(recommendations, explanations):
        print(f"- {rec['name']} ({rec['category']}): {exp}")

if __name__ == "__main__":
    main()