# def pangrams(s):
#     s = s.lower()
#  letter s= set
#     return "pangram" if set(s.lower()) >= set("abcdefghijklmnopqrstuvwxyz") 
# else "not pangram"
def pangrams(s):
    letters = set(s.lower())
    p = set("abcdefghijklmnopqrstuvwxyz")
    if letters >= p:
        return "pangram"
    else:  
        return "not a pangram"
    
s = "Quickly pack my box with five dozen juicy green apples"
print(pangrams(s))