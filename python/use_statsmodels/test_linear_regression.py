import statsmodels.api as sm

# 假设你有一组解释变量和因变量的数据
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 将解释变量转换为一个矩阵
x = sm.add_constant(x)

# 使用 OLS 方法来拟合数据
model = sm.OLS(y, x)
results = model.fit()

print(results.params[1])
# 打印结果
print("Summary: %s" % results.summary())
print(results.predict())
