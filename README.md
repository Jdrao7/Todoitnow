# Todoitnow 📝

**Todoitnow** is a simple and efficient To-Do list web application built with Python using the Flask framework. It provides a clean and minimal interface for managing your daily tasks, powered by a lightweight SQLite database for persistent storage.

This project is a practical demonstration of the fundamentals of web development with Flask and showcases how to implement basic **CRUD** (Create, Read, Update, Delete) functionality in a real-world application.

## ✨ Features

-   **Create Tasks**: Quickly add new tasks to your list.
-   **View All Tasks**: See all your pending tasks in an organized list.
-   **Update Tasks**: Mark tasks as complete to track your progress.
-   **Delete Tasks**: Remove tasks that are no longer needed.
-   **Persistent Storage**: Your tasks are saved in a local SQLite database, so they're there when you come back.

## ⚙️ Technology Stack

-   **Backend**: Python, Flask
-   **Database**: SQLite3
-   **Frontend**: HTML & CSS (with Jinja2 for templating)

## 🚀 Getting Started

### Prerequisites

-   Python 3.x
-   `pip` (Python package installer)

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/Jdrao7/Todoitnow.git](https://github.com/Jdrao7/Todoitnow.git)
    cd Todoitnow
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Run the Flask application:**
    ```sh
    flask run
    ```
    The application will be running and accessible at `http://127.0.0.1:5000` in your web browser. The SQLite database file (`todo.db`) will be created automatically in the project directory upon first run.

## 📖 What You Can Learn

This project is an excellent resource for learning:
-   How to structure a basic Flask application.
-   Defining routes and handling requests.
-   Performing CRUD operations with an SQL database.
-   Rendering dynamic data in HTML templates using the Jinja2 templating engine.
