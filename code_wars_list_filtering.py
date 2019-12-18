def filter_list(l):
    new_list = []
    for i in l:
        if isinstance(i, int) == True:
            new_list.append(i)
            print(i)
    return new_list
  #'return a new list with the strings filtered out'

filter_list([1,2,'a','b'])
filter_list([1,'a','b',0,15])
