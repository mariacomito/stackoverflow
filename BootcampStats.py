#%% [markdown]
# Now let's look at the second question of interest.  That is - What does the data suggest of Bootcamp grads in terms of job placement and salary?
# 
# Again, let's read in the data and necessary libraries.

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv('./survey_results_public.csv')
df.head()


#%%
#In this case, we want to look at bootcamp data
#First - let's just look at how many people took a bootcamp in the dataset

bootcamp_df = df[df['TimeAfterBootcamp'].isnull()==False]
not_bootcamp_df = df[df['TimeAfterBootcamp'].isnull()==True] 
bootcamp_df.shape


#%%
# Looks like a reasonable sample of ~2600 people

#Additional questions about bootcamps - they suggest high salaries, placement, 
#helping those with non-traditional backgrounds and diversity break into tech... let's see what
#the data suggests.


#%%
bootcamp_df['Gender'].value_counts()/(bootcamp_df.shape[0] - sum(bootcamp_df['Gender'].isnull()))


#%%
not_bootcamp_df['Gender'].value_counts()/(not_bootcamp_df.shape[0] - sum(not_bootcamp_df['Gender'].isnull()))


#%%
#It does appear there is a small push for diversity overall by bootcamps, but not huge...


#%%
bootcamp_df['FormalEducation'].value_counts()/(bootcamp_df.shape[0] - sum(bootcamp_df['FormalEducation'].isnull()))


#%%
not_bootcamp_df['FormalEducation'].value_counts()/(not_bootcamp_df.shape[0] - sum(not_bootcamp_df['FormalEducation'].isnull()))


#%%
#In terms of formal education it looks basically the same - more bachelors degree holders do 
#bootcamps, but fewer phds do bootcamps.


#%%
bootcamp_df['TimeAfterBootcamp'].value_counts()/bootcamp_df.shape[0]


#%%
#So interestingly this data makes it more difficult to analyze the impact of bootcamps,
# as many of the students already had developer jobs before starting the program
# we could remove them?

#If you are truly new to the space, we can rule out that you already have a job as a developer
# then we can look at the other individuals and see which are still not 

not_devs = bootcamp_df[bootcamp_df['TimeAfterBootcamp']!="I already had a job as a developer when I started the program"]


#%%
not_devs['TimeAfterBootcamp'].value_counts()/not_devs.shape[0]


#%%
bootcamp_df[bootcamp_df['Salary']==195000]


#%%
bootcamp_df['Salary'].hist(bins=20);
plt.title('Salary for Bootcamp Grads');
plt.xlabel('Salary');
plt.ylabel('Count');


#%%
bootcamp_df.shape()
bootcamp_df['Salary'].describe()


#%%
#Here we can get some idea of how bootcamp grades fair, but this isn't straightforward.
#Many of these individuals are not new to the field, and the salaries are all over the place
#But the descriptive statistics here give us some ideas... just nothing really concrete


