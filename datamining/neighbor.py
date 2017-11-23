import os
import numpy as np
import csv
#同data文件夹路径。数据集所在的文件夹名称和数据集名称组合成数据集文件的完整路径
data_filename = os.path.join("/Users/apple/PycharmProjects/datamining/ionosphere.data")
#创建Numpy数组x，y存放数据集。数据集大小已知为351行34列
X = np.zeros((351,34),dtype='float')
y = np.zeros((351,),dtype='bool')
#数据集文件存储为csv，这是常用的数据集存储格式，用csv模块来导入数据集文件，并创建csv阅读器对象
with open(data_filename,'r') as input_file:
    reader = csv.reader(input_file)
    #遍历文件中的每一行数据。每行数据代表一组测量结果，可以将其称为数据集中的一个个体。枚举函数来获得每行的索引号
    for i, row in enumerate(reader):
        #获取每个个体的前34个值，将其强制转换为浮点型，保存到X中
        data = [float(datum) for datum in row [:-1]]
        X[i] = data
        #获取每个个体的类别的值，把字母转化成数字，假如类别是"g"，值为1，否则为0
        y[i] = row[-1] == 'g'
        #到此为止就把数据集读到了数组y中
#创建测试集和训练集，倒入库
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=14)
#调用近邻估计器
from sklearn.neighbors import KNeighborsClassifier
estimator = KNeighborsClassifier()
#创建好估计器之后对训练数据进行训练，比较待分类的新数据点和训练集中的数据，找到新数据点的近邻
estimator.fit(X_train,y_train)
#接着用测试集测试算法，评估测试集表现
y_predicted = estimator.predict(X_test)
accuracy = np.mean(y_test == y_predicted) * 100
print("the accuracy is {0:1f}%".format(accuracy))

#切分多个数据集，并保证每次切割得到的训练集和测试集都不一样从而，优化，即"交叉检验"
from sklearn.model_selection import cross_val_score
#传输两个完整的数据集和类别值
scores = cross_val_score(estimator,X,y,scoring='accuracy')
average_accuracy = np.mean(scores) * 100
print("the average accuracy is {0:.1f}%".format(average_accuracy))
avg_scores = []
all_scores = []
parameter_values = list(range(1,21))
for n_neighbors in parameter_values:
    estimator = KNeighborsClassifier(n_neighbors=n_neighbors)
    scores = cross_val_score(estimator,X,y,scoring='accuracy')
    avg_scores.append(np.mean(scores))
    all_scores.append(scores)
from matplotlib import pyplot as plt
plt.plot(parameter_values,avg_scores,'-o')
plt.show()