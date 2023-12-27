import json
import re

def identify_key(data, key_type, pattern):
    identified_keys = []

    def recursive_search(obj, current_key=''):
        if isinstance(obj, list):
            for i, item in enumerate(obj):
                recursive_search(item, current_key=f'{current_key}[{i}]')
        elif isinstance(obj, dict):
            for k, v in obj.items():
                nested_key = f'{current_key}["{k}"]' if current_key else k
                if isinstance(v, (dict, list)):
                    recursive_search(v, current_key=nested_key)
                elif isinstance(v, str) and pattern.match(v):
                    identified_keys.append((nested_key, v))

    recursive_search(data)
    return identified_keys
def validate_aadhar(aadhar):
    pattern = re.compile(r'^\d{4}[ -]?\d{4}[ -]?\d{4}$')
    return bool(pattern.match(aadhar))

def validate_pan(pan):
    pattern = re.compile(r'^[A-Z]{5}\d{4}[A-Z]{1}$')
    return bool(pattern.match(pan))

def validate_gst(gst):
    pattern = re.compile(r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[0-9A-Z]{1}[Z]{1}[0-9A-Z]{1}$')
    return bool(pattern.match(gst))


json_file_path = 'C:/Users/jain vinit/Documents/Python/test2.json'

with open(json_file_path, 'r') as file:
  
    data = json.load(file)

aadhar_keys = identify_key(data, 'Aadhar', re.compile(r'^\d{4}[ -]?\d{4}[ -]?\d{4}$'))
pan_keys = identify_key(data, 'PAN', re.compile(r'^[A-Z]{5}\d{4}[A-Z]{1}$'))
gst_keys = identify_key(data, 'GST', re.compile(r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[0-9A-Z]{1}[Z]{1}[0-9A-Z]{1}$'))


print("Keys containing Aadhar numbers:")
for key, value in aadhar_keys:
    print(f"{key}: {value} is valid")

print("\nKeys containing PAN numbers:")
for key, value in pan_keys:
    print(f"{key}: {value} is valid")

print("\nKeys containing GST numbers:")
for key, value in gst_keys:
    print(f"{key}: {value} is valid") 

#20440 function calls (19019 primitive calls) in 0.101 seconds   test2  used recusive
#9968 function calls (9453 primitive calls) in 0.059 seconds     test