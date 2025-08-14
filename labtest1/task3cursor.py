def recommend_movies(preferred_genres):
    # Few-shot examples
    movie_db = [
        {"title": "Inception", "genre": "sci-fi"},
        {"title": "The Godfather", "genre": "crime"},
        {"title": "Finding Nemo", "genre": "animation"},
        {"title": "The Shawshank Redemption", "genre": "drama"},
        {"title": "Avengers: Endgame", "genre": "action"},
        {"title": "La La Land", "genre": "musical"},
        {"title": "Get Out", "genre": "horror"},
        {"title": "The Hangover", "genre": "comedy"},
        {"title": "Titanic", "genre": "romance"},
        {"title": "Interstellar", "genre": "sci-fi"},
    ]

    recommendations = []
    for genre in preferred_genres:
        for movie in movie_db:
            if movie["genre"].lower() == genre.lower():
                recommendations.append(movie["title"])
    return list(set(recommendations))

if __name__ == "__main__":
    user_input = input("Enter your preferred genres (comma separated): ")
    genres = [g.strip() for g in user_input.split(",")]
    movies = recommend_movies(genres)
    if movies:
        print("Recommended movies for you:")
        for m in movies:
            print("-", m)
    else:
        print("No recommendations found for the selected genres.")