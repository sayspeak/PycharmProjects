import numpy as np
from sklearn.datasets import load_iris
#X, y = np.loadtxt("X_classification.txt"), np.loadtxt("y_classification.txt")
dataset = load_iris()
X = dataset.data
y = dataset.target
print("No.1\n")
print(dataset.DESCR)
n_samples, n_features = X.shape
attribute_means = X.mean(axis=0)
assert attribute_means.shape == (n_features,)
X_d = np.array(X >= attribute_means, dtype='int')
#切割出训练集和测试集
from sklearn.model_selection import train_test_split

# Set the random state to the same number to get the same results as in the book
random_state = None

X_train, X_test, y_train, y_test = train_test_split(X_d, y, random_state=random_state)
print("No.2\n")
print("There are {} training samples".format(y_train.shape))
print("There are {} testing samples".format(y_test.shape))
from collections import defaultdict
from operator import itemgetter


def train(X, y_true, feature):
    n_samples, n_features = X.shape
    assert 0 <= feature < n_features
    # Get all of the unique values that this variable has
    values = set(X[:, feature])
    # Stores the predictors array that is returned
    predictors = dict()
    errors = []
    for current_value in values:
        most_frequent_class, error = train_feature_value(X, y_true, feature, current_value)
        predictors[current_value] = most_frequent_class
        errors.append(error)
    # Compute the total error of using this feature to classify on
    total_error = sum(errors)
    return predictors, total_error
def train_feature_value(X, y_true, feature, value):
    # Create a simple dictionary to count how frequency they give certain predictions
    class_counts = defaultdict(int)
    # Iterate through each sample and count the frequency of each class/value pair
    for sample, y in zip(X, y_true):
        if sample[feature] == value:
            class_counts[y] += 1
    # Now get the best one by sorting (highest first) and choosing the first item
    sorted_class_counts = sorted(class_counts.items(), key=itemgetter(1), reverse=True)
    most_frequent_class = sorted_class_counts[0][0]
    # The error is the number of samples that do not classify as the most frequent class
    # *and* have the feature value.
    n_samples = X.shape[1]
    error = sum([class_count for class_value, class_count in class_counts.items()
                 if class_value != most_frequent_class])
    return most_frequent_class, error
all_predictors = {variable: train(X_train, y_train, variable) for variable in range(X_train.shape[1])}
errors = {variable: error for variable, (mapping, error) in all_predictors.items()}
# Now choose the best and save that as "model"
# Sort by error
best_variable, best_error = sorted(errors.items(), key=itemgetter(1))[0]
print("No.3\n")
print("The best model is based on variable {0} and has error {1:.2f}".format(best_variable, best_error))

# Choose the bset model
model = {'variable': best_variable,
         'predictor': all_predictors[best_variable][0]}
print("No.4\n")
print(model)
def predict(X_test, model):
    variable = model['variable']
    predictor = model['predictor']
    y_predicted = np.array([predictor[int(sample[variable])] for sample in X_test])
    return y_predicted
y_predicted = predict(X_test, model)
print("No.5")
print(y_predicted)
accuracy = np.mean(y_predicted == y_test) * 100
print("No.6\n")
print("The test accuracy is {:.1f}%".format(accuracy))
from sklearn.metrics import classification_report
print("No.7\n")
print(classification_report(y_test, y_predicted))