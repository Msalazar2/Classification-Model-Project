import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

def countplt(df, target, feature):
    
    sns.countplot(data = df, x = feature, hue = target)
    
    return plt.show()


def catplt(df, target, feature):
    
    sns.catplot(data= df, x= target, y= feature, kind = 'bar')
    
    return plt.show()


def corr(x, y):

    corr, p = stats.pearsonr(x, y)

    return corr, p


def chi(df, target, feature):
    
    cross_tab = pd.crosstab(df[target], df[feature])

    chi2_stat, p_val, dof, expected = stats.chi2_contingency(cross_tab)

    print("Chi-Square Statistic:", chi2_stat)
    print("P-value:", p_val)
    print("Degrees of Freedom:", dof)
    print("Expected Frequencies:\n", expected)
    print('')

    if p_val < 0.05:
    
        print("Conclusion: There is a significant association between the variables. We reject the null hypothesis")

    else:
    
        print("Conclusion: There is no significant association between the variables. we fail to reject the null hypothesis")

        

def one_samp_t(sample, overall_mean):

    t, p = stats.ttest_1samp(sample, overall_mean)

    print(t, p/2)
    print('')

    a =.05

    if p/2 > a:
    
        print("Conclusion: We fail to reject the null hypothesis.")

    elif t < 0:
    
        print(" Conclusion: We fail to reject null hypothesis.")

    else:
    
        print("Conclusion: We reject the null hypothesis.")