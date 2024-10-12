import random
import time
import csv

class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, user_answer):
        return user_answer.lower() == self.correct_option.lower()
    
    @classmethod
    def from_csv(cls, csv_row):
        # csv_row is a list containing [text, option1, option2, ..., correct_option]
        text = csv_row[0]
        options = csv_row[1:-1]
        correct_option = csv_row[-1]
        return cls(text, options, correct_option)

class Test:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def conduct_test(self):
        random.shuffle(self.questions)  # Shuffle questions for a random order
        start_time = time.time()

        for i, question in enumerate(self.questions, start=1):
            print(f"\nQuestion {i}/{len(self.questions)}: {question.text}")
            for j, option in enumerate(question.options, start=1):
                print(f"{j}. {option}")

            user_answer = input("Your answer (enter the option number): ")
            print(f"You entered: {user_answer}, Correct Answer: {question.correct_option}")
            if question.is_correct(user_answer):
                self.score += 1
                print("Correct!")
            else:
                print(f"Wrong! The correct answer is: {question.correct_option}")


        end_time = time.time()
        total_time = end_time - start_time
        print(f"\nYour final score is: {self.score}/{len(self.questions)}")
        print(f"Total time taken: {total_time:.2f} seconds")
        print("Thanks for taking the test!")

        # Save test results
        user_name = input("Enter your name: ")
        self.save_test_results(user_name, self.score, len(self.questions), total_time)

    def get_final_score(self):
        return self.score

    def save_test_results(self, user_name, final_score, total_questions, total_time):
        with open('test_results.csv', 'a', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([user_name, final_score, total_questions, total_time])


def read_questions_from_csv(file_path):
    questions = []
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            question = Question.from_csv(row)
            questions.append(question)
    return questions

# Example usage:
csv_file_path = 'questions.csv'
questions_from_csv = read_questions_from_csv(csv_file_path)
user_test = Test(questions_from_csv)

# Conduct the test and save results
user_test.conduct_test()
final_score = user_test.get_final_score()
print(f"\nFinal Score: {final_score}/{len(questions_from_csv)}")
