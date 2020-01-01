import string

def is_pangram(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    place = 1
    for i in s:
        if i.isalpha() and s.find(i, place):
            place = place + 1
            #print(place)
            #if
            print(s.find(i, place))




                #print(i)
                #place =place + 1
                #print(place)
            #else:
                #return False
            #return True


pangram = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(pangram))
pangram = "not a panagram"
print(is_pangram(pangram))
