# thesis-progress-script

To start, you'll need to remove all `progress.csv` entries (except the headers in the first line)

Then you'll need to update the following lines in the `updateProgress.sh` to map to your output/.tex file/.csv file:

```
...
DOCUMENT='/Users/jackkraus/Desktop/masters-thesis/Jack-MS-Thesis-Draft/main.pdf'
TEX_DOC='/Users/jackkraus/Desktop/masters-thesis/Jack-MS-Thesis-Draft/main.tex'
PROGRESSFILE='/Users/jackkraus/Desktop/masters-thesis/Jack-MS-Thesis-Draft/progressTracking/progress.csv'
cd /Users/jackkraus/Desktop/masters-thesis/Jack-MS-Thesis-Draft/
...
python3 /Users/jackkraus/Desktop/masters-thesis/Jack-MS-Thesis-Draft/progressTracking/plotProgress.py
```

Afterwards, hopefully with minimal debugging, you should be able to run the update script:

`$ ./updateProgress.sh` 

This will automatically count pages and words and deposit them along with the date into the `progress.csv` :) 