#!/usr/bin/env python

import getopt
import os
import urllib.request
import sys

def download_gs(oform, odir, dstring, dform):
    for year in range(1992, 2013):
        year_dir = odir + str(year)
        if not os.path.isdir(year_dir):
            os.makedirs(year_dir)
        for number in range(1, 5):
            if (year == 1996 and number == 1):
                continue
            mag = urllib.request.urlretrieve(dstring.format(year, number, dform), year_dir + oform.format(year, number, dform))

if __name__ == "__main__":
    #set defaults
    OUTPUT_FORMAT = "/{0}-{1}.{2}"
    OUTPUT_DIR = os.getcwd() + "/GegenStandpunkt/Hefte/"
    DOWNLOAD_STRING = "http://gegenstandpunkt.com/gs/{2}-Format/GegenStandpunkt%20{0}%20Heft%20{1}%20-%20GegenStandpunkt%20Verlag.{2}"
    DOWNLOAD_FORMAT = "epub"

    #get options
    named,unnamed = getopt.gnu_getopt(sys.argv[1:], "o:", ["output=", "output-format="])

    #parse named options
    for o,v in named:
        #parse output option
        if o == "-o" or o == "--output":
            #check if slash at end
            if not v[-1] == "/":
                v += "/"
            #check if valid path
            OUTPUT_DIR = os.path.expanduser(v) + "GegenStandpunkt/Hefte/"
            if not os.path.isdir(OUTPUT_DIR):
                os.makedirs(OUTPUT_DIR)
        elif o == "--output-format":
            OUTPUT_FORMAT = "/" + v + ".{2}"

    for o in unnamed:
        #set format of gs download
        if (o == "gsazw"):
            DOWNLOAD_FORMAT = "azw3"
        if (o == "gsmobi"):
            DOWNLOAD_FORMAT = "mobi"
        if (o == "gsepub"):
            DOWNLOAD_FORMAT = "epub"

    download_gs(OUTPUT_FORMAT, OUTPUT_DIR, DOWNLOAD_STRING, DOWNLOAD_FORMAT)
