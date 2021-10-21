import timeit
print ("The Following will print the timeit result of running the following code (timeit.timeit('import random;random.sample(range(100),5)'))")
print()
print("the Time Taken is...")
print()
print (timeit.timeit('import random;random.sample(range(100),5)'))


    