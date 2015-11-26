import time
from dtw import DTW
from file import File

__author__ = 'phizaz'

jobs = [
    {
        'title': 'Coffee',
        'train': File.open_with_label('Coffee_TRAIN'),
        'test': File.open_with_label('Coffee_TEST')
    },
    {
        'title': 'Beef',
        'train': File.open_with_label('Beef_TRAIN'),
        'test': File.open_with_label('Beef_TEST')
    }
]

for i, job in enumerate(jobs):
    print('job:', i, 'of', len(jobs))
    print('job:', job['title'])

    results = {
        'title': job['title'],
        'results': [],
    }

    start_time = time.process_time()

    for a in range(1, 2):
        print('a:', a)
        for b in range(1, 2):
            print('b:', b)
            for c in range(1, 2):

                abc = [a, b, c]
                zeros = abc.count(0)

                if zeros == 3:
                    continue

                if zeros == 2:
                    if b == 0:
                        continue

                print('c:', c)

                start_time = time.process_time()

                accuracy, correctness = DTW.predict_list(job['train'], job['test'])

                print('[', a, b, c, ']', 'accuracy:', accuracy, 'correctness:', correctness)

                end_time = time.process_time()
                time_elasped = end_time - start_time
                print('time_elapsed:', time_elasped)

                result = {
                    'a': a,
                    'b': b,
                    'c': c,
                    'accuracy': accuracy,
                    'correctness': correctness,
                    'total': len(job['test']),
                    'time_elapsed': time_elasped
                }

                results['results'].append(result)

    end_time = time.process_time()

    results['time_elapsed'] = end_time - start_time

    File.write_json(job['title'] + '.json', results)

