def square_digits(num):
    nl = "".join([str(int(i)**2) for i in str(num)])
    nl = int(nl)
    return(nl)
    print(type(nl))

def square_digits(num):
    nl = ""
    for i in str(num):
        nl = nl + (str(int(i)**2))
    print(nl)

square_digits(9119)
