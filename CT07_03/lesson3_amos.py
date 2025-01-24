# lives = 3
# for qn_num in range(1, 16):
#     if lives == 0:
#         break
#     num1, num2 = random.randint(2, 20), random.randint(2, 20)
#     res = int(input(f"Q{qn_num}. What is {num1} x {num2}? "))
#     while res != num1 * num2:
#         lives -= 1
#         if lives == 0:
#             print("WRONG AGAIN! GO AND SEE MS TAN FOR REMEDIAL")
#             break
#         print(f"Wrong. Try again. You have {lives} live(s) left.")
#         res = int(input(f"Q{qn_num}. What is {num1} x {num2}? "))
#     else:
#         print("Correct!")
# else:
#     print(f"Congratulations! You don't need remedial!")


start_time = time.time()
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
    time_taken = time.time() - start_time
    mins_taken = math.floor(time_taken / 60)
    secs_taken = round(time_taken - mins_taken * 60, 2)
    if mins_taken >= 1:
        print(f"Congratulations! You finished the quiz in {mins_taken} minute(s) and {secs_taken} seconds.")
    else:
        print(f"Congratulations! You finished the quiz in {secs_taken} seconds")
        