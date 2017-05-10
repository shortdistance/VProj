DATA_FILE = "/Users/leizhang/Downloads/UK_House_Price_paid_data/pp-complete.csv"
OUT_FILE = "/Users/leizhang/Downloads/ret.log"

"""
with open(OUT_FILE, 'w') as outfile, open(DATA_FILE, 'r') as infile:
    for line in infile:
        line = line.replace('"','')
        datetime = line.split(',')
        if datetime[2]:
            if int(datetime[2].split('-')[0])>2015:
                outfile.write(','.join(line.split(',')[1:-2])+'\n')
"""

# save all postcode to check which postcode has house sold info.
with open(OUT_FILE, 'w') as outfile, open(DATA_FILE, 'r') as infile:
    i = 0
    for line in infile:
        i += 1
        line = line.replace('"', '')
        datetime = line.split(',')
        postcode = ''
        if datetime[2]:
            if int(datetime[2].split('-')[0]) > 2015:
                outfile.write(line.split(',')[3] + '\n')
        if i % 2000 == 0:
            print(i)
