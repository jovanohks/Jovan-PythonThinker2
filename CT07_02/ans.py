score = 0
max_attempts = 3

# Questions and their correct answers using 1D list alternating between question and answer
questions_answers = [
    "What is the capital of France?", "Paris",
    "How many continents are there?", "7",
    "What planet is known as the Red Planet?", "Mars"
]

# Iterating through the questions and answers
for i in range(0, len(questions_answers), 2):  # Increment by 2 to get question and then answer
    question = questions_answers[i]
    correct_answer = questions_answers[i + 1]
    attempts = 0

    while attempts < max_attempts:
        # Ask the user the question
        user_input = input(question)

        if user_input.lower() == correct_answer.lower():
            print(f"Correct! The answer is {correct_answer}.")
            score += 1  # Increment score for correct answer
            break  # Move on to the next question
        elif user_input.lower() == "skip":
            print("Question skipped.")
            break  # Skip the question
        else:
            print("That's not correct, try again.")
            attempts += 1  # Increment attempts

        if attempts == max_attempts:
            print("Too many incorrect attempts, moving to next question.")

# Print the final score
print(f"Your final score is {score} out of {len(questions_answers) // 2}.")