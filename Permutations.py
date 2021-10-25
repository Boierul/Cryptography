# Measure the time of program execution
import time
start_time = time.time()

from itertools import permutations
# A list of some numbers
myList = [1,2,3,4,5,6,7]

# Creating a var to store all the permutations of myList
listOfPermutations = permutations(myList)
counter = 0
for permutation in listOfPermutations:
    counter += 1
    print(permutation)
print(len(myList),counter)

# Measure time (continuation)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
