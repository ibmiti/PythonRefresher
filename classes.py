class Human :
    
    def Sneeze(self):
        print('AHHHH-CHOOOO')    

my_friend = Human()
my_friend.Sneeze()

# Giving Human class attributes
my_friend.current_first_name = ''
my_friend.current_last_name = ''

# Allow Human to change name of friend
if my_friend.current_first_name == '' :
    question1 = input('Would you like to change the name of your friend? ')
    if question1.lower() == 'yes' :
        print('Changing name of friend...')
        print('.......')
        are_you_sure = input('Almost Done would you like to keep the name same?:')
        if are_you_sure.lower() == 'no' :
            new_name_first_name = my_friend.fist_name = input("What would you like for the first name to be?")
            print(f'Great {new_name_first_name} will be the new first name')
            new_last_name = my_friend.last_name = input('What would you like for the new last name to be?')
            print(f'Great {new_last_name} has been set')
            print('I hope the breakup was amicable...')
            print('.... < / 3 ....')
            print('.... Completing this terrible task ....')
            print(' .. done .. ')
            print('your new friends name is : {} {}'.format(new_name_first_name, new_last_name))
        else : 
            print('Great thanks for keeping your friend.')
            

