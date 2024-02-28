# Borrowings Service

This is one of the service that implemented for learning twelve-factor-app-framework.

## Borrowing Service Endpoints and Database Schema

Building upon our previous discussions about the library management system, here's a detailed outline of the borrowing service endpoints and database schema:

**Endpoints:**

**1. Borrowing Management:**

- **POST /borrowings:** Creates a new borrowing record.

  - **Request Body:**
    - `user_id`: Unique identifier of the user borrowing the book (required).
    - `book_id`: Unique identifier of the book being borrowed (required).
    - `borrowed_at`: Timestamp of borrowing (optional, defaults to current time).
    - `expected_return_at`: Timestamp of expected return (optional).
  - **Response:**
    - `201 Created`: Borrowing record created successfully, returns the newly created borrowing object.
    - `400 Bad Request`: Invalid or missing required fields in the request body.
    - `404 Not Found`: User or book not found.
    - `409 Conflict`: Book is already borrowed by another user (consider returning a more informative error message).

- **GET /borrowings/{borrowing_id}:** Retrieves a specific borrowing record.

  - **Path Parameter:**
    - `borrowing_id`: Unique identifier of the borrowing record (required).
  - **Response:**
    - `200 OK`: Borrowing record found, returns the borrowing object.
    - `404 Not Found`: Borrowing record with the specified ID not found.

- **PUT /borrowings/{borrowing_id}:** Updates an existing borrowing record (e.g., extend due date).

  - **Path Parameter:**
    - `borrowing_id`: Unique identifier of the borrowing record (required).
  - **Request Body:**
    - Any fields that need to be updated (optional, e.g., `expected_return_at`).
  - **Response:**
    - `200 OK`: Borrowing record updated successfully, returns the updated borrowing object.
    - `400 Bad Request`: Invalid or missing fields in the request body.
    - `404 Not Found`: Borrowing record with the specified ID not found.

- **DELETE /borrowings/{borrowing_id}:** Returns a borrowed book.
  - **Path Parameter:**
    - `borrowing_id`: Unique identifier of the borrowing record (required).
  - **Response:**
    - `200 OK`: Book returned successfully.
    - `404 Not Found`: Borrowing record with the specified ID not found.
    - `409 Conflict`: Book cannot be returned due to outstanding fees (consider returning a more informative error message).

**2. User Borrowing History:**

- **GET /users/{user_id}/borrowings:** Retrieves a user's borrowing history.
  - **Path Parameter:**
    - `user_id`: Unique identifier of the user (required).
  - **Response:**
    - `200 OK`: Borrowing history retrieved successfully, returns a list of borrowing objects or relevant information.
    - `404 Not Found`: User with the specified ID not found.

**3. Book Availability:**

- **GET /books/{book_id}/availability:** Checks the availability of a book.
  - **Path Parameter:**
    - `book_id`: Unique identifier of the book (required).
  - **Response:**
    - `200 OK`: Book information and availability status (available, borrowed, etc.).
    - `404 Not Found`: Book with the specified ID not found.

**Database Schema:**

**1. Borrowings Table:**

| Column Name        | Data Type | Description                                              |
| ------------------ | --------- | -------------------------------------------------------- |
| id                 | INT       | Unique identifier for the borrowing record (primary key) |
| user_id            | INT       | Foreign key referencing the `Users` table (required)     |
| book_id            | INT       | Foreign key referencing the `Books` table (required)     |
| borrowed_at        | DATETIME  | Timestamp of borrowing (default: current time)           |
| expected_return_at | DATETIME  | Timestamp of expected return (optional)                  |
| returned_at        | DATETIME  | Timestamp of book return (null initially)                |
| late_fees          | INT       | Late fees of the book                                    |

**2. Additional Considerations:**

- You might want to include additional columns like `late_fees` to track and manage fees associated with overdue returns.
- Implement relationships between tables using foreign keys to ensure data integrity.
- Consider implementing background processes or triggers to handle overdue book notifications and automated fee calculations.
