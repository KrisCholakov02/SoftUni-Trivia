# Trivia

Trivia is a web-based trivia game application developed as a final project for a Django course exam at SoftUni (2019). The application offers an engaging platform for users to test and expand their general knowledge while enjoying a fun and challenging game experience.

## Purpose

The primary goal of Trivia is to provide a digital environment where users can:
- **Challenge themselves:** Answer questions of varying difficulty levels to test their knowledge.
- **Learn and grow:** Enhance their general culture and learn new facts in a playful setting.
- **Relax and enjoy:** Unwind after a busy day with an entertaining game that combines education and leisure.

## Features

- **User Accounts:**  
  Secure registration, login, and profile management, including the ability to edit personal information.

- **Dynamic Gameplay:**  
  - Start new games and progress through rounds of questions.
  - Use in-game aids such as fifty-fifty, right answer, and answer removal options to help during gameplay.
  - Restart the game (administrator-only feature) to manage game sessions.

- **Question Management:**  
  Create, edit, and delete trivia questions with proper access control to ensure only authorized users make modifications.

- **Game History:**  
  Record and display game sessions, allowing users to view their performance history.

- **Consistent UI/UX:**  
  Shared templates and a common CSS framework ensure a unified look and navigation across the application.

## Project Structure

The application is divided into several modular Django apps, each responsible for specific functionalities:

- **Accounts:**  
  Handles user authentication, profile creation, and profile editing.

- **Game:**  
  Contains the core logic and tactics for managing the trivia game, including functions for starting, progressing through, and restarting games.

- **Games:**  
  Manages the recording of completed games and displays a history of games played by each user.

- **Questions:**  
  Facilitates the creation, update, and deletion of trivia questions, ensuring that only authorized users can modify content.

- **Common:**  
  Provides shared resources such as base templates, CSS, and the navigation bar that ties the application together.

## Installation & Setup

*Note: For detailed installation instructions, please refer to the project documentation.*

1. **Clone the Repository:**
   ```bash
   git clone https://your-repository-url.git
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure Settings:**
   Update the Django settings with your database configurations and other environment-specific settings.
4. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Run the Server:**
   ```bash
   python manage.py runserver
   ```
6. **Access the Application:**
   Open your web browser and navigate to `http://127.0.0.1:8000/` to start playing Trivia.

## Future Enhancements

The project is actively evolving with planned improvements, including:
- **Group Play Mode:**  
  Introducing a new game mode that allows multiple players to compete in groups.
- **Enhanced UI/UX:**  
  Continuous refinement of the user interface based on user feedback.
- **Additional Game Mechanics:**  
  Further development of in-game features to enhance the overall gaming experience.

## Documentation

For a more detailed overview of the project's structure and implementation, refer to the official documentation:  
[Project Documentation](https://drive.google.com/drive/folders/1Yzf1batvcAsdExkMGkElrIKno5U6IzTq?usp=sharing)
