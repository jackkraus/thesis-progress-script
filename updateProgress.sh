#!/bin/sh
export PATH=/usr/local/bin:/Library/TeX/texbin/:$PATH
#export PATH=/usr/local/bin:$PATH
echo "Updating dissertation progress"
DOCUMENT='/Users/jackkraus/Desktop/masters-thesis/Jack-MS-Thesis-Draft/main.pdf'
TEX_DOC='/Users/jackkraus/Desktop/masters-thesis/Jack-MS-Thesis-Draft/main.tex'
PROGRESSFILE='/Users/jackkraus/Desktop/masters-thesis/Jack-MS-Thesis-Draft/progressTracking/progress.csv'
cd /Users/jackkraus/Desktop/masters-thesis/Jack-MS-Thesis-Draft/
WORDCOUNT=`texcount -sum -total -merge {$TEX_DOC} | grep "Sum count:" | tr -d "Sum count: "`
# Use this line in OSX
PAGECOUNT=`mdls -name kMDItemNumberOfPages -raw ${DOCUMENT}`
# Use this line in Linux
# PAGECOUNT=`pdfinfo mythesis.pdf | grep Pages | sed 's/[^0-9]*//'`
echo `date '+%Y-%m-%d %H:%M:%S'`,$WORDCOUNT,$PAGECOUNT >> $PROGRESSFILE
echo "Done! Page count ${PAGECOUNT}, word count ${WORDCOUNT}"

python3 /Users/jackkraus/Desktop/masters-thesis/Jack-MS-Thesis-Draft/progressTracking/plotProgress.py
# Code from Tyler Burch, thank you!!