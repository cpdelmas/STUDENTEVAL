# CAHLEIN LOUISE P. DELMAS
# 8 - SAMPAGUITA
# STUDENT PERFORMANCE EVALUATOR

## LOCAL VARIABLES
def display_header():
    print("STUDENT PERFORMANCE EVALUATOR")
    print("======================================")

def display_report():
    print("STUDENT PERFORMANCE REPORT")
    print("=======================================")
    print(f"Student name: {student_name}")
    print(f"Assessment Scores: {score1, score2, score3}")
    print(f"Average Score: {average:.2f}")

display_header()

## GLOBAL VARIABLES
student_name = input("Enter your name: ")
score1 = int(input("Enter your score for assessment 1: "))
score2 = int(input("Enter your score for assessment 2: "))
score3 = int(input("Enter your score for assessment 3: "))

average = (score1 + score2 + score3) / 3

display_report()

if 90 <= average <= 100:
    print("Outstanding!")
elif 90 > average >= 85:
    print("Very Satisfactory!")
elif 80 <= average >= 75:
    print("Satisfactory!")
elif 75 <= average < 80:
    print("Fairly Satisfactory!")
else:
    print("Needs Improvement")



