# chore_wars

Find it at: https://chore-wars.onrender.com

Our application uses a gamified approach to managing household chores. Users can register, log in, and complete tasks to earn points. A leaderboard displays the top users based on their accumulated points.

The system consist of a backend built with Python and a frontend using HTML templates.

Database is mysql and it's hosted by Aiven. The required credentials are stored in **.env file.** Please email a project member to get access to the **.env** file.

# To run the application
(venv is recommended)
1. pip install -r requirements.txt
2. Set up the **.env** file with the required database credentials.
3. Run the backend server: `python backend/app.py`
4. Access the frontend by going to localhost:5000. It will redirect to login page
5. Register a new user and start completing tasks!

# Project Structure
- backend/: Contains the backend code including database configuration, CRUD operations, and API endpoints.
- frontend/: Contains HTML templates for user interfaces such as registration, login, task viewing, and
    leaderboard display.
