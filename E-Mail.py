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
               