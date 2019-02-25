# coding: utf-8

# # DOCUMENTATION: babyalgebraist.github.io
"""
I'm making content for a personal website that will include details on my
activities and course histories. This page will serve as a sort of 'Appendix'
for my CV, with added detail should an interested person check it out.

General Task: Convert HTML table to DataFrame; make new HTML Table with
Required Information
We want to take the raw table data (saved manually from a password protected
student portal by inspecting elements with Chrome).
We will strip away extraneous information, and make a simple list of the
institution's course name and number with a brief description or name,
correcting missing or poorly formatted data with correct or better details.
What follows are the steps taken along with some justification.
If you have any comments, please make them on the github repository
as an issue.

Thanks a bunch!
"""

# Start Script
import pandas as pd


# The Column names are Truncated, and or Abbreviated. Let's change that.

col_names = ['Course', 'Num', 'Section',	'Description',
             'Attempted', 'Grade', 'Notation',
             'GPA', 'Class Avg', 'Class Size',
             'Credits Earned', 'Other']

# Read 'FILE_NAME' into DataFrames with pandas 'pd.read_html()'.
# Will return a list containing all the tables as DataFrames: 'df_list'
# For each DataFrame, we're going to make a copy, each as a csv named
# for their index in the list. We expect 8.

FILE_NAME = 'assets/data/course_history_raw.html'

df_list = pd.read_html(FILE_NAME)


# So we made a list of the files to use to build a clean list of courses.
# We are only really interested in Table 2 onward.
# So lets remove 'table_0.csv' and 'table_1.csv', making the list only 6 long.

df_list = df_list[2:]
len(df_list)

files = []
for i, df in enumerate(df_list):
    df.to_csv('assets/data/table_{}.csv'.format(i),
              index=False)
    files.append('assets/data/table_{}.csv'.format(i))

files

# Inpsect the DataFrames...

i = 0
for table in df_list:
    print("\nTable number {} \n\n".format(i), table)
    i += 1

# First, we'll sneakily save the 'names' for the DataFrames in a DataFrames
# as strings: `df_<cnt>`

# Then concatenate the DataFrames
# In a loop, we'll read in each of the tables saved as CSVs in the last step.
# Then drop unnecessary column: 'Section' in place

cnt = len(files)  # counter for loop
dict_of_df = {}  # initialize empty dictionary

csv_files = 'assets/data/table_{}.csv'
for i in range(cnt):
    dict_of_df['df_{}'.format(i)] = pd.read_csv(csv_files.format(i),
                                                header=None,
                                                skiprows=1,
                                                usecols=[0, 1, 2, 3],
                                                names=col_names[:4])
dfs_list = list(dict_of_df.keys())

df = pd.concat(dict_of_df, ignore_index=True)
# display(df)
df.drop(columns=['Section'], inplace=True)
print(df)


# See that there are some extraneous 'Course Topic' etries set by the student
# portal to handle topics classes or courses taken by Inter University
# Transfer (Crépuq here in Quebec). These rows should be removed.
# We'll use a mask to find them all.
# See the 15th record is a topic course. We need to rescue the data in the
# description column, put it in 'Course Number' column as 'MATH 457'  and
# set the description to 'Fields and Galois Theory'

# Similarly,
# -  update 'Description' to the description in the next row
# -  but with some special attention paid to the 'Course' and 'Num'
# information. (see below)
# - likewise for the other records. No special attention is required

# The boolean mask to find index of location of the 'Course Topics:' value

mask = df.Course == 'Course Topic:'
topics_ind = list(df[mask].index)
topics = list(df[mask].Num.values)

topics_ilocs = list(zip(topics_ind, topics))

topics_ilocs

# Reminder: the record for 'Honors Algebra 4' has to have some extra lifting.
# Here it is for reference.

df.loc[24:25, 'Course':'Description']

# This should be self-explanitory.
for ind, value in iter(topics_ilocs):
    if df.loc[ind - 1, 'Course'] == 'INTU':
        df.loc[ind - 1, 'Course'] = 'MATH'
        df.loc[ind - 1, 'Num'] = '457'
        df.loc[ind - 1, 'Description'] = 'Fields and Galois Theory'.upper()
        df.drop([ind], inplace=True)
        print('\n')
        print(df.loc[ind - 1])
    else:
        df.loc[ind - 1, 'Description'] = 'TOPIC: ' + df.loc[ind, 'Description']
        df.drop([ind], inplace=True)
        print('\n', df.loc[ind - 1], '\n')

df.reset_index(inplace=True, drop=True)
df

# Now, that we have the 'Descriptions' more or less okay,
# we'll cast the 'Num' column as a string to concatenate the strings
# they contain.

# We do this because we want a single column with the Departement code and
# the course code as one strong for reading.
df['Num'] = df.Num.astype(str)
df.info()

# Now, we actually do the concatenation, making the new column 'Course Number'
# then drop the old columns, 'Course' and 'Num' in place, before reordering
# the columns for readability, and dropping the extra 'Topics' rows

df['Course Number'] = (df['Course'] + ' ' + df['Num'])
df.drop(columns=['Course', 'Num'], inplace=True)
df = df[['Course Number', 'Description']]

# Inspect the DF
print(df)

# Save them to files: CSV for later usage; html for incorporation into the
# website.

df.to_csv('assets/data/course_history.csv')
df.to_html('assets/data/course_history_temp.html', index=False)

# Thoughts:
# As I have two degrees at 4 institutions, consider adding these and columns
# that state year taken, at which institution.

# End Script
