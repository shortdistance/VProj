import time
from functools import wraps

DATA_FILE = "/Users/leizhang/Downloads/UK_House_Price_paid_data/pp-complete.csv"
OUT_FILE1 = "/Users/leizhang/Downloads/ret1.log"
OUT_FILE2 = "/Users/leizhang/Downloads/ret2.log"
Summary = {}
count_without_post_code1 = 0
count_without_post_code2 = 0

def analyseLinebyyear(Summary, line):
    global count_without_post_code1
    line = line.replace('"', '')
    line = line.strip()
    price = line.split(',')[1]
    transaction_date = line.split(',')[2]
    date_year = transaction_date.split('-')[0]

    post_code = line.split(',')[3]
    if not post_code:
        count_without_post_code1 +=1
        return
    outward_code = post_code.split(' ')[0]

    # D = Detached, S = Semi-Detached, T = Terraced, F = Flats/Maisonettes, O = Other
    property_type = line.split(',')[4]

    # Y = a newly built property, N = an established residential building
    old_or_new = line.split(',')[5]

    if Summary.get(outward_code):
        if Summary[outward_code].get(date_year):
            Summary[outward_code][date_year]['count'] += 1
            Summary[outward_code][date_year]['total_price'] += int(price)
            Summary[outward_code][date_year]['avg_price'] = float(
                float(Summary[outward_code][date_year]['total_price']) / Summary[outward_code][date_year]['count'])

            if property_type == 'D':
                Summary[outward_code][date_year]['D_count'] += 1
            elif property_type == 'S':
                Summary[outward_code][date_year]['S_count'] += 1
            elif property_type == 'T':
                Summary[outward_code][date_year]['T_count'] += 1
            elif property_type == 'F':
                Summary[outward_code][date_year]['F_count'] += 1
            elif property_type == 'O':
                Summary[outward_code][date_year]['O_count'] += 1
            else:
                Summary[outward_code][date_year]['E1_count'] += 1

            if old_or_new == 'Y':
                Summary[outward_code][date_year]['Y_count'] += 1
            elif old_or_new == 'N':
                Summary[outward_code][date_year]['N_count'] += 1
            else:
                Summary[outward_code][date_year]['E2_count'] += 1

        else:
            Summary[outward_code][date_year] = {}
            Summary[outward_code][date_year]['count'] = 1
            Summary[outward_code][date_year]['total_price'] = int(price)
            Summary[outward_code][date_year]['avg_price'] = int(price)

            Summary[outward_code][date_year]['D_count'] = 0
            Summary[outward_code][date_year]['S_count'] = 0
            Summary[outward_code][date_year]['T_count'] = 0
            Summary[outward_code][date_year]['F_count'] = 0
            Summary[outward_code][date_year]['O_count'] = 0
            Summary[outward_code][date_year]['E1_count'] = 0
            Summary[outward_code][date_year]['Y_count'] = 0
            Summary[outward_code][date_year]['N_count'] = 0
            Summary[outward_code][date_year]['E2_count'] = 0

            if property_type == 'D':
                Summary[outward_code][date_year]['D_count'] = 1
            elif property_type == 'S':
                Summary[outward_code][date_year]['S_count'] = 1
            elif property_type == 'T':
                Summary[outward_code][date_year]['T_count'] = 1
            elif property_type == 'F':
                Summary[outward_code][date_year]['F_count'] = 1
            elif property_type == 'O':
                Summary[outward_code][date_year]['O_count'] = 1
            else:
                Summary[outward_code][date_year]['E1_count'] = 1

            if old_or_new == 'Y':
                Summary[outward_code][date_year]['Y_count'] = 1
            elif old_or_new == 'N':
                Summary[outward_code][date_year]['N_count'] = 1
            else:
                Summary[outward_code][date_year]['E2_count'] = 1

    else:
        Summary[outward_code] = {}
        Summary[outward_code][date_year] = {}

        Summary[outward_code][date_year]['count'] = 1
        Summary[outward_code][date_year]['total_price'] = int(price)
        Summary[outward_code][date_year]['avg_price'] = int(price)

        Summary[outward_code][date_year]['D_count'] = 0
        Summary[outward_code][date_year]['S_count'] = 0
        Summary[outward_code][date_year]['T_count'] = 0
        Summary[outward_code][date_year]['F_count'] = 0
        Summary[outward_code][date_year]['O_count'] = 0
        Summary[outward_code][date_year]['E1_count'] = 0
        Summary[outward_code][date_year]['Y_count'] = 0
        Summary[outward_code][date_year]['N_count'] = 0
        Summary[outward_code][date_year]['E2_count'] = 0

        if property_type == 'D':
            Summary[outward_code][date_year]['D_count'] = 1
        elif property_type == 'S':
            Summary[outward_code][date_year]['S_count'] = 1
        elif property_type == 'T':
            Summary[outward_code][date_year]['T_count'] = 1
        elif property_type == 'F':
            Summary[outward_code][date_year]['F_count'] = 1
        elif property_type == 'O':
            Summary[outward_code][date_year]['O_count'] = 1
        else:
            Summary[outward_code][date_year]['E1_count'] = 1

        if old_or_new == 'Y':
            Summary[outward_code][date_year]['Y_count'] = 1
        elif old_or_new == 'N':
            Summary[outward_code][date_year]['N_count'] = 1
        else:
            Summary[outward_code][date_year]['E2_count'] = 1


def analyseLinebyyearmonth(Summary, line):
    global count_without_post_code2
    line = line.replace('"', '')
    line = line.strip()
    price = line.split(',')[1]
    transaction_date = line.split(',')[2]
    date_year_month = transaction_date.split('-')[0]+'-'+transaction_date.split('-')[1]

    post_code = line.split(',')[3]
    if not post_code:
        count_without_post_code2 += 1
        return
    outward_code = post_code.split(' ')[0]

    # D = Detached, S = Semi-Detached, T = Terraced, F = Flats/Maisonettes, O = Other
    property_type = line.split(',')[4]

    # Y = a newly built property, N = an established residential building
    old_or_new = line.split(',')[5]

    if Summary.get(outward_code):
        if Summary[outward_code].get(date_year_month):
            Summary[outward_code][date_year_month]['count'] += 1
            Summary[outward_code][date_year_month]['total_price'] += int(price)
            Summary[outward_code][date_year_month]['avg_price'] = float(
                float(Summary[outward_code][date_year_month]['total_price']) / Summary[outward_code][date_year_month][
                    'count'])

            if property_type == 'D':
                Summary[outward_code][date_year_month]['D_count'] += 1
            elif property_type == 'S':
                Summary[outward_code][date_year_month]['S_count'] += 1
            elif property_type == 'T':
                Summary[outward_code][date_year_month]['T_count'] += 1
            elif property_type == 'F':
                Summary[outward_code][date_year_month]['F_count'] += 1
            elif property_type == 'O':
                Summary[outward_code][date_year_month]['O_count'] += 1
            else:
                Summary[outward_code][date_year_month]['E1_count'] += 1

            if old_or_new == 'Y':
                Summary[outward_code][date_year_month]['Y_count'] += 1
            elif old_or_new == 'N':
                Summary[outward_code][date_year_month]['N_count'] += 1
            else:
                Summary[outward_code][date_year_month]['E2_count'] += 1

        else:
            Summary[outward_code][date_year_month] = {}
            Summary[outward_code][date_year_month]['count'] = 1
            Summary[outward_code][date_year_month]['total_price'] = int(price)
            Summary[outward_code][date_year_month]['avg_price'] = int(price)

            Summary[outward_code][date_year_month]['D_count'] = 0
            Summary[outward_code][date_year_month]['S_count'] = 0
            Summary[outward_code][date_year_month]['T_count'] = 0
            Summary[outward_code][date_year_month]['F_count'] = 0
            Summary[outward_code][date_year_month]['O_count'] = 0
            Summary[outward_code][date_year_month]['E1_count'] = 0
            Summary[outward_code][date_year_month]['Y_count'] = 0
            Summary[outward_code][date_year_month]['N_count'] = 0
            Summary[outward_code][date_year_month]['E2_count'] = 0

            if property_type == 'D':
                Summary[outward_code][date_year_month]['D_count'] = 1
            elif property_type == 'S':
                Summary[outward_code][date_year_month]['S_count'] = 1
            elif property_type == 'T':
                Summary[outward_code][date_year_month]['T_count'] = 1
            elif property_type == 'F':
                Summary[outward_code][date_year_month]['F_count'] = 1
            elif property_type == 'O':
                Summary[outward_code][date_year_month]['O_count'] = 1
            else:
                Summary[outward_code][date_year_month]['E1_count'] = 1

            if old_or_new == 'Y':
                Summary[outward_code][date_year_month]['Y_count'] = 1
            elif old_or_new == 'N':
                Summary[outward_code][date_year_month]['N_count'] = 1
            else:
                Summary[outward_code][date_year_month]['E2_count'] = 1

    else:
        Summary[outward_code] = {}
        Summary[outward_code][date_year_month] = {}

        Summary[outward_code][date_year_month]['count'] = 1
        Summary[outward_code][date_year_month]['total_price'] = int(price)
        Summary[outward_code][date_year_month]['avg_price'] = int(price)

        Summary[outward_code][date_year_month]['D_count'] = 0
        Summary[outward_code][date_year_month]['S_count'] = 0
        Summary[outward_code][date_year_month]['T_count'] = 0
        Summary[outward_code][date_year_month]['F_count'] = 0
        Summary[outward_code][date_year_month]['O_count'] = 0
        Summary[outward_code][date_year_month]['E1_count'] = 0
        Summary[outward_code][date_year_month]['Y_count'] = 0
        Summary[outward_code][date_year_month]['N_count'] = 0
        Summary[outward_code][date_year_month]['E2_count'] = 0

        if property_type == 'D':
            Summary[outward_code][date_year_month]['D_count'] = 1
        elif property_type == 'S':
            Summary[outward_code][date_year_month]['S_count'] = 1
        elif property_type == 'T':
            Summary[outward_code][date_year_month]['T_count'] = 1
        elif property_type == 'F':
            Summary[outward_code][date_year_month]['F_count'] = 1
        elif property_type == 'O':
            Summary[outward_code][date_year_month]['O_count'] = 1
        else:
            Summary[outward_code][date_year_month]['E1_count'] = 1

        if old_or_new == 'Y':
            Summary[outward_code][date_year_month]['Y_count'] = 1
        elif old_or_new == 'N':
            Summary[outward_code][date_year_month]['N_count'] = 1
        else:
            Summary[outward_code][date_year_month]['E2_count'] = 1


def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print ("Total time running %s: %s seconds" %
               (function.func_name, str(t1 - t0))
               )
        return result

    return function_timer

@fn_timer
def analysisYearHpp():
    with open(OUT_FILE1, 'w') as outfile, open(DATA_FILE, 'r') as infile:
        i = 0
        print '================Start analysis================'
        for line in infile:
            i += 1
            line = line.replace('"', '')
            line = line.strip()
            analyseLinebyyear(Summary, line)
        print '================total count:%d, without postcode:%d================' % (i, count_without_post_code1)

        j = 0
        count_total = 0
        for key in Summary:
            for key1 in Summary[key]:
                j += 1
                count_total += int(Summary[key][key1]['count'])
                retstr = key + ',' + key1 + ',' + str(Summary[key][key1]['count']) + ',' \
                         + str(Summary[key][key1]['avg_price']) + ',' + str(Summary[key][key1]['D_count']) \
                         + ',' + str(Summary[key][key1]['S_count']) + ',' + str(Summary[key][key1]['T_count']) \
                         + ',' + str(Summary[key][key1]['F_count']) + ',' + str(Summary[key][key1]['O_count']) \
                         + ',' + str(Summary[key][key1]['Y_count']) + ',' + str(Summary[key][key1]['N_count']) \
                         + '\n'
                outfile.write(retstr)
        print '================total analysis records:%d, total count:%d================' % (j, count_total)


@fn_timer
def analysisYearMonthHpp():
    with open(OUT_FILE2, 'w') as outfile, open(DATA_FILE, 'r') as infile:
        i = 0
        print '================Start analysis================'
        for line in infile:
            i += 1
            line = line.replace('"', '')
            line = line.strip()
            analyseLinebyyearmonth(Summary, line)
        print '================total count:%d, without postcode:%d================' % (i, count_without_post_code2)

        j = 0
        count_total = 0
        for key in Summary:
            for key1 in Summary[key]:
                j += 1
                count_total += int(Summary[key][key1]['count'])
                retstr = key + ',' + key1 + ',' + str(Summary[key][key1]['count']) + ',' \
                         + str(Summary[key][key1]['avg_price']) + ',' + str(Summary[key][key1]['D_count']) \
                         + ',' + str(Summary[key][key1]['S_count']) + ',' + str(Summary[key][key1]['T_count']) \
                         + ',' + str(Summary[key][key1]['F_count']) + ',' + str(Summary[key][key1]['O_count']) \
                         + ',' + str(Summary[key][key1]['Y_count']) + ',' + str(Summary[key][key1]['N_count']) \
                         + '\n'
                outfile.write(retstr)
        print '================total analysis records:%d, total count:%d================' % (j, count_total)


if __name__ == "__main__":
    analysisYearHpp()
    #analysisYearMonthHpp()