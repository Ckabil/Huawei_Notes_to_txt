from glob import glob
import re

output_folder = "file_location/OUTPUT/"


for i in glob('file_location/*/'):
    try:
        f = open(i + "json.js", "r")
        line = f.read()
        a = line[line.find('\"Text|'):line.find('\"has_todo\"')].replace("\\n", " \n ").replace('\"Text|', "")
        filename = re.sub('[!@#$Ä±Ã¼Ÿ§¶ÅŸ<>|:]','',a.partition('\n')[0].strip()).replace(' ', '').replace('/','')
        filenamelimit = output_folder + filename[:26]
        f1 = open(filenamelimit + ".txt", "w")
        f1.write(a)
        f1.close()
    except:
        print(i)