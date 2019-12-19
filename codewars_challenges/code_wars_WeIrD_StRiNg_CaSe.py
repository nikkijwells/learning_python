def to_weird_case(string):
    new_string = ""
    i = 0
    counter = 0
    for i in string:
        if i == " ":
            new_string = new_string + " "
            counter = 0
            continue
        if counter % 2 == 0:
            new_string = new_string + i.upper()
            counter = counter + 1
        elif counter % 2 != 0:
            new_string = new_string + i.lower()
            counter = counter + 1
        else:
            new_string =+ " "
            counter = counter + 1
    return new_string



to_weird_case('is')
to_weird_case('This')
to_weird_case('This is a test')
