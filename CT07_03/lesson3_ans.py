# Initialize the total questions and lives
total_questions = 15
lives = 3

for q_num in range(total_questions):
    # Generate random numbers for the question
    num1 = randint(2, 20)
    num2 = randint(2, 20)
    correct_answer = num1 * num2

    # Ask the question
    while lives > 0:
        # Ask the user the question
        answer = int(input(f"Q{q_num} What is {num1} x {num2}? "))

        if answer == correct_answer:
            print(f"Correct! {num1} x {num2} = {correct_answer}")
            break  # Move on to the next question
        else:
            lives -= 1  # Deduct a life for incorrect answer
            print(f"Wrong! Try again. You have {lives} lives left.")

        if lives == 0:
            print("GO AND SEE MS TAN FOR REMEDIAL")
            break

    if lives == 0:
        break  # Exit the quiz if no more lives are left

# If the loop is completed successfully, it means the user answered all questions correctly
if lives > 0:
    print("Congratulations! You have completed the quiz.")