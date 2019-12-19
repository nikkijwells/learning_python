def filter_list(l):
    new_list = []
    for i in l:
        if isinstance(i, int) == True:
            new_list.append(i)
    return new_list
  #'return a new list with the strings filtered out'

  #a good solution =
  #def filter_list(l):
  #return [i for i in l if not isinstance(i, str)]

filter_list([1,2,'a','b'])
filter_list([1,'a','b',0,15])
