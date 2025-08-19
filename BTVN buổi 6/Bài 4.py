def format_phone_number(phone_number):
    phone_number_new = ""

    for i in range(len(phone_number)):
        if phone_number[i].isdigit():
            phone_number_new += phone_number[i]
    if phone_number_new[0] != "0":
        return "Invalid phone number"
    if len(phone_number_new) != 10:
        return "Invalid phone number"
    return "+84 " + phone_number_new[1:]

pn = input()
print(format_phone_number(pn))