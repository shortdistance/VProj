import json

DATA_FILE = "/Users/leizhang/Downloads/food.tsv"
OUT_FILE = "/Users/leizhang/Downloads/ret.json"

foodData = {}
split_flag = '\t'
level1_num = 14
level2_num = 1000

level1_list = range(1, level1_num + 1)
level2_list = range(1, level2_num + 1)
print level1_list
print level2_list
"""
input:

Alcoholic beverage	Beer	bitter, average (<4% ABV)	30
Alcoholic beverage	Beer	bitter, best, premium	33
Alcoholic beverage	Beer	bitter, strong (>5% ABV)	42
Alcoholic beverage	Cider	dry	36
Alcoholic beverage	Cider	low alcohol	17
Alcoholic beverage	Cider	strong	68
Alcoholic beverage	Cider	sweet	42
Alcoholic beverage	Egg nog	homemade	98
Alcoholic beverage	Lager	alcohol-free	7
Alcoholic beverage	Lager	extra strong	60
Alcoholic beverage	Lager	low alcohol	16
Alcoholic beverage	Lager	premium	29
Alcoholic beverage	Lager	standard	24
Alcoholic beverage	Liqueurs	cream	305
Alcoholic beverage	Liqueurs	high strength	314
Alcoholic beverage	Liqueurs	low-medium strength	262
Alcoholic beverage	Shandy	50% lager, homemade	23
Alcoholic beverage	Shandy	bottled or canned	24
Alcoholic beverage	Sherry	medium	116
Alcoholic beverage	Spirits	40% volume	222
Alcoholic beverage	Stout	Guinness	37
Alcoholic beverage	Vermouth	dry	109
Alcoholic beverage	Wine	mulled wine, homemade	155
Alcoholic beverage	Wine	red	76
Alcoholic beverage	Wine	rose, medium	79
Alcoholic beverage	Wine	white, dry	75
Alcoholic beverage	Wine	white, medium	75
Alcoholic beverage	Wine	white, sparkling	84
Alcoholic beverage	Wine	white, sweet	94


output:

var foodData = {
    "1": {
        "name": "Vegetables and vegetable products", "cell": {
            "24": {
                "name": "Agar", "cell": {
                    "31": {"name": "canned, drained"},
                    "2": {"name": "dried, soaked and drained"}
                }
            },
            "29": {
                "name": "Ackee", "cell": {
                    "151": {"name": "canned, drained"}
                }
            },
            "58": {
                "name": "Amaranth leaves", "cell": {
                    "16": {"name": "boiled in unsalted water"},
                    "18": {"name": "raw"}
                }
            },
            "58": {
                "name": "Arrowhead", "cell": {
                    "91": {"name": "boiled in unsalted water"},
                    "107": {"name": "raw"}
                }
            }
        }
    }
    ....
}
"""


def check_str_is_value_of_subobject_of_object(str1, dict1):
    index = None
    if isinstance(dict1, dict):
        for k, v in dict1.items():
            if v['name'] == str1:
                index = k
    return index


def check_exist(str1, l1):
    i = 0
    index = -1
    if isinstance(l1, list):
        for i in xrange(len(l1)):
            if l1[i]['n'] == str1:
                index = i
    return index


with open(OUT_FILE, 'w') as outfile, open(DATA_FILE, 'r') as infile:
    i = 0
    j = 0
    global level1_list
    global level2_list
    for line in infile:
        line = line.strip()
        n1st = n2nd = n3rd = ''
        n1st = line.split(split_flag)[0]
        n2nd = line.split(split_flag)[1]
        n3rd = line.split(split_flag)[2]
        n3rd_value = line.split(split_flag)[3]
        if n1st and n2nd and n3rd and n3rd_value:
            index1 = check_str_is_value_of_subobject_of_object(n1st, foodData)
            if index1:
                index2 = check_str_is_value_of_subobject_of_object(n2nd, foodData[index1]['cell'])
                if index2:
                    index3 = check_str_is_value_of_subobject_of_object(n3rd, foodData[index1]['cell'][index2]['cell'])
                    if index3:
                        pass
                    else:
                        foodData[index1]['cell'][index2]['cell'][str(n3rd_value)] = {}
                        foodData[index1]['cell'][index2]['cell'][str(n3rd_value)]['name'] = n3rd

                else:
                    j = level2_list.pop(0)
                    foodData[index1]['cell'][str(j)] = {}
                    foodData[index1]['cell'][str(j)]['name'] = n2nd
                    foodData[index1]['cell'][str(j)]['cell'] = {}
                    foodData[index1]['cell'][str(j)]['cell'][str(n3rd_value)] = {}
                    foodData[index1]['cell'][str(j)]['cell'][str(n3rd_value)]['name'] = n3rd

            else:
                i = level1_list.pop(0)
                foodData[str(i)] = {}
                foodData[str(i)]['name'] = n1st
                foodData[str(i)]['cell'] = {}
                j = level2_list.pop(0)
                foodData[str(i)]['cell'][str(j)] = {}
                foodData[str(i)]['cell'][str(j)]['name'] = n2nd
                foodData[str(i)]['cell'][str(j)]['cell'] = {}
                foodData[str(i)]['cell'][str(j)]['cell'][str(n3rd_value)] = {}
                foodData[str(i)]['cell'][str(j)]['cell'][str(n3rd_value)]['name'] = n3rd
    foodData = json.dumps(foodData, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ':'))
    print foodData
    outfile.write(foodData)
