import glob
import re
import pandas as pd

file_list = glob.glob(r"C:\Users\Takeo Furukubo\PycharmProjects\check_origin\nuta_cons_info\*")
s_info = {}
for filename in file_list:
    f = open(filename,'r')
    for line in f:
        line.strip()
        if line.find('Configured Serial Number') != -1:
            ## charssis serial ##
            content = line
            pattern = '.+Configured\s+Serial\s+Number.+\s+(\S{12})'
            result = re.match(pattern,content)
            c_s = result.group(1)

            ## Move to Node Position ##
            while(line.find('Node Position') == -1):
                line = f.readline()
            ## node position ##
            content = line
            pattern = '.+Node\s+Position\s+.+\s+(\w)'
            result = re.match(pattern,content)
            n_p = result.group(1)
            
            ## Move to Node Serial ##
            while(line.find('Serial number') == -1):
                line = f.readline()
            ## node serial ##
            content = line
            pattern = '.+Serial\s+number\s+.+\s+(\S{12})'
            result = re.match(pattern,content)
            n_s = result.group(1)
            if c_s not in s_info:
                s_info[c_s] = {}
            s_info[c_s][n_p] = n_s
    f.close()

f = open("SFDCdata.csv",'w')
for key in s_info:
    for p in s_info[key]:
        temp = key+","+s_info[key][p]+","+p+"\n"
        f.write(temp)
f.close()


df = pd.read_csv("all.csv")
chassis = df['chassis']
f = open("original.csv",'w')
for index,row in df.iterrows():
    if row['chassis'] in s_info:
        if row['position'] == "A":
            temp = row['host']+","+s_info[row['chassis']]["A"]+","+row['chassis']+","+"A"+"\n"
        else:
            temp = row['host']+","+s_info[row['chassis']]["D"]+","+row['chassis']+","+"D"+"\n"
    else:
        if row['position'] == "A":
            temp = row['host']+","+"N/A"+","+"replaced"+","+"A"+"\n"
        else:
            temp = row['host'] + "," + "N/A" + "," + "replaced" + "," + "D" + "\n"
    f.write(temp)
f.close()