import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pareto

shape = 3.0
scale = 1.0
size = 1000

#生成采样数据
samples = pareto.rvs(shape,scale=scale,size=size)

#计算分布函数的概率密度函数
x = np.linspace(pareto.ppf(0.01,shape,scale=scale),
                pareto.ppf(0.99,shape,scale=scale),100)
pdf = pareto.pdf(x,shape,scale=scale)
#绘制概率密度函数曲线
plt.plot(x,pdf,'r-',lw=2,alpha=0.6,label='pdf')

plt.show()