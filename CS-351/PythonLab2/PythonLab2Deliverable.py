import re

def regSearch(item):
    print("Testing: \"" + item + "\"")

    # An integer
    if re.search(r'^\d+$$', item) != None:
        print(item + " Matches pattern: An integer")
    else:
        print(item + " Does not match pattern: An integer")

    # A float consists of 1 or more digits before and after the decimal point
    if re.search(r"\d+\.\d+", item) != None:
        print(item + " Matches pattern: A float consists of 1 or more digits before and after the decimal point")
    else:
        print(item + " Does not match pattern: A float consists of 1 or more digits before and after the "
                     " decimal point")

    # A float with exactly 2 digits after the decimal point
    if re.search(r"\d+\.\d{2}", item) != None:
        print(item + " Matches pattern: A float with exactly 2 digits after the decimal point")
    else:
        print(item + " Does not match pattern: A float with exactly 2 digits after the decimal point")

    # A float end with letter f (4.321f)
    if re.search(r"\d+\.\d+f", item) != None:
        print(item + " Matches pattern: A float end with letter f")
    else:
        print(item + " Does not match pattern: A float end with letter f")

    # Capital letters, followed by small case letters, followed by digits
    if re.search(r"[A-Z]+[a-z]+\d+", item) != None:
        print(item + " Matches pattern: Capital letters, followed by small case letters, followed by digits")
    else:
        print(item + " Does not match pattern: Capital letters, followed by small case letters, followed by digits")

    # Exactly 3 digits, followed by at least 2 letters
    if re.search(r"\d{3}[A-z]{2,}", item) != None:
        print(item + " Matches pattern: Capital letters, followed by small case letters, followed by digits")
    else:
        print(item + " Does not match pattern: Capital letters, followed by small case letters, followed by digits")

    print()

def removeInt(item):
    index2 = 0
    print("For string: \"" + item + "\"")
    if re.search(r'^\d+$', item) != None:
        print("String " + item + " is only an integer")
    elif re.search(r'^\d.*', item):
        for i in range(len(item)):
            if re.search(r'[^0-9]', item[i]) != None:
                index2 = i
                break
        print("Found int, \"" + item[0: index2] + "\" at the begining of the string \"" + item + "\" starting at index 0 and ending at index" +
              str(index2) + ". The rest of the string is: \"" + item[index2: len(item)] + "\"")

    else:
        print("String \""+ item +"\" does not start with an integer")

    print()

if __name__ == '__main__':
    words = ['22.11','23','66.7f', '123abcde','Case44', 'Happy','78', '66.7', 'yes123','Book111']
    # rexp = ['^\d+$$', '\d+\.\d+', '\d+\.\d{2}', '\d+\.\d{2}f', '[A-Z]+[a-z]+\d+', '\d{3}[A-z]{2,}']

    print("#########################TASK 1#########################")
    print()
    for word in words:
        regSearch(word)

    print("#########################TASK 2#########################")
    print()

    removeInt("hello")
    removeInt("35165")
    removeInt("123abc")
    removeInt("what 300")
    removeInt("234 who's there")
