import csv
import json

__author__ = 'phizaz'

class File:

    @staticmethod
    def open(file):
        with open(file, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            result = []
            for row in spamreader:
                new_row = []
                result.append(new_row)

                for col in row:
                    new_row.append(float(col))

            return result

    @staticmethod
    def open_with_label(file):
        arr = File.open(file)

        result = []
        for each in arr:
            result.append({
                "label": each[0],
                "data": each[1:]
            })
        return result

    @staticmethod
    def open_json(file):
        with open(file) as file:
            return json.load(file)

    @staticmethod
    def write_json(file, thing):
        with open(file, 'w') as outfile:
            json.dump(thing, outfile)