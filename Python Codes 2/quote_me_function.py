# quote_me() Function
def quote_me(sentnc):
    if sentnc.startswith("\""):
        sentnc = "'"+sentnc+"'"
    else:
        sentnc = '"'+sentnc+'"'
    return sentnc
usr_sentnc = input("Enter a sentence: ")
print(quote_me(usr_sentnc))
