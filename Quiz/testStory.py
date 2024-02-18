import testQuiz
import time

def questions(number):

    count = 1
    
    while count <= number: # loops count + 1 times
        
        print("Answer this question " + name + ": ")
        time.sleep(2)
        if testQuiz.quiz() == 0:
            print("Wrong, lets continue")
        else:
            print("Well done")
            count += 1
            
        print("You answered " + str(count - 1) + " questions correct!") 
            
            
            
print("\n" * 2)
name = input("What is your name? : ")
print("\n")
print("Hello there " + name)
numberOfQuestions = input("How many questions you want to answer? : ")
numberOfQuestions = int(numberOfQuestions)
print("\n")

questions(numberOfQuestions)

print("You did really well!")

