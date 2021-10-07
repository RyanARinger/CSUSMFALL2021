import re

def tinyPieLexer(code):
    print()
    outputList = []
    tempLit = ""

    while len(code) != 0:
        # first remove all whitespaces

        search = re.search(r'\s', code)
        # print(search)
        if search != None:
            code = re.sub(search.group(), '', code)

        # now check each possible token type
        # keyword
        # print(code)
        search = re.search(r'if|else|int|float', code)

        while search != None:
            outputList.append(opFormat("kywrd", search.group()))
            code = re.sub(search.group(), '', code, 1)
            search = re.search(r'if|else|int|float', code)

        # operator
        # print(code)
        search = re.search(r'\=|\+|\<|\>|\*', code)
        while search != None:
            outputList.append(opFormat("oprtr", search.group()))
            code = re.sub(r'\=|\+|\<|\>|\*','',code,1)
            search = re.search(r'\=|\+|\<|\>|\*', code)

        # separator
        search = re.search(r'[\(\)\:\"\;]', code)
        # print(search)
        while search != None:

            # kill the string literal while we're here
            if search.group() == '"':
                outputList.append(opFormat("sprtr", search.group()))
                code = re.sub(search.group(), '', code, 1)
                done = False
                templit = ""
                i = search.start()
                while not done:

                    if i < len(code) and code[i] != '"':
                        templit = templit + str(code[i])
                        i = i+1
                    else:
                        outputList.append(opFormat("ltrl", templit))
                        outputList.append(opFormat("sprtr", search.group()))
                        code = re.sub(templit, '', code, 1)
                        code = re.sub(search.group(), '', code, 1)
                        done = True

            outputList.append(opFormat("sprtr", search.group()))
            code = re.sub(r'[\(\)\:\"\;]', '', code, 1)
            search = re.search(r'[\(\)\:\"\;]', code)

        # identifier
        search = re.search(r'[A-Za-z_][A-Za-z0-9]*', code)
        while search != None:
            outputList.append(opFormat("idtfr", search.group()))
            code = re.sub(search.group(), '', code, 1)
            search = re.search(r'[A-Za-z_][A-Za-z0-9]*', code)
        # literals
        search = re.search(r'\d+.?\d*', code)
        if search != None:
            outputList.append(opFormat("ltrl", search.group()))
            code = re.sub(r'\d+.?\d*', '', code, 1)
        break
    print(outputList)

def opFormat(type, val):
    return "<" + type + "," + val + ">"


if __name__ == '__main__':
    tinyPieLexer("int    A1=5")
    tinyPieLexer("float BBB2     =1034.2")
    tinyPieLexer("float     cresult     =     A1     +BBB2     *      BBB2")
    tinyPieLexer("if     (cresult     >10): 	print(“TinyPie    ”    )")