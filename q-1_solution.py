import csv
from collections import Counter


def problem_1():
    with open('interview_scent.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        no_of_row = 0
        distinct_val = []
        for row in reader:
            if row['predictions'] != "None":
                no_of_row += 1

            distinct_val.append(row['predictions'])

        unique_distinct_val = set(distinct_val)
        print("No of ROW = ",no_of_row)
        print("distinct values = ", unique_distinct_val)

        value_count = dict(Counter(distinct_val))
        print("count of each distinct value = ", value_count)

        with open('output_q-1.csv', 'w', newline='') as fp:
            output_file = csv.writer(fp, delimiter=',')
            data = [['No of Rows', no_of_row],
                    ['Distinct Values', unique_distinct_val],
                    ['Count of Each Distinct Value', value_count]]
            output_file.writerows(data)


problem_1()
