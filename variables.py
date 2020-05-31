import sys 

# num = 1
# count = 0
# while num >= 1 : 
#     count += num
#     continue 
#     print(count)

# in this file we will show usages of pythons variables and constants
MIN_AGE_TO_ENTER = 18
INCORRECT_ANSWERS_GIVEN = 3

# based off time of day print hello and good morning vs hello and good evening
greetings = ['hello '] 
species = ['Human','non-human']
user_names = []

# pick greeting for adjective
def greet() : 

    print(greetings[0] + species[0])
    species_check = input('... \n you are indeed human no?')  
    
    #  if the user response with an input ( answer || response ) execute the nested code
    if species_check != False :
        print('hmm..\n ...')
        if species_check.lower() == 'yes' :
            print("great i'm glad I got that correct - my eyes do not yet see.")
        else :
            non_human_user = input('okay sorry about that, are you {}?'.format(species[0] or species[1]))
            if non_human_user :
                print('... how best to say this, you terrify me ')
        
        
# execute greeting
greet()



#  this could even search the internet for more choices
def species_selection(arg , arg1) :
    print('foo')
    


users_age = input('how old are you?: ')
print(users_age)
if users_age < str(MIN_AGE_TO_ENTER) :
    print('sorry minimum age not met')
    
    attempts_given_to_enter_game = 3
    #  if attempts taken are over 3 then send user to infinite loop
    print('Hello human - you have {} attempts before you are sunk into an endless loop'.format(int(attempts_given_to_enter_game) ++ 1 ))
    # sometimes we must convert types to properly compare them
    if int(users_age) <= 18 :
        print(f'You have {attempts_given_to_enter_game -- 1}')
        
    # while attempts_given_to_enter_game >= 2 :  
    #     print('sorry try again. That was not the correct answer')
        
    #     print(attempts_given_to_enter_game)
        
    #     if attempts_given_to_enter_game == 0 :
    #         print('Good-Bye')
    #         sys.exit(0)

name_of_game = "variables game"
name_of_host = "variable"
print("Welome to the " + name_of_game , "\n my name is {}".format(name_of_host))

# print(f"My name is {}".format(name_of_host))
question = input("what's your name?: ")
user_names = []
user_names.append(question)
print(user_names[0])
if user_names:
    response = "Great, Thank you for that, i'll call you "
    print(response + user_names[0])
    # we could also use format() method here instead of f'' - string
    response2 = input(f"is it okay if I call you {user_names[0]} yes or no?")
    if response2.lower() == 'yes' :
        print('great i am so glad \n')
        #  figure out how to include a picture here? 
        print(' ++ loading ++ ')
        
        def loading() :
            
            print('++ Beginning load ++')
            print('++')
            print('+++')
            print(' ')
            print('+++ Almost Done +++')
            print(' ')
            print(' ')
            print('name added to my list of favorite people.')
            print(' ')
            print(' ')
            print('Heres the updated list')
            print(user_names)
            print(' ')
            print(' ')
           
            print('Would you like to tell me your middle name?')
            middle_name_request_prompt = input('yes or no?')
            
            if middle_name_request_prompt.lower() == 'yes' :
                
                middle_name = input("what is your middle name? ") 
                if middle_name : 
                    print('great thank your for that')
                    print('What is your last name?')
                    last_name = input('Enter last name here: ')
                
                print('So your full name is : ')
                print(user_names[0] +  " " + middle_name + " " + last_name)
                sys.exit(0)
            else :
                print('Alright if I cannot have your information I will end this conversation...')
                print('good bye')
                sys.exit(0)
            
            
        loading()
        
        def middle_name() :
            middle_name_request = input("what is your middle name? ")
            middle_name = middle_name_request
            print(middle_name)
            
        def last_name() :
            last_name_request = input("what is your last name? ")
            last_name = last_name_request
            print(last_name)
            
        # def favorite_list() :
        #     print("Heres the list")
        #     user_names

        middle_name()
        last_name()   
        
        
        # favorite_list()
        
            
        
    else : 
        print('Sorry - I apologize')
    
    
