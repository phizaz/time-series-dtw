import csv
import numpy
from dtw import DTW
from file import File

__author__ = 'phizaz'

# open training files
training = File.open('Coffee_TRAIN')

training_with_label = []
for each in training:
    training_with_label.append({
        "label": each[0],
        "data": each[1:]
    })

# open testing file
testing = File.open('Coffee_TEST')

result = {
    'title': 'Coffee',
}

# using Euclidean
print('using Euclidean...')
correctness = 0
for i, each in enumerate(testing):
    print(i, "of", len(testing))

    label = each[0]
    data = each[1:]

    min_dist = float('Inf')
    min_pos = -1

    for j, candidate in enumerate(training_with_label):
        dist = DTW.euclid_dist(data, candidate['data'])

        if dist < min_dist:
            min_dist = dist
            min_pos = j

    predicted = training_with_label[min_pos]['label']

    if predicted == label:
        correctness += 1

    print('min_dist:', min_dist)
    print('min_pos:', min_pos)
    print('predicted label:', predicted)
    print('actual label:', label)

print('correctness:', correctness)
print('accuracy:', correctness / len(testing) * 100)

result['euclid'] = {
    "correctness": correctness,
    "total": len(testing),
    'accuracy': correctness / len(testing) * 100
}

# using DTW
print('using DTW')
correctness = 0
for i, each in enumerate(testing):
    print(i, "of", len(testing))

    label = each[0]
    data = each[1:]

    min_dist = float('Inf')
    min_pos = -1

    for j, candidate in enumerate(training_with_label):
        dist = DTW.dist(data, candidate['data'])

        if dist < min_dist:
            min_dist = dist
            min_pos = j

    predicted = training_with_label[min_pos]['label']

    if predicted == label:
        correctness += 1

    print('min_dist:', min_dist)
    print('min_pos:', min_pos)
    print('predicted label:', predicted)
    print('actual label:', label)

print('correctness:', correctness)
print('accuracy:', correctness / len(testing) * 100)

result['dtw'] = {
    "correctness": correctness,
    "total": len(testing),
    'accuracy': correctness / len(testing) * 100
}

# write to file
File.write_json('Coffee.json', result)

