import csv
import os
import numpy
import sys
import numpy as np
from collections import OrderedDict

def find_feature():
    diction = {}
    with open(path_to_input_basket_file, mode='r') as basket_file:
        reader=csv.reader(basket_file, delimiter=',')
        for row in reader:
            for i in range(2, len(row)):
                try:
                    feature = row[-1-i].split(':')[1].split('=')[0]
                except:
                    feature = row[-1-i].split('=')[0].lower()
                try:
                    val = int(row[-1-i].split(':')[1].split('=')[1])
                except:
                    val = 1
                if feature in diction:
                    diction[feature] += val
                else:
                    diction[feature] = val
    return diction

def get_top_n():
    top_n = []
    count = 0;
    for key, val in features_dict.items():
        top_n.append(key)
        count+=1
        if count==top_n_features_to_extract:
            break
    return top_n

def make_header(vector):
    with open(path_to_output_vector_file, encoding='utf8', mode='w', newline='') as out_file:
        writer = csv.writer(out_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        SS = vector + ['section', 'source']
        writer.writerow(SS)
        num_col = len(SS)
        r1 = ['d' for i in range(num_col)]
        writer.writerow(r1)
        r2 = ['' for i in range(num_col-2)] + ['c', 'm']
        writer.writerow(r2)

def write_vector(vector):
    with open(path_to_input_basket_file, mode='r') as basket_file:
        reader=csv.reader(basket_file, delimiter=',')
        with open(path_to_output_vector_file, encoding='utf8', mode='a', newline='') as out_file:
            writer = csv.writer(out_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                write_val = []
                dit = {}
                for i in range(2, len(row)):
                    try:
                        feature = row[-1-i].split(':')[1].split('=')[0]
                    except:
                        feature = row[-1-i].split('=')[0].lower()
                    try:
                        val = int(row[-1-i].split(':')[1].split('=')[1])
                    except:
                        val = 1
                    dit[feature] = val
                for e in vector:
                    if e in dit:
                        write_val.append(dit[e])
                    else:
                        write_val.append(0)
                write_val.append(row[-2].replace(' ','').split('=')[0])
                write_val.append(row[-1].replace(' ','').split('=')[0])
                writer.writerow(write_val)

if __name__=='__main__':
    path_to_input_basket_file = sys.argv[1]
    path_to_output_vector_file = sys.argv[2]
    top_n_features_to_extract = int(sys.argv[3])

    features_dict = find_feature()
    features_dict = OrderedDict(sorted(features_dict.items(), key=lambda x: x[1], reverse=True))
    #print (features_dict)
    vector = get_top_n()
    print(vector)
    make_header(vector)
    write_vector(vector)
