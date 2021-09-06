from app.workshop.python import methods
import os


def start():
    print('==================================================')
    print('\n\t{} {}/{}/{}\n'.format(methods.time_now.strftime('%A'),
                                     methods.time_now.day, methods.time_now.month, methods.time_now.year))
    print('For Exist Account: 1')
    print('For New Account: 2')
    user = int(input('\n( choice ): \t ( To Exit prees 0 ): '))
    try:
        if user == 1:
            print('==================================================')
            # methods.exist_account()
            exist_account = methods.exist_account()
            if exist_account == True:
                main()
            else:
                start()
        elif user == 2:
            print('==================================================')
            methods.new_account()
            main()
        elif user == 0:
            pass
        else:
            raise Exception('Error: your choice is incorrect !')
    except Exception as Error:
        print(Error)
        start()


def main():
    print('==================================================')
    print('\nFor Courses: 1')
    print('For Requireds: 2')
    print('For Reports: 3')
    print('For Timeline: 4')
    user = int(input('\n( choice ): \t ( To Exit: 0 OR To Logout: 9 ): '))
    try:
        if user == 1:
            methods.courses()
            main()
        elif user == 2:
            methods.Requireds()
            main()
        elif user == 3:
            methods.Reports()
        elif user == 4:
            methods.Timeline()
        elif user == 0:
            pass
        elif user == 9:
            start()
        else:
            raise Exception('Error: Your choice is incorrect !')
    except Exception as Error:
        print(Error)
        main()


start()
