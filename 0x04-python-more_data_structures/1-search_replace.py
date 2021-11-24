#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [h if h != search else replace for h in my_list]
    return new_list
