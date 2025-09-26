<!-- DO NOT REMOVE - contributor_list:data:start:["MuhammadSaadSiddique", "YousraMashkoor"]:end -->

# QScience

QScience is a pioneering website dedicated to closing the gap between modern science and the Quran. Our mission is to identify and analyze various patterns found within the Quran, making them easily accessible by harnessing the power of AI. Our platform continually expands its knowledge base, uncovering new patterns and connections that may have been previously overlooked.

## Features

*   **Quranic Analysis:** Explore the Quran with a scientific lens.
*   **Pattern Recognition:** Discover hidden patterns and connections in the text.
*   **AI-Powered:** Our platform uses AI to expand its knowledge base.
*   **Community-Driven:** Join our community of researchers and enthusiasts.

## Project Structure

The repository is a monorepo containing both the frontend and backend code.

```
.
├── backend/         # Flask backend application
│   ├── app/
│   │   ├── models/  # SQLAlchemy database models
│   │   └── views/   # Flask-RESTful API resources
│   └── migrations/  # Database migration scripts
├── fastapi_backend/ # FastAPI backend application
├── frontend/        # React frontend application
│   └── src/
│       ├── components/ # Reusable React components
│       └── routes/     # Page components
└── Databasedesign.md  # Details on the database schema
```

## Setup your Environment

### Flask Backend

1.  Navigate to the `backend` folder.
2.  Create a virtual environment: `python3 -m venv venv`
3.  Activate the virtual environment: `source venv/bin/activate`
4.  Install the required packages: `pip install -r requirements.txt`

### Setting DB Credentials

1.  Create a `.env` file in the `backend` directory.
2.  Add the following environment variables to the `.env` file:

    ```
    export DB_USER=your-user-name
    export DB_PASSWORD=your-pwd
    export DB_HOST=localhost
    export DB_NAME=quranicsci-db
    ```

### Run the Flask server

1.  Navigate to the `backend` folder.
2.  Run the server: `python manage.py runserver`

### FastAPI Backend

1.  Navigate to the `fastapi_backend` folder.
2.  Create a virtual environment: `python3 -m venv venv`
3.  Activate the virtual environment: `source venv/bin/activate`
4.  Install the required packages: `pip install -r requirements.txt`
5.  Run the server: `uvicorn main:app --reload`

### Frontend

1.  Navigate to the `frontend` folder.
2.  Install the required packages: `npm install`
3.  Start the development server: `npm start`

## Contributing

Contributions are welcome! If you have a suggestion or want to report a bug, please open an issue to discuss it.

To contribute code:
1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with a clear message.
4.  Push your branch to your fork.
5.  Create a pull request to the main repository.

Please try to follow the existing coding style.

# [Join Discord server for discussion](https://discord.gg/kWJjnFW3eK)

<!-- prettier-ignore-start -->
<!-- DO NOT REMOVE - contributor_list:start -->
### 👥 Contributors


- **[@MuhammadSaadSiddique](https://github.com/MuhammadSaadSiddique)** (3 contributions)

- **[@YousraMashkoor](https://github.com/YousraMashkoor)** (1 contribution)

<!-- DO NOT REMOVE - contributor_list:end -->
<!-- prettier-ignore-end -->