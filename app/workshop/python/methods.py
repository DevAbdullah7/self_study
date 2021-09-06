import os
import calendar
import time
from datetime import datetime
calendar.setfirstweekday(calendar.SUNDAY)

# variables
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
    username = input('Enter username: ')
    os.mkdir('app\\\\accounts\\\\{}'.format(username))
    # print('\n\tWelcome {} ^_^'.format(username))
    os.mkdir('app\\\\accounts\\\\{}\\\\courses'.format(username))
    os.mkdir('app\\\\accounts\\\\{}\\\\subjects'.format(username))
    with open('app\\\\accounts\\\\{}\\\\study_plan.txt'.format(username), 'w') as study_plan:
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


def courses():
    print('==================================================')

    def cs50():
        os.system('app\\\\accounts\\\\{}\\\\courses\\\\cs50\\\\main.bat')

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
            os.system('courses\\\\js\\\\\js_course\\\\main.bat')

    def ux():
        print('Google Course: 1')
        print('Satr Course: 2')
        user = int(input('\nchoice : \tTo Exit prees: ( 0 ): '))
        if user == 1:
            os.system('courses\\\\ux_design\\\\main.bat')
        elif user == 2:
            os.system(
                'courses\\\\ux_design\\\\Satr_UIUX_Course\\\\main.bat')
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
