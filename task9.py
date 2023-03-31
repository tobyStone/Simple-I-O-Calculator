'''
https://stackoverflow.com/questions/38649496/python-determine-if-a-string-contains-math
https://stackoverflow.com/questions/61097144/reading-operations-line-by-line-and-making-eval-for-each-line
Mike James's The Python Programmer: Everything is Data, pages 239/240- Context Managers and With pattern
https://stackoverflow.com/questions/4138202/using-isdigit-for-floats
https://www.w3schools.com/python/python_ref_list.asp
Feedback from Darren and Chris at Hyperion 
'''

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
    

        
#writeToFile()
#readFromFile()
           

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

def find_next_num_func(j, find_next_num, array, int2_catcher, counter):

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
    tuple_return_next = (array, j, int2_catcher)
    return tuple_return_next


def find_last_num_func(h, find_last_num, array, int1_catcher):

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
    tuple_return_last = (array, h, int1_catcher, end_slice)
    return tuple_return_last

def sum_and_replace_func(operator, j, h, int1_catcher, int2_catcher, counter, array, end_slice):

    print(array, "array")
    print(int1_catcher)
    print(int2_catcher)
    int1_sum = list_to_number(int1_catcher)
    int2_sum = list_to_number(int2_catcher)
    print(int1_sum, "here")
    print(int2_sum, "there")
    if operator == "*":
        reinsert_sum = multiplication(int1_sum, int2_sum)
    elif operator == "/":
        reinsert_sum = division(int1_sum, int2_sum)
    elif operator == "+":
        reinsert_sum = addition(int1_sum, int2_sum)
    elif operator == "-":
        reinsert_sum = subtraction(int1_sum, int2_sum)

    int1_catcher.clear()
    int2_catcher.clear()
    array.insert(j, str(reinsert_sum))
    counter = counter + 1
    print(end_slice, "end_slice")
    for index in array:
        del array[end_slice + 1:j]
        j = 0
        h = 0
    tuple_return_final = (j, h, int1_catcher, int2_catcher, counter, array)
    return tuple_return_final


array_from_stream = ["3","-","7","*","2","3","/","8","+","0","-","3","2","1","8","8"]
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
                    operator = "*"
                    print(i, "i", counter, "counter in if")

                    find_last_num = True
                    find_next_num = True
                    h = counter - 1
                    j = counter + 1

                    print(array, "array")
                    tuple_returned_next = find_next_num_func(j, find_next_num, array, int2_catcher, counter)
                    array, j, int2_catcher = tuple_returned_next


                    tuple_returned_last = find_last_num_func(h, find_last_num, array, int1_catcher)
                    array, h, int1_catcher, end_slice = tuple_returned_last

                    tuple_returned_final = sum_and_replace_func(operator, j, h, int1_catcher, int2_catcher, counter, array, end_slice)
                    j, h, int1_catcher, int2_catcher, counter, array = tuple_returned_final

                    precedence_counter = precedence_counter - 1

                elif i == "/":
                    operator = "/"
                    find_last_num = True
                    find_next_num = True
                    h = counter - 1
                    j = counter + 1
                    tuple_returned_next = find_next_num_func(j, find_next_num, array, int2_catcher, counter)
                    array, j, int2_catcher = tuple_returned_next
                    tuple_returned_last = find_last_num_func(h, find_last_num, array, int1_catcher)
                    array, h, int1_catcher, end_slice = tuple_returned_last

                    tuple_returned_final = sum_and_replace_func(operator, j, h, int1_catcher, int2_catcher, counter, array, end_slice)
                    j, h, int1_catcher, int2_catcher, counter, array = tuple_returned_final

                    precedence_counter = precedence_counter - 1

                else:
                    counter = counter + 1
                    for index in array:
                        del array[end_slice + 1:j]
                        j = 0
                        h = 0

            else:
                if i == "+":
                    operator = "+"
                    print(i, "i", counter, "counter in if")

                    find_last_num = True
                    find_next_num = True
                    h = counter - 1
                    j = counter + 1

                    print(array, "array")
                    tuple_returned_next = find_next_num_func(j, find_next_num, array, int2_catcher, counter)
                    array, j, int2_catcher = tuple_returned_next
                    tuple_returned_last = find_last_num_func(h, find_last_num, array, int1_catcher)
                    array, h, int1_catcher, end_slice = tuple_returned_last


                    tuple_returned_final = sum_and_replace_func(operator, j, h, int1_catcher, int2_catcher, counter, array, end_slice)
                    j, h, int1_catcher, int2_catcher, counter, array = tuple_returned_final
                    print(array)

                elif i == "-":
                    operator = "-"
                    find_last_num = True
                    find_next_num = True
                    h = counter - 1
                    j = counter + 1
                    tuple_returned_next = find_next_num_func(j, find_next_num, array, int2_catcher, counter)
                    array, j, int2_catcher = tuple_returned_next
                    tuple_returned_last = find_last_num_func(h, find_last_num, array, int1_catcher)
                    array, h, int1_catcher, end_slice = tuple_returned_last


                    tuple_returned_final = sum_and_replace_func(operator, j, h, int1_catcher, int2_catcher, counter, array, end_slice)
                    j, h, int1_catcher, int2_catcher, counter, array = tuple_returned_final

                else:
                    counter = counter + 1
                    for index in array:
                        del array[end_slice + 1:j]
                        j = 0
                        h = 0
        print(array)

calc(array_from_stream)



