#!/usr/bin/python
# -*- coding: utf-8 -*-

from Item import ItemList, Item

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = ItemList(item_count, capacity)

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.insert(Item(i-1, int(parts[0]), int(parts[1])))

    items.heapify()
    items.DP()

#    print '-------'
#    print items.totalValue
#    print items.taken
#    print '-----'

    (value, weight, taken) = items.result()

#    print "---" + str(weight) + "---"
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

