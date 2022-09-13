from sklearn.multiclass import OneVsOneClassifier
import torch
import numpy as np

### 张量生成
data = [[1,2],[3,4]]

# 直接生成
x_data = torch.tensor(data)

# Numpy数组生成
np_array = np.array(data)
x_np = torch.from_numpy(np_array)

# 既有数据生成
shape = (2,3,)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zero_(shape)

# 既有张量生成
x_int = torch.ones_like(x_data)
x_float = torch.rand_like(x_data,dtype=torch.float)

