# Speechrecognition-Text-to-speech.

Voice Assistant Program

A simple voice assistant program that uses speech recognition and text-to-speech capabilities to perform various tasks.

Features

- Retrieves the price of an inventory item from a database
- Reads news articles from text files (sports, movies, politics, headlines)
- Uses speech recognition to understand voice commands
- Provides text-to-speech feedback for user interactions
- Supports multiple voice commands for different tasks

Requirements

- Python 3.x
- SpeechRecognition library
- pyttsx3 library
- PyMySQL library (for database connectivity)
- MySQL database (for inventory management)

Technical Details

- The program uses the SpeechRecognition library to recognize user voice commands.
- The pyttsx3 library is used to provide text-to-speech feedback.
- The PyMySQL library is used to connect to the MySQL database for inventory management.
- The program uses a simple text-based interface to interact with the user.

Usage

1. Install the required libraries using pip: pip install SpeechRecognition pyttsx3 PyMySQL
2. Create a MySQL database and add the necessary tables and data
3. Update the database connection settings in the program code
4. Run the program using Python: python (link unavailable)
5. Use voice commands to interact with the program (e.g., "price", "sports", "movies", etc.)

Contributing

Contributions are welcome! If you'd like to improve the program or add new features, please fork the repository and submit a pull request.

Future Development

- Integrate with other APIs for more features (e.g., weather, calendar, etc.)
- Improve speech recognition accuracy
- Add support for multiple languages
- Develop a user-friendly interface for configuring settings and customizing the program
