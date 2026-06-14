# Quiz

### Project Overview

A simple quiz generator website, which allows users to create their own quizes and practice them.
<img width="1552" height="906" alt="image" src="https://github.com/user-attachments/assets/ea5d62b6-a9d8-4ac7-bc16-3530aa79ecab" />
<img width="1552" height="906" alt="image" src="https://github.com/user-attachments/assets/f7a370eb-3d62-4c21-9250-1f4733c8f060" />

Live score count is shown next to the quiz. 
<img width="1552" height="906" alt="image" src="https://github.com/user-attachments/assets/689e3975-3420-4012-947c-262fb62e485f" />

Since the quizes are stored in a database, users can enjoy doing there quizes any time after generating them once.

### Tech Stack
- Back End: Python
- Front End: HTML, CSS, JS
- Databse: SQLite3

### Project Structure
- `app.py`: Main Python file that contains all the routes and back end logic
- `helper.py`: Hold functions to initialize the database
- `reauirements.txt`: Contains the python libraries used in making the app
- `static`
    - `script.js`: Contains all the front end logic
    - `styles.css`: Contains all the styling
- `templates`
    - `layout.html`: Contains the boilerplate html file
    - `index.html`: Contains all the home page elements
    - `generate-pg-1.html`: Contains the quiz details elements
    - `generate-pg-2.html`: Contains all the questions and answer elements
    - `quiz.html`: Contains quiz page elements


### Getting Started
#### Prerequisites
- Make sure you have python and sqlite3 installed by running,
```
python --version
sqlite3 --version
```

#### Installation
- Clone the repository into your machine and move into the folder
```
git clone https://github.com/ChamalInd/Quiz.git
cd Sudoku
```
- Then install all the requirements
```
pip install -r requirements.txt
```

#### Running the app
- Start the Flask app by running
```
flask run
```


