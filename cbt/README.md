# Exam Testing System

## Introduction

This Python script is an Exam Testing System that allows users to take a test based on a set of questions provided in a CSV file. The system shuffles the questions, presents them to the user, and records their score.

## Features

- Randomized Questions: The system shuffles the questions for a random order in each test session.
- User-Friendly Interface: Clear and simple console-based interface for users to answer questions.
- Scoring: Calculates and displays the user's final score at the end of the test.
- Time Tracking: Measures the time taken by the user to complete the test.

## Getting Started

### Clone the Repository:

```bash
git clone https://github.com/sbendavid/CBT.git
cd exam-testing-system
```

### Install Dependencies:
Ensure you have Python installed. Run the following command to install the required packages:

```bash
pip install -r requirements.txt
```

### Prepare Questions:
Create a CSV file (questions.csv) with the questions and answer options. Each row should have the question text, options, and the correct option.

Example:

 - What is the capital of France?,Paris,London,Berlin,Paris
 - Which programming language is this test written in?,Java,Python,C++,Python
 - What is the square root of 64?,6,8,10,8

### Run the Test:
Execute the script to conduct a test:

```bash
python main.py
```

### Review Results:
After completing the test, the script will display the user's final score and time taken. Test results are also saved to test_results.csv.

## Customization

### Question Structure:
Ensure the CSV file follows the structure expected by the script. Each row represents a question with the question text, options, and the correct option.

### File Paths:
Adjust file paths and names in the script to match your project structure and preferences.

## Contributing
Feel free to contribute by opening issues or submitting pull requests. Your feedback and contributions are welcome!

## License
This project is licensed under the MIT License - see the LICENSE file for details.