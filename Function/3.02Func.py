#number = input("give me a integer")
#while "." in number:
#    number = input("That is not a integer")
#print("yes it is a integer")


#name: safe_to_integer
#purpose: ensures an input as an integer
#input: varies (type: varies)
#output: ture or false

def safe_to_integer(a):
    try:
        int(a)
        return True
    except ValueError:
        print("that is not an integer: ")
        return False
    except:
        print("a unknown error occured")
        return False

a = input("enter a character: ")

if safe_to_integer(a) == True:
    print("Character is a Integer")
else:
    print("Character is not a Integer")