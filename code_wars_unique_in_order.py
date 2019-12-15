def unique_in_order(iterable):
    unique_list = []
    counter = 0
    for i in iterable:
        if counter == 0:
            unique_list.append(i)
            counter =+ 1
        elif i == unique_list[counter -1]:
            counter = counter
        else:
            unique_list.append(i)
            counter = counter + 1
            #print(unique_list)
    return unique_list

unique_in_order('AAAABBBCCDAABBB')


#counter = 0 unique_list = [A] ('A')
#counter = 1 unique_list = [A] ('AA')
#counter = 1 unique_list = [A] ('AAA')
#counter = 1 unique_list = [A] ('AAAA')
#counter = 2 unique_list = [A, B] ('AAAAB')

#BCCDAABBB
