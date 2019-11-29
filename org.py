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
            pattern = '.+Configured\s+Serial\s+Number(.+)\s+(\S{12})'
            result = re.match(pattern,content)
            c_s = result.group(2)
            print("chassis serial is {}".format(c_s))
            while(line.find('Node Module') != -1):
                line = f.readline()
        if line.find('Node Position') != -1:
            ## node position ##
            n_p = line
            print("node position is {}".format(n_p))
        if line.find('Serial number') != -1:
            ## node serial ##
            n_s = line
            print(n_s)
