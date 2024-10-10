# 目标 通过梯度下降算法，求取函数 f(x) = x^2 - 2x + 4的极值点和最小函数值
# 给出目标函数
# 给出目标函数的一阶导函数
# 设置初始位置，设置步长，设置迭代次数
import random

class Slover:
    def function(self, x):
        return x ** 2 - 4 * x + 4
    
    def grad(self, x):
        return 2 * x - 4
    
    def grad_descent(self, start_x, learn_rate, iteration):
        x = start_x
        for i in range(iteration):
            x -= learn_rate * self.grad(x)
            if ((i % 20) == 0):
                print(f'iteartion:{i}, function={self.function(x)}')
        return x
    
if __name__ == '__main__':
    ss = Slover()
    res = ss.grad_descent(random.randint(200, 500), 0.1, 500)
    print(res)