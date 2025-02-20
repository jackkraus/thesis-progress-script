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

yourname = "Jack Kraus"

# Adjust this to the path you want the progress.csv to show up 
df = pd.read_csv('/Users/jackkraus/Desktop/masters-thesis/Jack-MS-Thesis-Draft/progressTracking/progress.csv')

df['timestamp_fixed'] = pd.to_datetime(df['timestamp'], format="%Y-%m-%d %H:%M:%S")
df = df.set_index('timestamp_fixed')

# Define the start and end dates for the range you want to check
start_date = '2024-12-01'
end_date = '2025-02-19'

# Filter the DataFrame for the specified date range
filtered_df = df.loc[start_date:end_date]

# Calculate percent change for pagecount and wordcount
filtered_df['pagecount_pct_change'] = filtered_df['pagecount'].pct_change() * 100
filtered_df['wordcount_pct_change'] = filtered_df['wordcount'].pct_change() * 100

# Print the filtered DataFrame with percent change
print("Filtered DataFrame with Percent Change:")
print(filtered_df[['pagecount', 'pagecount_pct_change', 'wordcount', 'wordcount_pct_change']])

# Use the last values from the filtered DataFrame for annotations
current_pagecount = filtered_df["pagecount"].iloc[-1]
current_wordcount = filtered_df["wordcount"].iloc[-1]

wc_color="orangered"
pc_color="royalblue"
pct_color="green"  # Color for percent change lines

# Adjust this to your name
def add_watermark(text=yourname):
    """
    adds watermark to lower left corner of matplotlib plot
    """
    # print(f"Adding watermark: {text}")  # Debugging print statement
    plt.annotate(text, xy=(.01,.007), xycoords='figure fraction',
                 textcoords='figure fraction', color='grey',alpha=0.7, fontsize=14)

# Combined Plot with Percent Change
months = mdates.MonthLocator()  # every month
days = mdates.DayLocator()  # every day
date_fmt = mdates.DateFormatter('%b %d')


# Plot 1: Word Count and Percent Change
fig, ax1 = plt.subplots()
ax1.set_xlabel('Date', fontsize=16)
ax1.set_ylabel('Word Count', fontsize=16, color=wc_color)
ax1.plot(filtered_df.index, filtered_df['wordcount'], color=wc_color, label='Word Count')
ax1.tick_params(axis='y', labelcolor=wc_color)

ax1.xaxis.set_minor_locator(days)
ax1.xaxis.set_major_formatter(date_fmt)

# Add percent change for word count
ax2 = ax1.twinx()
ax2.set_ylabel('Word Count % Change', fontsize=16, color=pct_color)
ax2.plot(filtered_df.index, filtered_df['wordcount_pct_change'], color=pct_color, linestyle='dashed', alpha=0.5, label='Word Count % Change')
ax2.tick_params(axis='y', labelcolor=pct_color)

plt.annotate("{:,d} Words".format(current_wordcount), xy=(.7,.9), xycoords="axes fraction",color=wc_color, fontsize=10)


sns.despine()
ax1.tick_params(labelsize=12,rotation=25)
plt.tight_layout()
add_watermark()
plt.savefig(savedir+'plots/wordcount.png')  # Save with a new name
plt.close()

# Plot 2: Page Count and Percent Change
fig, ax1 = plt.subplots()
ax1.xaxis.set_minor_locator(days)
ax1.xaxis.set_major_formatter(date_fmt)
ax1.set_xlabel('Date', fontsize=16)
ax1.set_ylabel('Page Count', fontsize=16, color=pc_color)
ax1.plot(filtered_df.index, filtered_df['pagecount'], color=pc_color, label='Page Count')
ax1.tick_params(axis='y', labelcolor=pc_color)


# Add percent change for page count
ax2 = ax1.twinx()
ax2.set_ylabel('Page Count % Change', fontsize=16, color=pct_color)
ax2.plot(filtered_df.index, filtered_df['pagecount_pct_change'], color=pct_color, linestyle='dashed', alpha=0.5, label='Page Count % Change')
ax2.tick_params(axis='y', labelcolor=pct_color)

plt.annotate("{:,d} Pages".format(current_pagecount), xy=(.7,.9), xycoords="axes fraction",color=pc_color, fontsize=10)

sns.despine()
ax1.tick_params(labelsize=12,rotation=25)
plt.tight_layout()
add_watermark()
plt.savefig(savedir+'plots/pagecount.png')  # Save with a new name
plt.close()


fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# Plot pagecount and wordcount
ax1.plot(filtered_df.index, filtered_df['pagecount'], color=pc_color, label='Page Count')
ax2.plot(filtered_df.index, filtered_df['wordcount'], color=wc_color, label='Word Count')

# Plot percent change for pagecount and wordcount
# ax1.plot(filtered_df.index, filtered_df['pagecount_pct_change'], color=pc_color, linestyle='--', label='Page Count % Change')
# ax2.plot(filtered_df.index, filtered_df['wordcount_pct_change'], color=wc_color, linestyle='--', label='Word Count % Change')

ax1.set_ylabel("Page Count", fontsize=16, color=pc_color)
ax2.set_ylabel("Word Count", fontsize=16, color=wc_color)
ax1.set_xlabel('Date', fontsize=16)
ax1.set_ylim(ymin=0)
ax2.set_ylim(ymin=0)

plt.annotate("{:,d} Pages".format(current_pagecount), xy=(.05,.88), xycoords="axes fraction",color=pc_color, fontsize=10)
plt.annotate("{:,d} Words".format(current_wordcount), xy=(.05,.8), xycoords="axes fraction",color=wc_color, fontsize=10)

ax1.xaxis.set_minor_locator(days)
ax1.xaxis.set_major_formatter(date_fmt)

ax1.tick_params(labelsize=12,rotation=25)
ax2.tick_params(labelsize=12)
plt.tight_layout()
add_watermark()
plt.savefig(savedir+"plots/combinedProgress.png")  # Save with a new name
