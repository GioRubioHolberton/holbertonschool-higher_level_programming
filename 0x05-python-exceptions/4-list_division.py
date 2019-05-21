#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = 0
    your_list = []
    for coun in range(list_length):
        try:
            res = my_list_1[coun] / my_list_2[coun]
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except TypeError:
            res = 0
            print("wrong type")
        except ValueError:
            res = 0
            print("wrong type")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            your_list.append(res)
    return your_list
