n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
    result = ""
    for i in range(0,len(words)):
        result = result + words[i]
    return result


print join_strings(n)
print "Hello" + "World"