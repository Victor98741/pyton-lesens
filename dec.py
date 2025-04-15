x = 0
def counter(func): 
       
    def call(): 
        global x
        x += 1
        print(f'This fuction called:{x}')
        func()
    return call

@counter
def some_func():
    print('Hello')
    
some_func()
some_func()
some_func()



def counter(func):      
    def call(): 
        func.__dict__['x'] += 1
        print(f"This fuction called:{func.__dict__['x']}")
        func()
    func.__dict__['x'] = 0    
    return call

@counter
def some_func():
    print('Hello')
    
some_func()
some_func()
some_func()


from collections import Counter

my_string = 'aaaabbccccbbbb'

my_counter = Counter(my_string)
print(my_counter)