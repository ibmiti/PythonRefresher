class Human :
    #  when this is provided this forces the users of this class to pass in these arguments to have a copy of this class
    # if we provide default values to each variable within the param of init - we do not need to enter all args
    def __init__(self, name, age , hair_color, skin_color, shirt_color, pants_color) :
        self.name = name
        self.age =  age 
        self.hair_color =  hair_color
        self.skin_color =  skin_color
        self.shirt_color = shirt_color
        self.pants_color = pants_color
    
    
    #  class variable - accessible on class
    friend_info = 'My friend is allergic to everthing..'
    
    seasons = ['spring', 'fall', 'winter', 'summer']
    
    print('here are all of the seasons that makes my friend sneeze')
    for season in seasons :
       print(season)

    
    season = input('Which season is it where you are from? write any that match the list: ')
    
    # print(season)
    if season in seasons :
        print(season)
        Sneeze('hello')
    else :
        print('no not found')
    # if seasonal_info : 
    
    def Sneeze(self, str):
        print('AHHHH-CHOOOO' + str)    

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
            hair  = self.hair_color =  input("what is your friends hair color?")
            skin  = self.skin_color =  input("what is your friends skin tone?")
            shirt = self.shirt_color = input("what is your friends shirt color?")
            pants = self.pants_color = input("what color of pants does your friend happen to be wearing?")

hair  = self.hair_color =  input("what is your friends hair color?")
skin  = self.skin_color =  input("what is your friends skin tone?")
shirt = self.shirt_color = input("what is your friends shirt color?")
pants = self.pants_color = input("what color of pants does your friend happen to be wearing?")
