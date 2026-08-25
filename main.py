#The population of interest is 10,000 Australian Shepherd puppies. Let's see what proportion of Aussie dogs have blue eyes and what proportion is hazel (assuming these are the only two eye colours they can have which is not true in reality). Let's assume I was able to find 20 puppies to participate in an experiment as our sample. The blue-eyed proportion (proportion is the mean of 0, 1 values) in those 30 puppies is our statistic. Simulate the sample and explain what you understand from it. Here is the sample - [0,1,0,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1] Here 1 represents the puppies with blue eyes, and 0 represents the puppies with hazel eyes.
blue = 14
hazel = 6
total = 20
prob1 = blue/total
prob2 = hazel/total
print(f"The prob of blue eyed puppies is {prob1}")
print(f"The prob of hazel eyed puppies is {prob2}")
