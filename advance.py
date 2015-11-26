import time
from dtw import DTW
from file import File

__author__ = 'phizaz'

def normal_sym_fn(A, B):
    return DTW.dist_damn_adv(A, B,
                      [ (0, -1),
                        (-1, -1),
                        (-1, 0) ],
                      [ [1],
                        [2],
                        [1] ])

def normal_asym_fn(A, B):
    return DTW.dist_damn_adv(A, B,
                      [ (0, -1),
                        (-1, -1),
                        (-1, 0) ],
                      [ [1],
                        [1],
                        [1] ])

def half_sym_fn(A, B):
    return DTW.dist_damn_adv(A, B,
                      [ (-1, -3),
                        (-1, -2),
                        (-1, -1),
                        (-2, -1),
                        (-3, -1), ],
                      [ [2, 1, 1],
                        [2, 1],
                        [2],
                        [2, 1],
                        [2, 1, 1] ])

def half_asym_fn(A, B):
    return DTW.dist_damn_adv(A, B,
                      [ (-1, -3),
                        (-1, -2),
                        (-1, -1),
                        (-2, -1),
                        (-3, -1), ],
                      [ [1/3, 1/3, 1/3],
                        [1/2, 1/2],
                        [1],
                        [1, 1],
                        [1, 1, 1] ])

def one_sym_fn(A, B):
    return DTW.dist_damn_adv(A, B,
                      [ (-1, -2),
                        (-1, -1),
                        (-2, -1), ],
                      [ [2, 1],
                        [2],
                        [2, 1] ])

def one_asym_fn(A, B):
    return DTW.dist_damn_adv(A, B,
                      [ (-1, -2),
                        (-1, -1),
                        (-2, -1), ],
                      [ [1/2, 1/2],
                        [1],
                        [1, 1] ])

def two_sym_fn(A, B):
    return DTW.dist_damn_adv(A, B,
                      [ (-2, -3),
                        (-1, -1),
                        (-3, -2), ],
                      [ [2, 2, 1],
                        [2],
                        [2, 2, 1] ])

def two_asym_fn(A, B):
    return DTW.dist_damn_adv(A, B,
                      [ (-2, -3),
                        (-1, -1),
                        (-3, -2), ],
                      [ [2/3, 2/3, 2/3],
                        [1],
                        [1, 1, 1] ])


jobs = [
    # {
    #     'title': 'Coffee.P=0.sym',
    #     'train': File.open_with_label('Coffee_TRAIN'),
    #     'test': File.open_with_label('Coffee_TEST'),
    #     'fn': normal_sym_fn,
    # },
    # {
    #     'title': 'Coffee.P=0.asym',
    #     'train': File.open_with_label('Coffee_TRAIN'),
    #     'test': File.open_with_label('Coffee_TEST'),
    #     'fn': normal_asym_fn,
    # },
    {
        'title': 'Coffee.P=0.5.sym',
        'train': File.open_with_label('Coffee_TRAIN'),
        'test': File.open_with_label('Coffee_TEST'),
        'fn': half_sym_fn,
    },
    {
        'title': 'Coffee.P=0.5.asym',
        'train': File.open_with_label('Coffee_TRAIN'),
        'test': File.open_with_label('Coffee_TEST'),
        'fn': half_asym_fn,
    },

    {
        'title': 'Coffee.P=1.sym',
        'train': File.open_with_label('Coffee_TRAIN'),
        'test': File.open_with_label('Coffee_TEST'),
        'fn': one_sym_fn,
    },
    {
        'title': 'Coffee.P=1.asym',
        'train': File.open_with_label('Coffee_TRAIN'),
        'test': File.open_with_label('Coffee_TEST'),
        'fn': one_asym_fn,
    },

    {
        'title': 'Coffee.P=2.sym',
        'train': File.open_with_label('Coffee_TRAIN'),
        'test': File.open_with_label('Coffee_TEST'),
        'fn': two_sym_fn,
    },
    {
        'title': 'Coffee.P=2.asym',
        'train': File.open_with_label('Coffee_TRAIN'),
        'test': File.open_with_label('Coffee_TEST'),
        'fn': two_asym_fn,
    },
]

for i, job in enumerate(jobs):
    print('job:', i, 'of', len(jobs))
    print('job:', job['title'])

    result = {
        'title': job['title'],
        'mode': 'P=0',
    }

    start_time = time.process_time()

    accuracy, correctness = \
        DTW.predict_list(
            job['train'],
            job['test'],
            job['fn'])

    end_time = time.process_time()

    result['accuracy'] = accuracy
    result['correctness'] = correctness
    result['total'] = len(job['test'])
    result['time_elapsed'] = end_time - start_time

    File.write_json(job['title'] + '.json', result)

