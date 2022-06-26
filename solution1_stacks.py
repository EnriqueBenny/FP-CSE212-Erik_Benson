#Problem 1
problem = list()
problem.append(0)
problem.append(1)
problem.append(2)
problem.pop()
problem.pop()
problem.append(3)
problem.append(4)
problem.append(5)
problem.append(6)
problem.append(7)
problem.append(8)
problem.pop()
problem.pop()
problem.pop()
problem.append(9)
problem.append(10)
problem.append(11)
problem.append(12)
problem.pop()
problem.append(13)
problem.append(14)
problem.append(15)
problem.append(16)
problem.append(17)
problem.pop()
problem.pop()
problem.append(18)
problem.append(19)
problem.append(20)
#What will the output be? Decide before you print it.
#Solution: 
# [0, 3, 4, 5, 9, 10, 11, 13, 14, 15, 18, 19, 20]
print(problem)

#Problem 2
# We are looking for the output:
# [0, 1, 2, 3, 11, 12, 13, 14, 15, 16]
# Change the variables 'pops' to the proper value to find
# the output we are after.
problem = list()
problem.append(0)
problem.append(1)
problem.append(2)
problem.append(3)
problem.append(4)
problem.append(5)
problem.append(6)
problem.append(7)
problem.append(8)
problem.append(9)
problem.append(10)
#Change pops, will determine how many times the function pop is called.
# Solution: 7
pops = 7
for i in range(0, pops):
    problem.pop()
problem.append(11)
problem.append(12)
problem.append(13)
problem.append(14)
problem.append(15)
problem.append(16)
problem.append(17)
problem.append(18)
problem.append(19)
problem.append(20)
#Change pops, will determine how many times the function pop is called. 
# Solution: 4
pops = 4
for i in range(0, pops):
    problem.pop()
print(problem)