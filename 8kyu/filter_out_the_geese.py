"""
Write a function, gooseFilter / goose-filter / goose_filter / GooseFilter, that takes an array of strings as an argument and returns a filtered array containing the same elements but with the 'geese' removed.

The geese are any strings in the following array, which is pre-populated in your solution:

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
For example, if this array were passed as an argument:

["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]
Your function would return the following array:

["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
"""
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    for i in geese:
        print(i)
        if i in birds:
            birds.remove(i)
    return birds
  
# other user's solution
geese = {"African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"}
def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]
