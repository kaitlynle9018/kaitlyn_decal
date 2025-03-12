#Section 1: HW 1/2 Review: Terminal, Command Line, Git
#1) pwd
#2) ls
#3) cd python_decal/brianna_repo and git pull origin main
#4) mv homework.py ~/judy_decal/homework/
#5) cat homework.py
#6) nano homework.py
#7) ctrl+x, git add homework.py, git commit -m "adding homework", git push origin main 
#8) git pull --rebase origin main, git push origin main (the error is that the remote repository has changes that are not in the local repository; there must be a pull before push)
#9) cd ~/Recents/

#Section 2: HW 3 Review: Data Types, Functions, Conditionals, Loops
#2.1) Data types
def checkDataType(value):
    return type(value).__name__
print(checkDataType(3.14))
print(checkDataType(True))
#2.2) Conditionals
def evenOrOdd(n):
    return "Even" if n % 2 == 0 else "Odd"
print(evenOrOdd(7)) 
print(evenOrOdd(10))  

#Section 3: Loops
def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = [1, 2, 3, 4, 5]
print(sumWithLoop(numbers)) 
#Section 4: HW 4 Review: Lists
#4.1) Lists
def duplicateList(lst):
    new_list = []
    for item in lst:
        new_list.extend([item, item])
    return new_list
print(duplicateList(['a', 'b', 'c']))
#4.2) Debugging 
def square(num):
    return num * num
print(square(4))

