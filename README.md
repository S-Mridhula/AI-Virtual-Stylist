AI Virtual Stylist

An intelligent virtual assistant that provides personalized outfit recommendations based on user preferences, weather conditions, and fashion trends. This project uses AI and weather integration to make styling easier and more effective.


Features
- 📋 Personalized Recommendations: Suggests outfits based on user input (occasion, style preferences, etc.).
- 🌦️ Weather Integration: Adjusts suggestions based on current weather conditions using OpenWeatherMap API.
- 🧠 AI-Powered Matching: Utilizes TF-IDF and cosine similarity for intelligent outfit selection.
- 💡 Scalable: Easily extendable to include more outfits and advanced recommendation logic.

How It Works
1. User Input: The user provides details such as the occasion or preferred style (e.g., "formal dinner", "casual outing").
2. AI Analysis: The system analyzes the input and matches it with the most relevant outfit in the database using text similarity.
3. Weather Adjustment: Weather data is fetched using OpenWeatherMap API, and suggestions are refined based on temperature and conditions.
4. Output: The recommended outfit, along with weather-based suggestions, is displayed.

Technologies Used
- Python: Core programming language.
- scikit-learn: For TF-IDF vectorization and cosine similarity.
- Requests: For fetching weather data from the OpenWeatherMap API.
- OpenWeatherMap API: For real-time weather data.

Setup and Installation

Prerequisites
- Python 3.6 or higher
- Required Python libraries:
  - `scikit-learn`
  - `requests`

Steps to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/S-Mridhula/AI-Virtual-Stylist.git
   ```
2. Navigate to the project folder:
   ```bash
   cd AI-Virtual-Stylist
   ```
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Replace `YOUR_API_KEY` in the code with your OpenWeatherMap API key.
5. Run the project:
   ```bash
   python virtual_stylist.py
   ```
Example Output
- Input: "Casual outing", Location: "New York"
- Output:
  ```
  Recommended Outfit: Casual jeans and white t-shirt, great for outings.
  Suggestion: Light clothing should be fine.
  ```



Future Enhancements
- 🔄 Integrate real-time fashion trends from external APIs.
- 🎨 Add a graphical user interface (GUI) for better user interaction.
- 🤖 Use advanced machine learning models for recommendation.
- 🌍 Multi-language support.



Contributing
Contributions are welcome! If you'd like to improve this project, follow these steps:
1. Fork the repository.
2. Create a new branch:
   bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   bash
   git commit -m "Added new feature"
   
4. Push to the branch:
   bash
   git push origin feature-name
   
5. Create a pull request.

Acknowledgments
- [OpenWeatherMap](https://openweathermap.org/) for the weather API.
- The developers of `scikit-learn` for providing excellent tools for text processing.


