import os
import calendar
import time
from datetime import datetime
# from .. .. import main
calendar.setfirstweekday(calendar.SUNDAY)

# variables
username = ''
time_now = datetime.now()
month_days = calendar.monthrange(time_now.year, time_now.month)[1]
this_week = 0
if time_now.day <= 7:
    this_week = 1
elif 8 <= time_now.day <= 14:
    this_week = 2
elif 15 <= time_now.day <= 21:
    this_week = 3
elif 22 <= time_now.day <= 31:
    this_week = 4


def new_account():
    global username
    username = input('\nEnter Username: ')
    os.mkdir('app\\\\accounts\\\\{}'.format(username))
    os.mkdir('app\\\\accounts\\\\{}\\\\courses'.format(username))
    os.mkdir('app\\\\accounts\\\\{}\\\\subjects'.format(username))
    with open('app\\\\accounts\\\\{}\\\\study_plan.txt'.format(username), 'w') as study_plan:
        study_plan.write('Hello {}.\n\nI\'m glad you are using my script and I hope that it be useful for you .\n\nAfter register and create an account I created all files you may need, now you have to :\n- write the specialization.\n- write all subjects and all courses you want to study it.\n- get course resources to courses folder.\n- get subjects resources to subjects folder.\n\nto see your path ( app/acounts/{} ) ^_^'.format(username, username))
        pass
    os.mkdir('app\\\\accounts\\\\{}\\\\timeline'.format(username))
    os.mkdir('app\\\\accounts\\\\{}\\\\timeline\\\\{}'.format(
        username, time_now.year))
    with open('app\\\\accounts\\\\{}\\\\timeline\\\\{}\\\\Requireds.txt'.format(
            username, time_now.year), 'w') as Requireds:
        pass
    with open('app\\\\accounts\\\\{}\\\\timeline\\\\{}\\\\Report.txt'.format(
            username, time_now.year), 'w') as Report:
        pass
    for i in range(1, 12+1):
        os.mkdir('app\\\\accounts\\\\{}\\\\timeline\\\\{}\\\\{}'.format(
            username, time_now.year, i))
        for x in range(1, 4+1):
            os.mkdir('app\\\\accounts\\\\{}\\\\timeline\\\\{}\\\\{}\\\\{}'.format(
                username, time_now.year, i, x))
            with open('app\\\\accounts\\\\{}\\\\timeline\\\\{}\\\\{}\\\\{}\\\\Requireds.txt'.format(
                    username, time_now.year, i, x), 'w') as Requireds:
                pass
            with open('app\\\\accounts\\\\{}\\\\timeline\\\\{}\\\\{}\\\\{}\\\\Report.txt'.format(
                    username, time_now.year, i, x), 'w') as Report:
                pass
            with open('app\\\\accounts\\\\{}\\\\timeline\\\\{}\\\\{}\\\\{}\\\\schedule.txt'.format(
                    username, time_now.year, i, x), 'w') as schedule:
                pass
        for z in range(1, calendar.monthrange(time_now.year, i)[1]+1):
            if z <= 7:
                os.mkdir('app\\\\accounts\\\\{}\\\\timeline\\\\{}\\\\{}\\\\1\\\\{}'.format(
                    username, time_now.year, i, z))
                with open('app\\\\accounts\\\\{}\\\\timeline\\\\{}\\\\{}\\\\1\\\\{}\\\\Requireds.txt'.format(
                        username, time_now.year, i, z), 'w') as Requireds:
                    pass
                with open('app\\\\accounts\\\\{}\\\\timeline\\\\{}\\\\{}\\\\1\\\\{}\\\\Report.txt'.format(
                        username, time_now.year, i, z), 'w') as Report:
                    pass
            elif 8 <= z <= 14:
                os.mkdir('app\\\\accounts\\\\{}\\\\timeline\\\\{}\\\\{}\\\\2\\\\{}'.format(
                    username, time_now.year, i, z))
                with open('app\\\\accounts\\\\{}\\\\timeline\\\\{}\\\\{}\\\\2\\\\{}\\\\Requireds.txt'.format(
                        username, time_now.year, i, z), 'w') as Requireds:
                    pass
                with open('app\\\\accounts\\\\{}\\\\timeline\\\\{}\\\\{}\\\\2\\\\{}\\\\Report.txt'.format(
                        username, time_now.year, i, z), 'w') as Report:
                    pass
            elif 15 <= z <= 21:
                os.mkdir('app\\\\accounts\\\\{}\\\\timeline\\\\{}\\\\{}\\\\3\\\\{}'.format(
                    username, time_now.year, i, z))
                with open('app\\\\accounts\\\\{}\\\\timeline\\\\{}\\\\{}\\\\3\\\\{}\\\\Requireds.txt'.format(
                        username, time_now.year, i, z), 'w') as Requireds:
                    pass
                with open('app\\\\accounts\\\\{}\\\\timeline\\\\{}\\\\{}\\\\3\\\\{}\\\\Report.txt'.format(
                        username, time_now.year, i, z), 'w') as Report:
                    pass
            elif 22 <= z <= 31:
                os.mkdir('app\\\\accounts\\\\{}\\\\timeline\\\\{}\\\\{}\\\\4\\\\{}'.format(
                    username, time_now.year, i, z))
                with open('app\\\\accounts\\\\{}\\\\timeline\\\\{}\\\\{}\\\\4\\\\{}\\\\Requireds.txt'.format(
                        username, time_now.year, i, z), 'w') as Requireds:
                    pass
                with open('app\\\\accounts\\\\{}\\\\timeline\\\\{}\\\\{}\\\\4\\\\{}\\\\Report.txt'.format(
                        username, time_now.year, i, z), 'w') as Report:
                    pass
    os.system('app\\\\accounts\\\\{}\\\\study_plan.txt'.format(username))
    print('\nRegister successful ^_^')


def exist_account():
    global username
    username = input('username: ')
    try:
        if os.path.isdir('app\\\\accounts\\\\{}'.format(username)) == True:
            print('\n\tWelcome {} ^_^'.format(username))
            return True
        else:
            raise Exception('Error: username is incorrect !')
    except Exception as Error:
        print(Error)


def courses():
    print('==================================================')

    def cs50():
        os.system(
            'app\\\\accounts\\\\{}\\\\courses\\\\cs50\\\\main.bat'.format(username))

    def python():
        pass

    def html():
        pass

    def css():
        pass

    def js():
        print('\nJavaScript course: 1')
        print('Jquery course: 2')
        print('ReactJs course: 3')
        user = int(input('\nchoice : \tTo Exit prees: ( 0 ): '))
        if user == 1:
            os.system(
                'app\\\\accounts\\\\{}\\\\courses\\\\js\\\\\js_course\\\\main.bat'.format(username))

    def ux():
        print('Google Course: 1')
        print('Satr Course: 2')
        user = int(input('\nchoice : \tTo Exit prees: ( 0 ): '))
        if user == 1:
            os.system(
                'app\\\\accounts\\\\{}\\\\courses\\\\ux_design\\\\main.bat'.format(username))
        elif user == 2:
            os.system(
                'app\\\\accounts\\\\{}\\\\courses\\\\ux_design\\\\Satr_UIUX_Course\\\\main.bat'.format(username))
        elif user == 0:
            pass
        else:
            raise Exception('Error: Your choice is incorrect !')
            ux()
    print('\nCS50 course: 1')
    print('Python course: 2')
    print('Html course: 3')
    print('Css course: 4')
    print('JavaScript course: 5')
    print('UX Design course: 6')
    user = int(input('\nchoice : \tTo Exit prees: ( 0 ): '))
    if user == 1:
        print('==================================================')
        cs50()
    elif user == 2:
        print('==================================================')
        python()
    elif user == 3:
        print('==================================================')
        html()
    elif user == 4:
        print('==================================================')
        css()
    elif user == 5:
        print('==================================================')
        js()
    elif user == 6:
        print('==================================================')
        ux()


def Requireds():
    print('==================================================')
    print('\nYearly Requirements: 1')
    print('Monthly Requirements: 2')
    print('Weekly Requirements: 3')
    print('Daily Requirements: 4')
    klint = int(input('\nchoice : \tTo Exit prees: ( 0 ): '))
    try:
        if klint == 1:
            os.system(
                'timeline\\\\{}\\\\Requirements.txt'.format(time_now.year))
        elif klint == 2:
            os.system('timeline\\\\{}\\\\{}\\\\Requirements.txt'.format(
                time_now.year, time_now.month))
        elif klint == 3:
            os.system('timeline\\\\{}\\\\{}\\\\{}\\\\Requirements.txt'.format(
                time_now.year, time_now.month, this_week))
        elif klint == 4:
            os.system('timeline\\\\{}\\\\{}\\\\{}\\\\{}\\\\Requirements.txt'.format(
                time_now.year, time_now.month, this_week, time_now.day))
        elif klint == 0:
            pass
        else:
            raise Exception('Error: Your choice is incorrect !')
    except Exception as Error:
        print(Error)
        time.sleep(2)
        Requireds()


def Attendees():
    pass


def Reports():
    pass


def Timeline():
    pass
