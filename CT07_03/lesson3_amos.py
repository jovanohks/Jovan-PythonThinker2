lives = 3
for qn_num in range(1, 16):
    if lives == 0:
        break
    num1, num2 = random.randint(2, 20), random.randint(2, 20)
    res = int(input(f"Q{qn_num}. What is {num1} x {num2}? "))
    while res != num1 * num2:
        lives -= 1
        if lives == 0:
            print("WRONG AGAIN! GO AND SEE MS TAN FOR REMEDIAL")
            break
        print(f"Wrong. Try again. You have {lives} live(s) left.")
        res = int(input(f"Q{qn_num}. What is {num1} x {num2}? "))
    else:
        print("Correct!")
else:
    print(f"Congratulations! You don't need remedial!")