import torch
import torch.nn.functional as F

input = torch.tensor([[1, 2, 0, 3, 1],
                      [0, 1, 2, 3, 1],
                      [1, 2, 1, 0, 0],
                      [5, 2, 3, 1, 1],
                      [2, 1, 0, 1, 1]])
weight = torch.tensor([[1,2,1],
                       [0,1,0],
                       [2,1,0]
                       ])

print(input.size())
print(weight.size())

input = torch.reshape(input, (1,1,5,5))
weight = torch.reshape(weight, (1,1,3,3))

print(input.size())
print(weight.size())

conv2_out =  F.conv2d(input=input, weight=weight, stride=1)


print(conv2_out)
print(conv2_out.size())
conv2_out2 =  F.conv2d(input=input, weight=weight, stride=2)

print(conv2_out2)
print(conv2_out2.size())


conv2_out3 =  F.conv2d(input=input, weight=weight, stride=1,padding=1)

print(conv2_out3)
print(conv2_out3.size())

