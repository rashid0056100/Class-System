def add(a,b):

    return a+b

print(add(4554352345234524523,4523523452345234234))


def word():
    print("Hello World")
    return

word()



def math():
    a=23
    b=23
    def add():
        return a+b
    def sub():
        
        return a-b
    def mul():
        return a*b
        
    def division():
        return a//b
        
    return add(), sub(), mul(), division()
       
print(math())    


def office():
    password = "1234" 

    def pass1():
        entered = input("Enter the password: ")
        if entered == password:
            print("Enter in office")
        else:
            print("Access denied")

    return pass1()

office()      


add=lambda p,r:p+r
print(add(34,43))


a=[1,2,3,4]
square=list(map(lambda x:x**2,a))
print(square)
# new 
nums = [1, 2, 3, 4,5,6,7,8]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
data = [(2, 'b'), (1, 'a'), (3, 'c')]
sort_data=sorted(data,key=lambda x:x[1])
numbers = [x[0] for x in sort_data]
letters = [x[1] for x in sort_data]

print(numbers) 
print(letters)
print(sort_data)