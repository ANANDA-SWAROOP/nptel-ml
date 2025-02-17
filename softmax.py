import math

logits = [5,2,3]

sum = 0
for i in logits:
    sum+=(math.exp(i))
for i in logits:
    print(math.exp(i)/sum)
