import sys
import numpy as np
import pandas as pd

def check_value(v1, v2):
    return v1.equals(v2)

def check_shape(v1, v2):
    r1 = v1.values[0].tolist()==v2.values[0].tolist()
    r2 = v1.values[1].tolist()==v2.values[1].tolist()
    if (r1 and r2):
        return (v1.shape == v2.shape)
    return False

def main(v1, v2):
    if not check_shape(v1, v2):
        print ('wrong format-shape, False vector')
    else:
        columns = list(v1.columns.values)
        v1 = v1.sort_values(columns, ascending=False)
        try:
            v2 = v2[columns]
            v2 = v2.sort_values(columns, ascending=False)
            
            v1.to_csv('temp1.tsv', index=False, sep='\t')
            v2.to_csv('temp2.tsv', index=False, sep='\t')
            v1 = pd.read_csv('temp1.tsv', sep='\t')
            v2 = pd.read_csv('temp2.tsv', sep='\t')
            
            if check_value(v1, v2):
                print ('True vector')
            else:
                print ('wrong contents, False vector')
        except:
            print ('wrong feature columns, False vector')

if __name__=='__main__':
    path_to_verified_vector_file = sys.argv[1]
    path_to_test_vector_file = sys.argv[2]
    vect1_data = pd.read_csv(path_to_verified_vector_file, sep='\t')
    vect2_data = pd.read_csv(path_to_test_vector_file, sep='\t')
    main(vect1_data, vect2_data)