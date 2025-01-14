# Assignment 1.1
print("Naman "*3)

# Assignment 2.1
a=10
b=20
c=30
print("Result:",a+b+c)

# Assignment 2.2
print("hello" + " " + "world")

# Assignment 4.1
print("Table of 7")
for i in range(10):
    print(f"7 x {i} = ",7*i)
print("Table of 9")
for i in range(10):
    print(f"9 x {i} = ",9*i)

# Assignment 4.2
n=int(input("Enter a number:"))
for i in range(10):
    print(f"{n} x {i} = ",n*i)

# Assignment 4.3
m = int(input("Enter a number:"))
print("Sum of first n numbers:", sum(range(1,m+1)))

# Assignment 5.1
t = int(input("Enter first number:"))
u = int(input("Enter second number:"))
v = int(input("Enter third number:"))
print("Max of the 3 numbers is:",max(t,u,v))

# Assignment 5.2
ans=0
num=int(input("enter a number:"))
for i in range(1,num):
    if(i%7==0 and i%9==0):
        ans+=i
print("Sum of numbers divisible by 7 and 9 upto n:", ans)

# Assignment 5.3
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
p = int(input("Enter a number:"))
prime_sum=0
for i in range(1,p+1):
    if(is_prime(i)):
        prime_sum+=i
print("the sum of prime numbers upto n is:", prime_sum)

# Assignment 6.1
def add_odd(n):
    l = [i for i in range(1,n+1) if i%2!=0]
    return sum(l)
q=int(input("enter a number:"))
print("Sum of odd numbers upto n:", add_odd(q))

# Assignment 6.2
def add_prime(n):
    l = [i for i in range(1,n+1) if is_prime(i)]
    return sum(l)
r=int(input("enter a number:"))
print("Sum of prime numbers upto n:", add_prime(r))