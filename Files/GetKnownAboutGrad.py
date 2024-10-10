# 其实对梯度下降都是没有理解的，我想自己学会为什么梯度下降是有效的
# 使用y = x^2找寻最值。会不会也是最优化的原理
class SolveOptiProblem:
    # 原函数
    def function(self, x):
        return x ** 2
    # 导函数
    def derivative(self, x):
        return 2 * x
    # 实现梯度下降算法,实际上就是向实际的最值点进行移动
    def gradient_descent(self, start_x, learn_rate, num_iteration):
        x = start_x
        for i in range(num_iteration):
            # 计算当前点梯度
            grad = self.derivative(x)
            # 如果不是最值点，梯度下降方向就是向极值的方向。
            # 两侧梯度在向着极值点处减小
            x -= learn_rate * grad
            if (i % 50 == 0):
                print(f'iteration:{i}, f(x)={self.function(x)}')
        return x
    
if __name__ == '__main__':
    solver = SolveOptiProblem()
    solver.gradient_descent(100, 0.1, 500)