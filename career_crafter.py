not_allowed_chars = (",", ".", ";", "/", "!", "%", "&")
skill_set = ("attention to detail", "problem solving", "Communication", "Project Management")
programming_skills = ("Java", "Python", "SQL")
while True:
    print()
    user_input1 = input("Please enter your name: ")
    user_input2 = input ("Pleaase enter your surname: ")
    user_cell_number = input("Please enter your cell phone number: ")
    user_location = input("Please enter your location (within radius of miles): ")
    user_skills = input ("What skill sets you are possessed with: ")
    user_programming_skill = input("What programming skills do you have: ")
    invalid_char_counter = 0
    skill = 0
    radius_of_miles = 0
    programming = 0
    if 0 <= radius_of_miles and radius_of_miles <= 60:
        print("You are eligible to apply")
    else:
        print("Vacancies are not available")
    for char in not_allowed_chars:
        if char in user_input1 and user_input2:
            invalid_char_counter += 1           
    if invalid_char_counter > 0:
        print()

        print('INVALID! Name and Surname can not contain ",", ".", ";", "/", "!", "%", "&"')
    else:
        break
    for skill in skill_set:
        if skill in user_skills:
            skill += 1
    if skill > 0:
        print()
        print("You are eligible for this positions")
    else:
        break
 
    for programming in programming_skills:
        if programming in user_programming_skill:
            programming += 1
    if programming > 0:
        print()
        print("You are eligible for this positions in terms of programming skill set")
    else:
        break
print()
print("Applicant name: ", user_input1, user_input2)

if len(user_cell_number) == 11 and user_cell_number.isdigit():
    print("This applicant has a valid cell phone number")

else:
    print("This applicant has an invalid cell phone number")
    


