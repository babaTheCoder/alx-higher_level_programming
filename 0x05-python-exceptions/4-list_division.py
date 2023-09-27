#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = [0] * list_length

    try:
        for i in range(list_length):
            try:
                num1 = my_list_1[i]
                num2 = my_list_2[i]
            except IndexError:
                print("out of range")
                continue

            if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
                print("wrong type")
                continue

            try:
                new_list[i] = num1/num2
            except ZeroDivisionError:
                print("division by 0")
    except Exception as e:
        print(e)

    finally:
        return new_list
