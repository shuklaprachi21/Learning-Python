def distance_from_zero(a):
    if(type(a)==type(1) or type(a)==type(1.5)):
        return abs(a)
    else:
        return "Nope"

print distance_from_zero("Hi")
print distance_from_zero(-1)
print distance_from_zero(-2.6)