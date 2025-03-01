# Password Generator Web App

This is a simple web-based password generator built using Django. Users can specify the number of passwords and the length of each password, and the app generates random passwords. The generated passwords can also be copied to the clipboard with a click of a button.

## Features

- User input for the number of passwords and the length of each password.
- Generates random, secure passwords using letters, digits, and special characters.
- Option to copy generated passwords to the clipboard.
- Simple and intuitive web interface.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (for styling)
- **Clipboard functionality**: JavaScript (for copying passwords to the clipboard)

## Project Structure

```bash
password_generator/
 │ ├── manage.py # Django project management script 
 ├── passgen/ # Main Django app 
 │ ├── migrations/ # Django migrations 
 │ ├── templates/ 
 │ │ └── index.html # Main template for password generation form 
 │ ├── static/ 
 │ │ └── passgen/ 
 │ │ └── styles.css # CSS file for styling the app 
 │ ├── views.py # Django views (handles logic) 
 │ ├── urls.py # URL routing for the app 
 │ └── models.py # (Empty) Model file 
 └── README.md # Project documentation
```

## Setup and Installation

To run this project locally, follow these steps:

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Virtual environment (optional but recommended)

### Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/password-generator.git
   cd password-generator
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
        python3 -m venv myenv
        source myenv/bin/activate  # For Linux/Mac
        # On Windows:
        # myenv\Scripts\activate
    ```

3. Install the required packages:

    ```bash
        pip install -r requirements.txt
    ```

If requirements.txt isn't available, you can manually install Django:

```bash
    pip install django
```

4. Run migrations:

```bash
    python manage.py migrate
```

5. Run the Django development server:

```bash
    python manage.py runserver
```

6. Access the web app:

Open your browser and visit `http://127.0.0.1:8000/` to access the password generator.

### Usage

- Open the app in your browser.
- Enter the number of passwords you want to generate and the length of each password.
- Click "Generate Passwords" to display the random passwords.
- Click the "Copy" button next to each password to copy it to the clipboard.

### Screenshots

Image 1: ![Screenshot](https://github.com/eatulrajput/Password_Generator/blob/main/pasgen_web1.png)
Image 2: ![Screenshot](https://github.com/eatulrajput/Password_Generator/blob/main/pasgen_web2.png)

Contribution

If you'd like to contribute to this project:

- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
- Make your changes.
- Commit and push your changes (git commit -am 'Add feature').
- Create a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for more details.
Acknowledgements

- Django Documentation for excellent guides and tutorials.
- Pyperclip for clipboard functionality (if used).

## Note
- password_generator.py is not related to webapp, it can run as a desktop app after execution.
