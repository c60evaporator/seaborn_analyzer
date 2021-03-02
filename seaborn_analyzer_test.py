#%% custom_pair_plot
from custom_pair_plot import CustomPairPlot
import seaborn as sns

titanic = sns.load_dataset("titanic")
cp = CustomPairPlot()
cp.pairanalyzer(titanic, hue='survived')

#%% custom_dist_plot
from custom_dist_plot import dist
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
fig, axes = plt.subplots(2, 2, figsize=(8, 8))
dist.hist_dist(iris['sepal_length'], ax=axes[0, 0], rounddigit=5)
#%% custom_scatter_plot.regression_plot_pred
from custom_scatter_plot import dist
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import LeaveOneOut

iris = sns.load_dataset("iris")
dist.regression_plot_pred(LinearRegression(), 'petal_length', 'sepal_length', iris, plot_stats='median', rounddigit=3, rank_number=3, cv=5)
# %% custom_scatter_plot.linear_plot
from custom_scatter_plot import dist
import seaborn as sns
iris = sns.load_dataset("iris")
dist.linear_plot('petal_length', 'sepal_length', iris, hue='species', rounddigit=5)
# %%