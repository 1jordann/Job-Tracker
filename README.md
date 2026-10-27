# Python Job Tracker

A command-line application built with Python that allows users to organize, manage, and track their job applications. 
The application uses CSV file storage to save application information and provides a simple menu-driven interface.

## Features
- **Add Applications:** Save company names, application dates, and statuses.
- **View Applications:** Display all saved job applications.
- **Update Status:** Change application statuses to Pending, Accepted, or Denied.
- **Delete Applications:** Remove job applications by company name.
- **Input Validation:** Prevent blank company names and invalid application statuses.
- **CSV Storage:** Store application information between program sessions.
- **Flexible Search:** Match company names regardless of capitalization or surrounding spaces.

## Technologies Used
- Python
- CSV Module
- Datetime Module
- Python unittest Framework
- Git & GitHub

## How to Run

1. Download or clone this repository.
2. Make sure Python 3 is installed.
3. Open a terminal in the project folder.
4. Run the application:

```bash
python job_tracker.py
```

The application will automatically create a `job_applications.csv` file if one does not already exist.

## Automated Testing

The project includes a separate `test_job_tracker.py` file containing eight automated unit tests using Python's built-in `unittest` framework.

The tests cover:
- CSV file initialization
- Adding job applications
- Rejecting blank company names
- Viewing applications
- Updating application statuses
- Rejecting invalid statuses
- Deleting applications
- Preserving existing records

Run the tests using:

```bash
python -m unittest -v test_job_tracker.py
```

The tests use temporary CSV files to avoid modifying real application data.

## What I Learned

Through this project, I gained hands-on experience with Python programming, file handling, input validation, debugging, CRUD operations, and automated software testing.
