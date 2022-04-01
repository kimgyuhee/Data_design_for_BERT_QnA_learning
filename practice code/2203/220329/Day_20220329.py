import csv

f = open('C:\\Users\\gyuhee\\Documents\\GitHub\Data_design_for_BERT_QnA_learning\\practice code\\220329\\subwayfee.csv')
# f = open('subwayfee.csv')
data = csv.reader(f)
subway_header = next(data)
subway_lines = []
for _ in data :
    info = next(data)
    subway_line = info[1]
    if subway_line not in subway_lines :
        subway_lines.append(subway_line)

print(subway_lines)
"""
for i in data :
    print(i)
"""

f.close()