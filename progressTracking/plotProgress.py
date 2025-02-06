# code cred goes to Tyler Burch

# To start, you'll need to remove all `progress.csv` entries 
#       (except the headers in the first line) and then
#       you should be able to run the update script:
#       $ ./updateProgress.sh 

from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

# Adjust this to the path for your thesis/progressTracking directory
savedir = "/Users/jackkraus/Desktop/masters-thesis/Jack-MS-Thesis-Draft/progressTracking/"

# Adjust this to the path you want the progress.csv to show up 
df = pd.read_csv('/Users/jackkraus/Desktop/masters-thesis/Jack-MS-Thesis-Draft/progressTracking/progress.csv')

df['timestamp_fixed'] = pd.to_datetime(df['timestamp'], format="%Y-%m-%d %H:%M:%S")
df = df.set_index('timestamp_fixed')

current_pagecount = df["pagecount"].iloc[-1]
current_wordcount = df["wordcount"].iloc[-1]

wc_color="orangered"
pc_color="royalblue"

# Adjust this to your name
def add_watermark(text="Jack Kraus"):
    """
    adds watermark to lower left corner of matplotlib plot
    """
    print(f"Adding watermark: {text}")  # Debugging print statement
    plt.annotate(text, xy=(.01,.007), xycoords='figure fraction',
                 textcoords='figure fraction', color='grey',alpha=0.7, fontsize=14)

# Plot 1
df.plot(y='wordcount', legend=None, color=wc_color)
plt.xlabel('Date',fontsize=16)
plt.ylabel('Word Count',fontsize=16)
sns.despine()
plt.tight_layout()
plt.savefig(savedir+'plots/wordcount.png')
plt.close()

# Plot 2
df.plot(y='pagecount',legend=None, color=pc_color)
plt.xlabel('Date',fontsize=16)
plt.ylabel('Page Count',fontsize=16)
sns.despine()
plt.tight_layout()
plt.savefig(savedir+'plots/pagecount.png')
plt.close()

# Combined Plot
months = mdates.MonthLocator()  # every month
days = mdates.DayLocator()  # every dat
date_fmt = mdates.DateFormatter('%b %d')

fig, ax = plt.figure(), plt.gca()
ax2= ax.twinx()
df.plot(y='pagecount',legend=None, ax=ax, color=pc_color)
df.plot(y='wordcount', legend=None, ax=ax2, color=wc_color)

ax.set_ylabel("Page Count", fontsize=16, color=pc_color)
ax2.set_ylabel("Word Count", fontsize=16,color=wc_color)
ax.set_xlabel('Date',fontsize=16)
ax.set_ylim(ymin=0)
ax2.set_ylim(ymin=0)

plt.annotate("{:,d} Pages".format(current_pagecount), xy=(.05,.88), xycoords="axes fraction",color=pc_color, fontsize=12)
plt.annotate("{:,d} Words".format(current_wordcount), xy=(.05,.8), xycoords="axes fraction",color=wc_color, fontsize=12)

# ax.xaxis.set_major_locator(months)
ax.xaxis.set_minor_locator(days)
ax.xaxis.set_major_formatter(date_fmt)

# Add key dates
"""
dates = {}
dates["Detector chapter \nsent for edits "] = "2019-09-22 15:30:00"
dates["Theory chapter \nsent for edits "] = "2019-10-20 21:57:00"

for title,dt in dates.items():
    xloc = pd.to_datetime(dt)
    ax.axvline(x=xloc, color='firebrick', linestyle='--',)
    plt.annotate(title, xy=(xloc, 100), color="firebrick", fontsize=10, ha="right")
"""

ax.tick_params(labelsize=12)
ax2.tick_params(labelsize=12)
plt.tight_layout()
add_watermark()
plt.savefig(savedir+"plots/combinedProgress.png")
