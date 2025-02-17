import math

truths = [1,0,1,1,0]
preds = [0.9,0.2,0.8,0.95,0.1]

#binary cross entropy

n = len(truths)
sum = 0

for i in range(n):
    sum+=(truths[i]*math.log(preds[i]))
    sum+=((1-truths[i])*(math.log(1-preds[i])))
print(sum/n)
