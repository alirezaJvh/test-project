from dataloader import DatasetLoader, CategoriesSampler
from utils.types import LearningPhase
from torch.utils.data import DataLoader
import torch

# dataset = DatasetLoader(LearningPhase.TRAIN, './data/mini')

# sampler = CategoriesSampler(dataset.label, 8, 5, 1)

# loader = DataLoader(dataset=dataset, batch_sampler=sampler, num_workers= 2, pin_memory=True)

# x = torch.ones(5, requires_grad = True)
# y = x**2
# w = x.clone().detach()
# z = w**3

# r = (y+z).sum()
# r.backward()

# print(x.grad)