email = input("ENTER YOUR EMAIL : ")

k = j = d = 0

if len(email) >= 7:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if email[-4] == "." or email[-3] == ".":
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        continue
                    elif i.isdigit():
                        continue
                    elif i in ["_", ".", "@"]:
                        continue
                    else:
                        d = 1

                if k == 1 or d == 1:
                    print("Wrong Email ")
                else:
                    print("Valid Email ")
            else:
                print("Wrong Email : dot position ")
        else:
            print("Wrong Email : @ issue ")
    else:
        print("Wrong Email : first character ")
else:
    print("Wrong Email : length ")
