import numpy as np
puppies = np.array([0,1,0,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1])
sample_prob=[]
for i in range(10000):
    sample = np.random.choice(puppies, 15, replace=True)
    sample_prob.append(sample.mean())
sample_prob = np.array(sample_prob)
print(f"The mean of new list is {sample_prob.mean()}")
print(f"The standard deviation of new list is {sample_prob.std()}")
print(f"The variance of new list is {sample_prob.var()}")