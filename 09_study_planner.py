import datetime
def plan_study():

    today = datetime.date.today()
    exam_str = input("Enter exam date in (YYYY-MM-DD):")
    exam_date = datetime.datetime.strptime(exam_str,"%Y-%m-%d").date()
    days_left = (exam_date - today).days
    print(f"Today is {today}")
    print(f"The exam date is {exam_date}")
    print(f"You have {days_left} for the Exam!!")

    subjects = []
    
    while True:
        sub = input("Enter the name of the subject or q to quit:")
        if sub == "q":
            break
        diff = int(input("Enter the subjects difficulty from(1-5):"))
        sub_dict = {"sub" : sub , "difficulty" : diff}
        subjects.append(sub_dict)
    print("Subjects Added!!", subjects)
    total_diff = 0
    for sub in subjects:
        total_diff = total_diff + sub["difficulty"]
    print(f"total difficulty points = {total_diff}")
    print("Your Study Plan")
    for sub in subjects:
        days = round((sub["difficulty"] / total_diff)*  days_left)
        print(f"Study {sub['sub']} because only {days} days left")
plan_study()



