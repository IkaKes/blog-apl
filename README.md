# Simple Blog Application

## Introduction
This is a simple blog application built with Flask for the backend and vanilla HTML, CSS, and JavaScript for the frontend.

## Setup
### Backend
1. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
2. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the application:
    ```sh
    python app.py
    ```

### Frontend
The frontend is served by Flask and is located in the `frontend` directory.

## API Endpoints
### Get all posts
- **URL:** `/api/posts`
- **Method:** `GET`
- **Response:**
    ```json
    [
        {
            "id": 1,
            "title": "Post Title",
            "content": "Post content"
        },
        ...
    ]
    ```

### Add a new post
- **URL:** `/api/posts`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "title": "Post Title",
        "content": "Post content"
    }
    ```
- **Response:**
    ```json
    {
        "id": 1,
        "title": "Post Title",
        "content": "Post content"
    }
    ```

### Update a post
- **URL:** `/api/posts/<post_id>`
- **Method:** `PUT`
- **Request Body:**
    ```json
    {
        "title": "Updated Title",
        "content": "Updated content"
    }
    ```
- **Response:**
    ```json
    {
        "id": 1,
        "title": "Updated Title",
        "content": "Updated content"
    }
    ```

### Delete a post
- **URL:** `/api/posts/<post_id>`
- **Method:** `DELETE`
