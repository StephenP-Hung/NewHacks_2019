import torch 

x = torch.ones(2, 2, requires_grad=True)
print(x)

y = x + 4
print(y)

print(y.requires_grad)