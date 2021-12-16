def add(x, y):
    sum = x + y
    return sum

if __name__ == "__main__":
    x = input("Enter your first number: ")
    y = input("Enter your second number: ")
    
    z = add(x, y)
    import pdb; pdb.set_trace()
    print(z)

# NOTE: if do not put int() function to type cast the input, it returns wrong sum. Use pdb to do that debugging
# When you run the codebase, pdb is shown like a virtual env terminal only when the code reaches that execution, and
# then stops at that point. Do help and hit enter- it shows all commands. help command_name gives info about that command
# q or quit to get out of the pdb