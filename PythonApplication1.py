#from word2number import w2n

#MAX_HOURS = 60
#MIN_HOURS = 10
#total_wages = 0.0
#normal_pay = 10.0
#overtime = 15.0
#standard_hours = 40
#worked_hours = 0

#worked_hours = int(input("Please tell us how many hours you worked: "))

#if(worked_hours < MAX_HOURS and worked_hours > MIN_HOURS):

#    if (worked_hours > standard_hours):
#        total_wages = ((worked_hours - standard_hours) * overtime) + (standard_hours * normal_pay) 
#        print("I will pay you: ", total_wages)

#    elif (worked_hours <= standard_hours):
#        total_wages = worked_hours * normal_pay
#        print("I will pay you: ", total_wages)

#    else:
#        print("None of this makes sense!")

#else: 
#    print("Incorrect number of hours, please input a new figure...")

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


#int1_catcher =[]
#int2_catcher = []
#counter = 0
#for i in array:
##    print(i)
#    if i == "/":
#        find_last_num = True
#        find_next_num = True
#        h = counter - 1
#        j = counter + 1
#        print(array, "array")
#        while find_next_num == True:
#            if j > len(array) - 1:
#                find_next_num = False
#                break
#            elif array[j].isdigit():
#                int2_catcher.append(int(array[j]))
#                array.insert(counter, " ")
#                array.pop(counter + 1)
#                array.insert(j, " ")
#                array.pop(j + 1)
#                print(array, "array")
#                print(int2_catcher)
#                j = j + 1
#            else:
#                find_next_num = False
#                break
#        while find_last_num == True:
#            if h < 0:
#                find_last_num = False
#                break
#            elif array[h].isdigit():
#                int1_catcher.insert(0, int(array[h]))
#                array.insert(h, " ")
#                array.pop(h + 1)
#                print(array, "array")
#                print(int1_catcher)
#                h = h - 1
#            else:
#                find_last_num = False
#                break
#        print(array, "array")
#        print(int1_catcher)
#        print(int2_catcher)
#        int1_sum = list_to_number(int1_catcher)
#        int2_sum = list_to_number(int2_catcher)
#        int1_catcher.clear()
#        int2_catcher.clear()
#        print(int1_sum)
#        print(int2_sum)
#        reinsert_sum = division(int1_sum, int2_sum)
#        array.insert(j, str(reinsert_sum))
#        print(array)
#    elif i == "*":
#        find_last_num = True
#        find_next_num = True
#        h = counter - 1
#        j = counter + 1
#        while find_next_num == True:
#            if j > len(array)-1:
#                find_next_num = False
#                break
#            elif array[j].isdigit():
#                int2_catcher.append(int(array[j]))
#                array.insert(j, " ")
#                array.pop(j + 1)
#                print(int2_catcher)
#                j = j + 1
#            else:
#                find_next_num = False
#                break
#        while find_last_num == True:
#            if h < 0:
#                find_last_num = False
#                break
#            elif array[h].isdigit():
#                int1_catcher.insert(0, int(array[h]))
#                array.insert(h, " ")
#                array.pop(h + 1)
#                print(int1_catcher)
#                h = h - 1
#            else:
#                find_last_num = False
#                break
#        print(int1_catcher)
#        print(int2_catcher)
#        int1_sum = list_to_number(int1_catcher)
#        int2_sum = list_to_number(int2_catcher)
#        int1_catcher.clear()
#        int2_catcher.clear()
#        print(int1_sum)
#        print(int2_sum)
#        reinsert_sum = multiplication(int1_sum, int2_sum)
#        print(reinsert_sum)
#        array.insert(j, str(reinsert_sum))
#        print(array)
#    counter = counter + 1


array = ["5","3","*","3","+","7","8","/","2"]
print(array)

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
                    elif array[j].isdigit():
                        int2_catcher.append(int(array[j]))
            
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
                    elif array[h].isdigit():
                        int1_catcher.insert(0, int(array[h]))
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
                    elif array[j].isdigit():
                        int2_catcher.append(int(array[j]))
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
                    elif array[h].isdigit():
                        int1_catcher.insert(0, int(array[h]))
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
                    if j > len(array) - 1:
                        find_next_num = False
                        break
                    elif array[j].isdigit():
                        int2_catcher.append(int(array[j]))
            
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
                    elif array[h].isdigit():
                        int1_catcher.insert(0, int(array[h]))
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
                    elif array[j].isdigit():
                        int2_catcher.append(int(array[j]))
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
                    elif array[h].isdigit():
                        int1_catcher.insert(0, int(array[h]))
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