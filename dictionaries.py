# A Dictionary is another name for object
# You can access these dictionaries just like arrays or assoc. arrays

dogs = { 
        'Dog-1': {'name':'Milo','age':1 },
        'Dog-2':{ 'name': 'Rin','age' : 2 } 
        }

failure_to_adopt_message = 'Sorry! try back next time, all of the pups have been checked out!'
ordering_pup = 'Ordering pup'
successful_adoption = 'Amazing - thank you for taking care of our sweet pup!'

# if shelter run's  out of pups then restock
def order_pup(restock_needed) :
    # num == 2 because we already had 2 dogs within the shelter
    num = 2 
    if restock_needed == True :
        num += 1
        dogs[f'Dog-{num}']

def adopt_pup(restock_needed, available) :
    if restock_needed is True :
        print(failure_to_adopt_message)
    else :
        print(successful_adoption)
        


for dog in dogs :
    # various ways to print each element within dictionary
    # Priint each element within dogs dictionary
    print(dog)
    # del all elements from dogs dictionary 
    del(dog)

# if dog array empty     
if bool(dogs) :
    print('Sorry! try back next time, all of the pups have been checked out!')
    print('...')
    print('We will make room for more and let you know when a new pup is ready')
    restock_needed = True
    available = False
    adopt_pup(restock_needed, available)
else :
    print('here is your new puppy!')
    restock_needed = False
    available = True
    adopt_pup(restock_needed, available)

