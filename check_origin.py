import glob
import re

file_list = glob.glob("/home/furukubo/source/check_origin/hard/*")
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

for key in s_info:
    print(s_info[key])
