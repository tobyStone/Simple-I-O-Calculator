'''
https://stackoverflow.com/questions/38649496/python-determine-if-a-string-contains-math
https://stackoverflow.com/questions/1740726/turn-string-into-operator
https://stackoverflow.com/questions/48255651/calculations-using-a-list-with-operations-with-numbers-python
https://codereview.stackexchange.com/questions/233814/reverse-polish-notation-rpn-calculator
https://stackoverflow.com/questions/61097144/reading-operations-line-by-line-and-making-eval-for-each-line
Mike James's The Python Programmer: Everything is Data, pages 239/240- Context Managers and With pattern
https://www.w3schools.com/python/python_ref_list.asp
Feedback from Darren 
'''
import operator

def writeToFile():
    with open("CalculationFile.txt", "a") as myFile:
        loop = True
        while loop is not False:
            sum = input("Please input a sum you'd like solving: ")
            split_sum = list(sum.replace(" ", ""))
            print(split_sum)
            for i  in split_sum:
                if i.isdigit() == False:
                    print(i)
                    print("These inputs are not all numerical, please try again")
                    continue
                else:
                    answer_print = print(f"This is the answer to your math's question: {eval(sum)}")
                    answer = eval(sum)
                    myFile.write(sum)
                    myFile.write("\n=")
                    myFile.write(str(answer))
                    myFile.write("\n")
                    break
            loop = input("Please input \'False\' if you want to stop calculating...: ")
            if loop.upper() == "FALSE":
                loop = False
            else:
                continue
    


def readFromFile():
    with open("calculations.txt", "r") as myFile:
        loop = True
        while loop is not False:
            sum = myFile.readline()
            if not sum:
                print("There's nothing in this line.")
            split_sum = list(sum.replace(" ", ""))
            print(split_sum)
            for i in split_sum:
                if i.isdigit() == False:
                    print(i)
                    print("These inputs are not all numerical, please try to read the next line")
                    continue
                else:
                    print(f"""Printed below is the file's calculation along with it's answer:\n{sum} = {eval(sum)}""")
                    break
            loop = input("""Please input \'False\' if you want to stop reading lines from the opened file...: """)
            if loop.upper() == "FALSE":
                print("Thank you, and goodbye.")
                loop = False
            else:
                continue
    

def addition(number1, number2):
    sum = number1 + number2
    return sum

def subtraction(number1, number2):
    difference = number1 - number2
    return difference

def multiplication(number1, number2):
    product = number1 * number2
    return product

def division(number1, number2):
    dividend = number1/number2
    return dividend

def exponential(number1 , number2):
    power = number1 ** number2
    return power


        
writeToFile()
#readFromFile()
           


#def calc(split_sum):
    number1 = 0
    number2 = 0
#    tokens = []
#    line = []
#    for i in split_sum:
#        if i == "*" or i == "+" or i == "-" or i == "\\" or i == "(" or i == ")":
#            if i == "(":
#                calc(split_line)
#            elif i == ")":
#                return finished_sum
#            if i == "+":
                int1_catcher = []
                int2_catcher = []
                if [:i:-1].isdigit():
                    int1_catcher.push()
                if[i::1].isdigit():
                    int2_catcher.append()
                number1 = int(int1_catcher)
                number2 = int(int2_catcher)
                addition(number1, number2)

#                number1 = 
#                split_line.pop(i)
#                tokens.append(i)
#            elif i == "*":
                int1_catcher = []
                int2_catcher = []
                if [:i:-1].isdigit():
                    int1_catcher.push()
                if[i::1].isdigit():
                    int2_catcher.append()
                number1 = int(int1_catcher)
                number2 = int(int2_catcher)
                multiplication()
#                  if i+1 = "*"
                 exponential()
#                i = operator.mul
#                tokens.append(i)
#            elif i == "-":
int1_catcher = []
                int2_catcher = []
                if [:i:-1].isdigit():
                    int1_catcher.push()
                if[i::1].isdigit():
                    int2_catcher.append()
                number1 = int(int1_catcher)
                number2 = int(int2_catcher)
                subtraction(number1, number2)

#            elif i == "/":
int1_catcher = []
                int2_catcher = []
                if [:i:-1].isdigit():
                    int1_catcher.push()
                if[i::1].isdigit():
                    int2_catcher.append()
                number1 = int(int1_catcher)
                number2 = int(int2_catcher)
                division(number1, number2)

#            else:
#                tokens.append(i)
#        else:    
#            tokens.append(int(i))
#    ans = 3 + 4 - (7-2) + 20
#    print(tokens)
    #for i in tokens:
    #        op, num = re.match(r'([+\-\*/])(\d+)', x).groups()
    #        result = ops[op](result, int(num))
    #return result
#    ans = eval(tokens)
#    print(ans)
#        line_split = list(line)
#        token_parsed = lines.remove(" ")
#        print(line_split)
#        print(type(line_split))
#        for i in line_split:
#            if i is ["+", "-", "*", "\\", "="] or i.isdigit():
#                tokens.append(i)
#                i = i + 1
#            print(tokens)
#            return tokens
#    except FileNotFoundError as error:
#        print("The file you are trying to open does not exist")
#        print(error)
#    finally:
#        if open_file is not None:
#            open_file.close()

#def printCalc(tokens):
#    print(tokens)


#runfile('calculations.txt')
#printCalc(tokens)

