"""
Harry Bhai Thanks a lot :)
"""

# System Statements(dialogues)
s0 = "!!!Invalid Input!!!"
s1 = "Please Enter The Year You Are In:\n"
s2 = "Please Enter Your Name:\n"
s3 = "Please Enter Your Age:\n"
s4 = "Please Select Your Gender, For Male Press 'M' And For Female Press 'F'\n"
s5 = "Congratulations!!!"
s6 = "you have orbited The SUN"
s7 = "times. You will complete your 100th revolution by the year AD"
s8 = "How Many Times Do You Want This Message To Be Displayed?\n"
s9 = "Your Message Has Been Displayed"
s10 = "times successfully.\nThanks For Using The PROGRAM :)"

while True:
    year = input(s1)
    if year.isnumeric():
        while True:
            user_name = input(s2).upper()
            if user_name.isnumeric():
                print(s0)
            else:
                while True:
                    user_age = input(s3)
                    if user_age.isnumeric():
                        while True:
                            user_gender = input(s4).capitalize()
                            title = ""
                            if user_gender == "M":
                                title = "MR."
                                print(s5, title, user_name, s6, int(user_age), s7, (int(year) + 100 - int(user_age)))
                                while True:
                                    rep = input(s8)
                                    if rep.isnumeric():
                                        i = True
                                        while i <= int(rep):
                                            i += 1
                                            print(s5, title, user_name, s6, int(user_age), s7,
                                                  (int(year) + 100 - int(user_age)))
                                        print(title, user_name, s9, rep, s10)
                                        break
                                    else:
                                        print(s0)
                                break
                            elif user_gender == "F":
                                title = "Ms."
                                print(s5, title, user_name, s6, int(user_age), s7, (int(year) + 100 - int(user_age)))
                                while True:
                                    rep = input(s8)
                                    if rep.isnumeric():
                                        i = True
                                        while i <= int(rep):
                                            i += 1
                                            print(s5, title, user_name, s6, int(user_age), s7,
                                                  (int(year) + 100 - int(user_age)))
                                        print(title, user_name, s9, rep, s10)
                                        break
                                    else:
                                        print(s0)
                                break
                            else:
                                print(s0)
                        break
                    else:
                        print(s0)
                break
        break
    else:
        print(s0)
