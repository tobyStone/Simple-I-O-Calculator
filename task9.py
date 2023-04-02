'''
https://stackoverflow.com/questions/38649496/python-determine-if-a-string-contains-math
https://stackoverflow.com/questions/61097144/reading-operations-line-by-line-and-making-eval-for-each-line
Mike next_num_for_loop_counterames's The Python Programmer: Everything is Data, pages 239/240- Context Managers and With pattern
https://stackoverflow.com/questions/4138202/using-isdigit-for-floats
https://www.w3schools.com/python/python_ref_list.asp
Feedback from Darren and Chris at Hyperion 
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
    for place_value_column in array_to_change:
        sum = sum + place_value_column * 10 ** power
        power = power - 1
    return sum

def find_next_num_func(next_num_for_loop_counter, find_next_num, array, int2_catcher, for_loop_counter):

    while find_next_num == True:
        if next_num_for_loop_counter > len(array) - 1:
            find_next_num = False
            break
        elif array[next_num_for_loop_counter].replace(".","").replace("-","").isdigit():
            int2_catcher.append(float(array[next_num_for_loop_counter]))
            
            print(int2_catcher, "int2_catch")
            array.insert(for_loop_counter, 'a')
            array.pop(for_loop_counter + 1)
            array.insert(next_num_for_loop_counter, 'a')
            array.pop(next_num_for_loop_counter + 1)
            print(array, "array")
            print(int2_catcher)
            next_num_for_loop_counter = next_num_for_loop_counter + 1
                
        else:
            find_next_num = False
            break
    tuple_return_next = (array, next_num_for_loop_counter, int2_catcher)
    return tuple_return_next


def find_last_num_func(last_num_counter, find_last_num, array, int1_catcher):

    while find_last_num == True:
        if last_num_counter < 0:
            find_last_num = False
            break
        elif array[last_num_counter].replace(".","").replace("-","").isdigit():
            int1_catcher.insert(0, float(array[last_num_counter]))
            array.insert(last_num_counter, 'a')
            array.pop(last_num_counter + 1)
            print(array, "array")
            print(int1_catcher)
            last_num_counter = last_num_counter - 1
            end_slice = last_num_counter
        else:
            find_last_num = False
            break
    tuple_return_last = (array, last_num_counter, int1_catcher, end_slice)
    return tuple_return_last

def sum_and_replace_func(operator, next_num_for_loop_counter, last_num_counter, int1_catcher, int2_catcher, for_loop_counter, array, end_slice):

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
    array.insert(next_num_for_loop_counter, str(reinsert_sum))
    for_loop_counter = for_loop_counter + 1
    print(end_slice, "end_slice")
    for index in array:
        del array[end_slice + 1:next_num_for_loop_counter]
        next_num_for_loop_counter = 0
        last_num_counter = 0
    tuple_return_final = (next_num_for_loop_counter, last_num_counter, int1_catcher, int2_catcher, for_loop_counter, array)
    return tuple_return_final




def calc(array):

    loop = True

    while loop == True:
        print("looping")
        precedence_for_loop_counter = 0
        int1_catcher = []
        int2_catcher = []
        for_loop_counter = 0
        end_slice = 0
        last_num_counter = 0
        next_num_for_loop_counter = 0
        for precedence in array:
            if precedence == "/":
                precedence_for_loop_counter = precedence_for_loop_counter + 1
            if precedence == "*":
                precedence_for_loop_counter = precedence_for_loop_counter + 1
        print(precedence_for_loop_counter, "precedence")

        for numeric in array:
            print(numeric, "for looping")
            if precedence_for_loop_counter > 0:
                if numeric == "*":
                    operator = "*"
                    print(numeric, "numeric", for_loop_counter, "for_loop_counter in if")

                    find_last_num = True
                    find_next_num = True
                    last_num_counter = for_loop_counter - 1
                    next_num_for_loop_counter = for_loop_counter + 1

                    print(array, "array")
                    tuple_returned_next = find_next_num_func(next_num_for_loop_counter, find_next_num, array, int2_catcher, for_loop_counter)
                    array, next_num_for_loop_counter, int2_catcher = tuple_returned_next


                    tuple_returned_last = find_last_num_func(last_num_counter, find_last_num, array, int1_catcher)
                    array, last_num_counter, int1_catcher, end_slice = tuple_returned_last

                    tuple_returned_final = sum_and_replace_func(operator, next_num_for_loop_counter, last_num_counter, int1_catcher, int2_catcher, for_loop_counter, array, end_slice)
                    next_num_for_loop_counter, last_num_counter, int1_catcher, int2_catcher, for_loop_counter, array = tuple_returned_final

                    precedence_for_loop_counter = precedence_for_loop_counter - 1
                    if precedence_for_loop_counter == 0:
                        numeric = 0

                elif numeric == "/":
                    operator = "/"
                    find_last_num = True
                    find_next_num = True
                    last_num_counter = for_loop_counter - 1
                    next_num_for_loop_counter = for_loop_counter + 1
                    print(array[next_num_for_loop_counter], "array next_num_for_loop_counter + 1 for zero")
                    if array[next_num_for_loop_counter] == "0":
                        print("You are trying to divide by zero. This is undefined behaviour. The calculation is now exiting.")
                        del array[1:]
                        array[0] = "undefined"
                        loop = False
                        break
                    tuple_returned_next = find_next_num_func(next_num_for_loop_counter, find_next_num, array, int2_catcher, for_loop_counter)
                    array, next_num_for_loop_counter, int2_catcher = tuple_returned_next
                    tuple_returned_last = find_last_num_func(last_num_counter, find_last_num, array, int1_catcher)
                    array, last_num_counter, int1_catcher, end_slice = tuple_returned_last

                    tuple_returned_final = sum_and_replace_func(operator, next_num_for_loop_counter, last_num_counter, int1_catcher, int2_catcher, for_loop_counter, array, end_slice)
                    next_num_for_loop_counter, last_num_counter, int1_catcher, int2_catcher, for_loop_counter, array = tuple_returned_final

                    precedence_for_loop_counter = precedence_for_loop_counter - 1
                    precedence_for_loop_counter = precedence_for_loop_counter - 1
                    if precedence_for_loop_counter == 0:
                        break
                        continue


                else:
                    for_loop_counter = for_loop_counter + 1
                    for index in array:
                        del array[end_slice + 1:next_num_for_loop_counter]
                        next_num_for_loop_counter = 0
                        last_num_counter = 0

            else:
                if numeric == "+":
                    operator = "+"
                    print(numeric, "numeric", for_loop_counter, "for_loop_counter in if")

                    find_last_num = True
                    find_next_num = True
                    last_num_counter = for_loop_counter - 1
                    next_num_for_loop_counter = for_loop_counter + 1

                    print(array, "array")
                    tuple_returned_next = find_next_num_func(next_num_for_loop_counter, find_next_num, array, int2_catcher, for_loop_counter)
                    array, next_num_for_loop_counter, int2_catcher = tuple_returned_next
                    tuple_returned_last = find_last_num_func(last_num_counter, find_last_num, array, int1_catcher)
                    array, last_num_counter, int1_catcher, end_slice = tuple_returned_last


                    tuple_returned_final = sum_and_replace_func(operator, next_num_for_loop_counter, last_num_counter, int1_catcher, int2_catcher, for_loop_counter, array, end_slice)
                    next_num_for_loop_counter, last_num_counter, int1_catcher, int2_catcher, for_loop_counter, array = tuple_returned_final
                    print(array)
                    break
                    continue

                elif numeric == "-":
                    operator = "-"
                    find_last_num = True
                    find_next_num = True
                    last_num_counter = for_loop_counter - 1
                    next_num_for_loop_counter = for_loop_counter + 1
                    tuple_returned_next = find_next_num_func(next_num_for_loop_counter, find_next_num, array, int2_catcher, for_loop_counter)
                    array, next_num_for_loop_counter, int2_catcher = tuple_returned_next
                    tuple_returned_last = find_last_num_func(last_num_counter, find_last_num, array, int1_catcher)
                    array, last_num_counter, int1_catcher, end_slice = tuple_returned_last


                    tuple_returned_final = sum_and_replace_func(operator, next_num_for_loop_counter, last_num_counter, int1_catcher, int2_catcher, for_loop_counter, array, end_slice)
                    next_num_for_loop_counter, last_num_counter, int1_catcher, int2_catcher, for_loop_counter, array = tuple_returned_final
                    break
                    continue

                else:
                    for_loop_counter = for_loop_counter + 1
                    for index in array:
                        del array[end_slice + 1:next_num_for_loop_counter]
                        next_num_for_loop_counter = 0
                        last_num_counter = 0
            if len(array) <= 1:
                loop = False

            print(array)
    return array





def writeToFile():
    with open("CalculationFile.txt", "a") as myFile:
        loop = True
        while loop is not False:
            sum = input("""Please input a sum of as many whole numbers you'd like.\n
           You may include '+', '-', '*', and '/': """)
            split_sum = list(sum.replace(" ", "").replace("\n",""))
            print(split_sum)
            for i  in split_sum:
                if i.isdigit() == False:
                    print(i)
                    print("These inputs are not all numerical, please try again")
                    continue
                else:
                    sum_answered = calc(split_sum)
                    answer_print = print(f"This is the answer to your math's question: {sum_answered[0]}")
                    myFile.write(str(sum))
                    myFile.write(" = ")
                    myFile.write(str(sum_answered[0]))
                    myFile.write("\n")
                    break
            loop = input("Please input \'False\' if you want to stop calculating...: ")
            if loop.upper() == "FALSE":
                loop = False
                print("Thank you, and goodbye.")
            else:
                continue
    


def readFromFile(file_chosen):
    myFile = None
    try:
        with open(file_chosen, "r") as myFile:
            print("File opening...\n\nReading first line...\n\n")
            loop = True
            while loop is not False:
                sum = myFile.readline()
                if not sum:
                    print("There's nothing in this line.")
                split_sum = list(sum.replace(" ", "").replace("\n",""))
                print(split_sum)
                for i in split_sum:
                    if i.isdigit() == False:
                        print(i)
                        print("These inputs are not all numerical, please try to read the next line")
                        continue
                    else:
                        print(type(split_sum))
                        sum_answered = calc(split_sum)
                        print(type(sum_answered))
                        print(f"""Printed below is the file's calculation along with it's answer:\n{sum} = {sum_answered[0]}""")
                        break
                loop = input("""Please input \'False\' if you want to stop reading lines from the opened file...: """)
                if loop.upper() == "FALSE":
                    print("Thank you, and goodbye.")
                    loop = False
                else:
                    continue

    except FileNotFoundError as error:

        print("""Something has gone badly wrong with the logic in ths program.\n Please turn the computer off and on and try again...""")
        print(error)

    finally:
        if myFile is not None:
            myFile.close()


def stream_choice():
    looper = True

    while looper == True:

        choice = input("""Welcome to the calculator.\n 
        You can either choose to input an expression for calculation,\n
       or to open a file which will import expressions to be calculated.\n
       For the first please type 'input'.\n
       For the second please type 'import': """)
        if choice.upper() == 'INPUT':
            looper = False
            writeToFile()
        elif choice.upper() == 'IMPORT':
            fileChoice = input("""Please input the file you want to open.\n
           The following file: 'calculations.txt' is available: """)
            if fileChoice == 'calculations.txt':
                file_chosen = 'calculations.txt'
                looper = False
                readFromFile(file_chosen)
            else:
                print("The file that you are trying to open does not exist. Please try again: ")
        else:
            print("You have not made one of the choices. Please try again: ")


        
stream_choice()
           

