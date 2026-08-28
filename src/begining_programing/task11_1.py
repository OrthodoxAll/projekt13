from src import begining_programing


def filter_order_by_coast(file_iter, coast):
    raw_header = next(file_iter)
 #   print(raw_header)




with open(begining_programing/task11_11.csv, 'r') as f:
    result = filter_order_by_coast(f, 20)
print(result)