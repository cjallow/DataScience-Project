import pandas as pd

#added this because it's indicated as useful but not imported
import urllib
from zipfile import ZipFile
import os

#I Definitely copy and pasted this next piece. I found it here:
#http://stackoverflow.com/a/13895723
def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %*d / %d" % (
            percent, len(str(totalsize)), readsofar, totalsize)
        os.sys.stderr.write(s)
        if readsofar >= totalsize: # near the end
            os.sys.stderr.write("\n")
    else: # total size is unknown
        os.sys.stderr.write("read %d\n" % (readsofar,))



#my attempt at data caching
#it tries to open a file int the data directory.
#if the file does not exist, it downloads it and tries to open it again

#Input: a list of links to the data files.
#Output: a list of dataframes
def get_cached_or_dl(url_list):
    datadir = "data"
    try:
        os.makedirs(datadir)
    except:
        pass #directory already exists. :P
    
    theList = []
    for url in url_list:
        filename = os.path.join(datadir,url.split("/")[-1])
        extension = filename.split(".")[-1].lower()
        try:
            if(extension == "zip"):
                zipF = ZipFile(filename)
                #Let's try opening every file in the zip archive
                data = []
                for f in zipF.namelist():
                    fileinzip = os.path.join(datadir,f)
                    extinzip = f.split(".")[-1]
                    if(extinzip == "csv"):
                        data.append(pd.read_csv(fileinzip))
                    elif(extinzip == "xls" or extinzip == "xlsx"):
                        data.append(pd.read_excel(fileinzip))
                    elif(extinzip == "json"):
                        data.append(pd.read_json(fileinzip))
                    else:
                        print("how to open " + fileinzip + " in zip?")
            elif(extension == "csv"):
                data = [pd.read_csv(filename)]
            elif(extension == "xls" or extension == "xlsx"):
                data = [pd.read_excel(filename)]
            elif(extension == "json"):
                data = [pd.read_json(filename)]
            else:
                data = []
                print("how to open " + filename + "?")
        except FileNotFoundError as e:
            #if file doesn't exist, download it and try opening it again
            if(extension == "zip"):
                try:
                    zipF = ZipFile(filename)
                except FileNotFoundError as e:
                    #the zip file needs to be downloaded
                    urllib.request.urlretrieve(url, filename, reporthook)
                    zipF = ZipFile(filename)
            else:
                urllib.request.urlretrieve(url, filename, reporthook)
            
            if(extension == "zip"):
                #Let's extract and then open the files
                zipF.extractall(datadir)
                data = []
                for f in zipF.namelist():
                    fileinzip = os.path.join(datadir,f)
                    extinzip = f.split(".")[-1]
                    if(extinzip == "csv"):
                        data.append(pd.read_csv(fileinzip))
                    elif(extinzip == "xls" or extinzip == "xlsx"):
                        data.append(pd.read_excel(fileinzip))
                    elif(extinzip == "json"):
                        data.append(pd.read_json(fileinzip))
                    else:
                        print("how to open " + fileinzip + " in zip?")
            elif(extension == "csv"):
                data = [pd.read_csv(filename)]
            elif(extension == "xls" or extension == "xlsx"):
                data = [pd.read_excel(filename)]
            elif(extension == "json"):
                data = [pd.read_json(filename)]
        theList.extend(data)
    return theList
