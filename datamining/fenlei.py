import numpy as np
from collections import defaultdict
valid_rules = defaultdict(int)
invalid_rules = defaultdict(int)
num_occurances = defaultdict(int)
dataset_filename = "affinity_dataset.txt"
X = np.loadtxt(dataset_filename)
for sample in X:
    for premise in range(4):
        if sample[premise] == 0: continue
        num_occurances[premise] += 1
    for conclusion in range(4):
        if premise == conclusion: continue
    if sample[conclusion] == 1:
        valid_rules[(premise,conclusion)]+=1
    else:
        invalid_rules[(premise,conclusion)]+=1
support = valid_rules
confidence = defaultdict(float)
for premise,conclusion in valid_rules.keys():
    rule = (premise,conclusion)
    confidence[rule] = valid_rules[rule]/num_occurances[premise]

def print_rule(premise,conclusion,support,confidence,features):

    premise_name = features[premise]
    conclusion_name = features[conclusion]
    print("rule: if a person buy {} they will buy {}".format(premise_name,conclusion_name))
    print("-Support: {}".format(support[(premise,conclusion)]))
    print("-Confidence: {0:.3f}".format(confidence[(premise,conclusion)]))
from operator import itemgetter
sorted_support = sorted(support.items(),key = itemgetter(1),reverse = True)
for index in range(5):
    print("rule#{}".format(index + 1))
    premise,conclusion = sorted_support[index][0]
    print_rule(premise,conclusion,support,confidence,features)
