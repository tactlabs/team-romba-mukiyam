'''
Created on 

Course work: 

@author: raja

Source:


Pip:
    deepdiff
'''

# Import necessary modules
import json
from deepdiff import DeepDiff

def load(filename):
    
    data = None
    with open(filename) as local_file:
        data = json.load(local_file)

    return data

def save(filename, data):

    print(f"..saving {filename}")
    
    with open(f"results/{filename}", 'w') as file_obj:
        file_obj.write(data)

    print("..saved")

compare_config = {

    # exclude_regex_paths={r"root\[\d+\]\['b'\]"}))
    
    'ignore_order': True,
    'exclude_paths': [
        "root['data']['id']",
        # "root['data']['avatar']",
    ]
}

def compare_single_json(file_1_path, file_2_path, result_filepath):

    data1 = load(file_1_path)
    data2 = load(file_2_path)

    result = DeepDiff(data1, data2, **compare_config).pretty()

    # print(result)

    save(result_filepath, result)


def compare_local_data(product_list):

    for item in product_list:
        print(item)

        vendor_1_filename = str(item) + '-vendor1.json'
        vendor_2_filename = str(item) + '-vendor2.json'

        result_filepath = str(item) + '.txt'

        compare_single_json(vendor_1_filename, vendor_2_filename, result_filepath)


def startpy():

    product_list = [
        "10001"
    ]
    
    compare_local_data(product_list)


if __name__ == '__main__':
    startpy()

