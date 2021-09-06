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
            username = input('\nUsername: ')
            try:
                if os.path.isdir('app\\\\accounts\\\\{}'.format(username)) == True:
                    print('\n\tWelcome {} ^_^'.format(username))
                    main()
                else:
                    raise Exception('Error: username is incorrect !')
            except Exception as Error:
                print(Error)
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
    user = int(input('\n( choice ): \t ( To Exit prees 0 ): '))
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
        else:
            raise Exception('Error: Your choice is incorrect !')
    except Exception as Error:
        print(Error)
        main()


start()
