import json

DATA_FILE = "/Users/leizhang/Downloads/food.tsv"
OUT_FILE = "/Users/leizhang/Downloads/ret.json"

ret_json = {'n': 'root', 's': []}
split_flag = '\t'
"""
input:

lingxia,yinchuan,xinqin
lingxia,yinchuan,xixia
lingxia,yinchuan,jinfeng
lingxia,yinchuan,yongling
lingxia,yinchuan,helan
lingxia,n2ndzuishan,dawukou 
lingxia,n2ndzuishan,huinong
lingxia,n2ndzuishan,pinluo
lingxia,wuzhong,litong
lingxia,wuzhong,hongsibao


output:

{'n':'china', 
 's': [
    //index1
    {'n':'lingxia', 
     's': [
        //index2
        {
            'n':'yinchuan',
            's': [
                //index3
                {
                    'n':'xinqin',
                }
            ]
        }
     ]}
    ]}
"""


def check_exist(str1, l1):
    i = 0
    index = -1
    if isinstance(l1, list):
        for i in xrange(len(l1)):
            if l1[i]['n'] == str1:
                index = i
    return index


with open(OUT_FILE, 'w') as outfile, open(DATA_FILE, 'r') as infile:
    for line in infile:
        line = line.strip()
        n1st = n2nd = n3rd = ''
        n1st = line.split(split_flag)[0]
        n2nd = line.split(split_flag)[1]
        n3rd = line.split(split_flag)[2]
        n3rd_value = line.split(split_flag)[3]

        if  n1st and  n2nd and n3rd and n3rd_value:
            index1 = check_exist(n1st, ret_json['s'])
            if index1 != -1:
                index2 = check_exist(n2nd, ret_json['s'][index1])
                if index2 != -1:
                    index3 = check_exist(n3rd, ret_json['s'][index1]['s'][index2])
                    if index3 != -1:
                        pass  # n1st, n2nd, n3rd all exist, repeat data
                    else:  # n1st n2nd, exist, n3rd not exist.
                        n3rd_node = {'n': n3rd, 'v': n3rd_value}
                        ret_json['s'][index1]['s'][index2]['s'].append(n3rd_node)

                else:  # n1st exist; n2nd, n3rd not exist.
                    n3rd_node = {'n': n3rd, 'v': n3rd_value}
                    n2nd_node = {'n': n2nd, 's': []}
                    n2nd_node['s'].append(n3rd_node)
                    ret_json['s'][index1]['s'].append(n2nd_node)
            else:  # n1st, n2nd, n3rd all not exist.
                n3rd_node = {'n': n3rd, 'v': n3rd_value}
                n2nd_node = {'n': n2nd, 's': []}
                n2nd_node['s'].append(n3rd_node)
                n1st_node = {'n': n1st, 's': []}
                n1st_node['s'].append(n2nd_node)
                ret_json['s'].append(n1st_node)
    ret_json = json.dumps(ret_json, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ':'))
    print ret_json
    outfile.write(ret_json)