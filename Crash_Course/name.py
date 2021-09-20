def names(fname, lname):
    return f"{fname.title()} {lname.title()}"

# print(names("nabin", "Niroula"))

def profession(*jobs):   # asterisk makes jobs a tuple
    return jobs

prof1 = profession("Engineering")
# print(prof1)
prof2 = profession("Teaching")
# print(prof2)

