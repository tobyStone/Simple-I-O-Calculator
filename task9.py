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
    

#def addition(number1, number2):
#    sum = number1 + number2
#    return sum

#def subtraction(number1, number2):
#    difference = number1 - number2
#    return difference

#def multiplication(number1, number2):
#    product = number1 * number2
#    return product

#def division(number1, number2):
#    dividend = number1/number2
#    return dividend

#def exponential(number1 , number2):
#    power = number1 ** number2
#    return power


        
writeToFile()
#readFromFile()
           

'''
https://stackoverflow.com/questions/4138202/using-isdigit-for-floats
'''

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


def list_to_number(array_to_change):
    sum = 0
    power = len(array_to_change) - 1
    for i in array_to_change:
        sum = sum + i * 10 ** power
        power = power - 1
    return sum



array_from_stream = ["3","-","7","*","2","3","/","8","+","0","-","3","2","1","8","9"]
print(array_from_stream)

def calc(array):

    while len(array)> 1:
        precedence_counter = 0
        int1_catcher = []
        int2_catcher = []
        counter = 0
        end_slice = 0
        h = 0
        j = 0
        for precedence in array:
            if precedence == "/":
                precedence_counter = precedence_counter + 1
            if precedence == "*":
                precedence_counter = precedence_counter + 1

        for i in array:
            if precedence_counter > 0:
                if i == "*":
                    print(i, "i", counter, "counter in if")

                    find_last_num = True
                    find_next_num = True
                    h = counter - 1
                    j = counter + 1

                    print(array, "array")
                    while find_next_num == True:
                        if j > len(array) - 1:
                            find_next_num = False
                            break
                        elif array[j].replace(".","").replace("-","").isdigit():
                            int2_catcher.append(float(array[j]))
            
                            print(int2_catcher, "int2_catch")
                            array.insert(counter, 'a')
                            array.pop(counter + 1)
                            array.insert(j, 'a')
                            array.pop(j + 1)
                            print(array, "array")
                            print(int2_catcher)
                            j = j + 1
                
                        else:
                            find_next_num = False
                            break

                    while find_last_num == True:
                        if h < 0:
                            find_last_num = False
                            break
                        elif array[h].replace(".","").replace("-","").isdigit():
                            int1_catcher.insert(0, float(array[h]))
                            array.insert(h, 'a')
                            array.pop(h + 1)
                            print(array, "array")
                            print(int1_catcher)
                            h = h - 1
                            end_slice = h
                        else:
                            find_last_num = False
                            break
                    print(array, "array")
                    print(int1_catcher)
                    print(int2_catcher)
                    int1_sum = list_to_number(int1_catcher)
                    int2_sum = list_to_number(int2_catcher)
                    print(int1_sum, "here")
                    print(int2_sum, "there")
                    reinsert_sum = multiplication(int1_sum, int2_sum)
                    int1_catcher.clear()
                    int2_catcher.clear()
                    array.insert(j, str(reinsert_sum))
                    counter = counter + 1
                    for index in array:
                        del array[end_slice + 1:j]
                        j = 0
                        h = 0
          
                    print(array)
                    precedence_counter = precedence_counter - 1

                elif i == "/":
                    find_last_num = True
                    find_next_num = True
                    h = counter - 1
                    j = counter + 1
                    while find_next_num == True:
                        if j > len(array)-1:
                            find_next_num = False
                            break
                        elif array[j].replace(".","").replace("-","").isdigit():
                            int2_catcher.append(float(array[j]))
                            array.insert(j, 'a')
                            array.pop(j + 1)
                            print(int2_catcher)
                            j = j + 1
                        else:
                            find_next_num = False
                            break
                    while find_last_num == True:
                        if h < 0:
                            find_last_num = False
                            break
                        elif array[h].replace(".","").replace("-","").isdigit():
                            int1_catcher.insert(0, float(array[h]))
                            array.insert(h, 'a')
                            array.pop(h + 1)
                            print(int1_catcher)
                            h = h - 1
                            end_slice = h
                        else:
                            find_last_num = False
                            break
                    print(int1_catcher)
                    print(int2_catcher)
                    int1_sum = list_to_number(int1_catcher)
                    int2_sum = list_to_number(int2_catcher)
                    int1_catcher.clear()
                    int2_catcher.clear()
                    print(int1_sum)
                    print(int2_sum)
                    reinsert_sum = division(int1_sum, int2_sum)
                    array.insert(j, str(reinsert_sum))
                    print(array)
                    counter = counter + 1
                    for index in array:
                        del array[end_slice + 1:j]
                        j = 0
                        h = 0
                    precedence_counter = precedence_counter - 1

                else:
                    counter = counter + 1
                    for index in array:
                        del array[end_slice + 1:j]
                        j = 0
                        h = 0

            else:
                if i == "+":
                    print(i, "i", counter, "counter in if")

                    find_last_num = True
                    find_next_num = True
                    h = counter - 1
                    j = counter + 1

                    print(array, "array")
                    while find_next_num == True:
    #                    print(j,"j",array[j])
                        if j > len(array) - 1:
                            find_next_num = False
                            break
                        elif array[j].replace(".","").replace("-","").isdigit():
                            int2_catcher.append(float(array[j]))
                            print(j,"j")  
                            print(int2_catcher, "int2_catch")
                            array.insert(counter, 'a')
                            array.pop(counter + 1)
                            array.insert(j, 'a')
                            array.pop(j + 1)
                            print(array, "array")
                            print(int2_catcher)
                            j = j + 1
                
                        else:
                            find_next_num = False
                            break

                    while find_last_num == True:
                        print(h,"h", array[h])
                        if h < 0:
                            find_last_num = False
                            print("here")
                            break
                        elif array[h].replace(".","").replace("-","").isdigit():
                            print(h,"h2")
                            int1_catcher.insert(0, float(array[h]))
                            array.insert(h, 'a')
                            array.pop(h + 1)
                            print(array, "array")
                            print(int1_catcher)
                            h = h - 1
                            end_slice = h
                        else:
                            find_last_num = False
                            print("there")
                            break
                    print(array, "array")
                    print(int1_catcher)
                    print(int2_catcher)
                    int1_sum = list_to_number(int1_catcher)
                    int2_sum = list_to_number(int2_catcher)
                    print(int1_sum, "here")
                    print(int2_sum, "there")
                    reinsert_sum = addition(int1_sum, int2_sum)
                    int1_catcher.clear()
                    int2_catcher.clear()
                    array.insert(j, str(reinsert_sum))
                    counter = counter + 1
                    for index in array:
                        del array[end_slice + 1:j]
                        j = 0
                        h = 0
          
                    print(array)

                elif i == "-":
                    find_last_num = True
                    find_next_num = True
                    h = counter - 1
                    j = counter + 1
                    while find_next_num == True:
                        if j > len(array)-1:
                            find_next_num = False
                            break
                        elif array[j].replace(".","").replace("-","").isdigit():
                            int2_catcher.append(float(array[j]))
                            array.insert(j, 'a')
                            array.pop(j + 1)
                            print(int2_catcher)
                            j = j + 1
                        else:
                            find_next_num = False
                            break
                    while find_last_num == True:
                        if h < 0: 
                            find_last_num = False
                            break
                        elif array[h].replace(".","").replace("-","").isdigit():
                            int1_catcher.insert(0, float(array[h]))
                            array.insert(h, 'a')
                            array.pop(h + 1)
                            print(int1_catcher)
                            h = h - 1
                            end_slice = h
                        else:
                            find_last_num = False
                            break
                    print(int1_catcher)
                    print(int2_catcher)
                    int1_sum = list_to_number(int1_catcher)
                    int2_sum = list_to_number(int2_catcher)
                    int1_catcher.clear()
                    int2_catcher.clear()
                    print(int1_sum)
                    print(int2_sum)
                    reinsert_sum = subtraction(int1_sum, int2_sum)
                    array.insert(j, str(reinsert_sum))
                    print(array)
                    counter = counter + 1
                    for index in array:
                        del array[end_slice + 1:j]
                        j = 0
                        h = 0
          
                else:
                    counter = counter + 1
                    for index in array:
                        del array[end_slice + 1:j]
                        j = 0
                        h = 0
      #      counter = counter + 1
            print(counter, "counter first pass")            
        print(array)
        print(j)
        print(reinsert_sum)

calc(array_from_stream)





##def calc(split_sum):
#    number1 = 0
#    number2 = 0
##    tokens = []
##    line = []
##    for i in split_sum:
##        if i == "*" or i == "+" or i == "-" or i == "\\" or i == "(" or i == ")":
##            if i == "(":
##                calc(split_line)
##            elif i == ")":
##                return finished_sum
##            if i == "+":
#                int1_catcher = []
#                int2_catcher = []
#                if [:i:-1].isdigit():
#                    int1_catcher.push()
#                if[i::1].isdigit():
#                    int2_catcher.append()
#                number1 = int(int1_catcher)
#                number2 = int(int2_catcher)
#                addition(number1, number2)

##                number1 = 
##                split_line.pop(i)
##                tokens.append(i)
##            elif i == "*":
#                int1_catcher = []
#                int2_catcher = []
#                if [:i:-1].isdigit():
#                    int1_catcher.push()
#                if[i::1].isdigit():
#                    int2_catcher.append()
#                number1 = int(int1_catcher)
#                number2 = int(int2_catcher)
#                multiplication()
##                  if i+1 = "*"
#                 exponential()
##                i = operator.mul
##                tokens.append(i)
##            elif i == "-":
#int1_catcher = []
#                int2_catcher = []
#                if [:i:-1].isdigit():
#                    int1_catcher.push()
#                if[i::1].isdigit():
#                    int2_catcher.append()
#                number1 = int(int1_catcher)
#                number2 = int(int2_catcher)
#                subtraction(number1, number2)

##            elif i == "/":
#int1_catcher = []
#                int2_catcher = []
#                if [:i:-1].isdigit():
#                    int1_catcher.push()
#                if[i::1].isdigit():
#                    int2_catcher.append()
#                number1 = int(int1_catcher)
#                number2 = int(int2_catcher)
#                division(number1, number2)

##            else:
##                tokens.append(i)
##        else:    
##            tokens.append(int(i))
##    ans = 3 + 4 - (7-2) + 20
##    print(tokens)
#    #for i in tokens:
#    #        op, num = re.match(r'([+\-\*/])(\d+)', x).groups()
#    #        result = ops[op](result, int(num))
#    #return result
##    ans = eval(tokens)
##    print(ans)
##        line_split = list(line)
##        token_parsed = lines.remove(" ")
##        print(line_split)
##        print(type(line_split))
##        for i in line_split:
##            if i is ["+", "-", "*", "\\", "="] or i.isdigit():
##                tokens.append(i)
##                i = i + 1
##            print(tokens)
##            return tokens
##    except FileNotFoundError as error:
##        print("The file you are trying to open does not exist")
##        print(error)
##    finally:
##        if open_file is not None:
##            open_file.close()

##def printCalc(tokens):
##    print(tokens)


##runfile('calculations.txt')
##printCalc(tokens)

