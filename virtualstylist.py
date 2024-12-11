import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests

# Fashion dataset (basic example)
outfits = [
    {"id": 1, "description": "Red evening gown, perfect for formal dinners."},
    {"id": 2, "description": "Casual jeans and white t-shirt, great for outings."},
    {"id": 3, "description": "Black leather jacket with boots, ideal for chilly weather."},
    {"id": 4, "description": "Summer dress with floral patterns, light and breezy."},
    {"id": 5, "description": "Business suit in navy blue, professional and sleek."},
]

# Function to recommend an outfit
def recommend_outfit(user_input):
    descriptions = [outfit["description"] for outfit in outfits]
    descriptions.insert(0, user_input)  # Add user input to descriptions for comparison

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(descriptions)

    # Calculate cosine similarity
    similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    # Find the most similar outfit
    most_similar_index = similarities.argmax()
    return outfits[most_similar_index]

# Weather-based adjustment
def adjust_for_weather(outfit, location="New York"):
    api_key = "796e89f9592a27e35e08986f3a4d4608"  # Get an API key from OpenWeatherMap
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    try:
        response = requests.get(weather_url)
        weather = response.json()
        temp = weather["main"]["temp"]

        # Adjust recommendations based on temperature
        if temp < 10:
            suggestion = "Add a heavy coat or sweater for warmth."
        elif 10 <= temp <= 20:
            suggestion = "Consider a light jacket."
        else:
            suggestion = "Light clothing should be fine."

        return f"{outfit} Suggestion: {suggestion}"
    except Exception as e:
        return f"{outfit} Weather data not available."

# Main program
def virtual_stylist():
    print("Welcome to AI Virtual Stylist!")
    user_input = input("Describe the occasion or outfit you want (e.g., 'formal dinner', 'casual outing'): ")
    location = input("Enter your location for weather adjustment: ")

    recommended = recommend_outfit(user_input)
    outfit_description = recommended["description"]
    print(f"\nRecommended Outfit: {outfit_description}")

    adjusted_outfit = adjust_for_weather(outfit_description, location)
    print(adjusted_outfit)

# Run the stylist
virtual_stylist()
