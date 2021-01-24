

import json
data = []

with open('/Users/abhishekmane/Downloads/YWJhbG9uZQ==') as f:
    lines = f.readlines()
    for line in lines:
        attrs = line.split(' ')
        data.append({
            'age': int(attrs[0]),
            'sex': int(attrs[1].split(':')[1]),
            'length': float(attrs[2].split(':')[1]),
            'diameter': float(attrs[3].split(':')[1]),
            'height': float(attrs[4].split(':')[1]),
            'whole.weight': float(attrs[5].split(':')[1]),
            'shucked.weight': float(attrs[6].split(':')[1]),
            'viscera.weight': float(attrs[7].split(':')[1]),
            'shell.weight': float(attrs[7].split(':')[1]),
        })


f = open('./data.json', 'w')
f.write(json.dumps(data, separators=(',', ':')))
f.close()
