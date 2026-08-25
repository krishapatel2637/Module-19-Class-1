#The population of interest is 10,000 Australian Shepherd puppies. Let's see what proportion of Aussie dogs have blue eyes and what proportion is hazel (assuming these are the only two eye colours they can have which is not true in reality). Let's assume I was able to find 20 puppies to participate in an experiment as our sample. The blue-eyed proportion (proportion is the mean of 0, 1 values) in those 30 puppies is our statistic. Simulate the sample and explain what you understand from it. Here is the sample - [0,1,0,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1] Here 1 represents the puppies with blue eyes, and 0 represents the puppies with hazel eyes.
import numpy as np
puppies = np.array([0,1,0,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1])
p = puppies.mean()
print(f"The mean value is {p}")
sd = puppies.std()
print(f"The standard deviation is {sd}")
print(f"The variance is {puppies.var()}")
np.random.choice(puppies, size=(1,5), replace=True)
np.random.choice(puppies, size=(1,5), replace=True).mean()
print("Sample distribution of size 5 is: ")
sample_prob=[]
for i in range(10000):
    sample = np.random.choice(puppies, 5, replace=True)
    sample_prob.append(sample.mean())
sample_prob = np.array(sample_prob)
print(f"The mean of new list is {sample_prob.mean()}")
print(f"The standard deviation of new list is {sample_prob.std()}")
print(f"The variance of new list is {sample_prob.var()}")