#HAMMING DISTANCE 

slack_username = "Aseghiemhe"
twitter_handle = "_Oshoreame"


def hamming_distance_calculator():
  hamming_distance = sum(slack != twitter for slack, twitter  in zip(slack_username, twitter_handle))

  #Slack and twitter are used as the variable names representing slack_username and twitter_handle to avoid repitition.
  return(hamming_distance)


print(f"Hamming distance between '{slack_username}' and '{twitter_handle}' is: {hamming_distance}")


#SURPRISE TASKS


# (PART A) A to B
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Normalized counts for HBR vs URH
data_source1 = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/hbr_uhr_top_deg_normalized_counts.csv"
# extract data from data source
df = pd.read_csv(data_source1)

df.columns = ['genes', 'HBR_1', 'HBR_2', 'HBR_3', 'UHR_1', 'UHR_2', 'UHR_3']
df.set_index("genes", inplace=True)

# heatmap
sns.clustermap(
    df,
    cmap="Blues",
    figsize=(4,4),
    linewidths=0.5,
    linecolor="black")

# Differential expression results (chromosome 22) (b)
data_source2 = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/hbr_uhr_deg_chr22_with_significance.csv"
# extract data from data source
df1 = pd.read_csv(data_source2)

# volcano plot
plt.figure(figsize=(4,4))
sns.scatterplot(df1, x="log2FoldChange", y="-log10PAdj", hue="significance")
plt.axvline(x=-1, color="grey", linestyle="--", linewidth=1)
plt.axvline(x=1, color="grey", linestyle="--", linewidth=1)
plt.axhline(y=1.3, color="grey", linestyle="--", linewidth=1)
plt.show()


# (PART B) C to F
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_source3 = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/data-3.csv"


# Breast Cancer Wisconsin dataset (c)
# extract data from data source
df21 = pd.read_csv(data_source3)
sns.scatterplot(df21, x="radius_mean", y="texture_mean", hue="diagnosis")



# Correlation Heatmap (d)
# extract data from data source
df2 = pd.read_csv(data_source3)
# compute only the correlation matrix of 6 key features
x = df2[['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean']]

# plot heatmap
sns.heatmap(x.corr(numeric_only=True), annot=True, cmap="Blues")


# Breast Cancer Wisconsin dataset (e)
# extract data from data source
df31 = pd.read_csv(data_source3)

# plot scatterplot
sns.scatterplot(df31, x="smoothness_mean", y="compactness_mean", hue="diagnosis")


# Breast Cancer Wisconsin dataset (f)
# extract data from data source
df61= pd.read_csv(data_source3)

# plot density plot
sns.displot(df61, x="area_mean", kind="kde", hue="diagnosis", fill=True)
