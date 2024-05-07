# Analysis of Unemployment Rate

---

## Authors:
- Jiahe Wei (wei51)
- Zisong Ma (zisongm2)
- Zhen Li (zhenli6)

---

## Table of Contents
1. [Overview](#overview)
2. [Environment Setup](#environment-setup)
3. [Analysis](#analysis)
   - Validation of Hypothesis 1: The unemployment rate in the United States is independent of Age
   - Expansion on Hypothesis 1: Unemployment RATE in the United States
   - Expansion on Hypothesis 1 (Continue): Unemployment Rate in the European Union is independent of Age
   - Validation of Hypothesis 2: The unemployment rate in the United States is Independent of Race
   - Expansion on Hypothesis 2: Unemployment Rate in the U.K. is independent of Race
   - Validation of Hypothesis 3: Unemployment rate in the United States is independent of Education Level
   - Expansion on Hypothesis 3: Unemployment Rate in the European Union is independent of Education Level
   - Expansion on Hypothesis 3 (Continue): The Unemployment Rate detail about countries with relatively high employment-education equity in the European Countries
   - Expansion on Hypothesis 3 (Continue): The Unemployment Rate is independent of average educated years in China
   - Validation of Hypothesis 7: There is no relationship between Gross Domestic Product (GDP) and Unemployment Rate
   - Expansion on Hypothesis 7: The relationship between Gross Domestic Product (GDP) growth and Unemployment Rate
   - Expansion on Hypothesis 7 (Continue): There is no relationship between Gross Domestic Product (GDP) and Unemployment Rate of European Union
   - Validation of Hypothesis 8: There is no relationship between the President's Political Party and Unemployment Rate
   - Validation of Hypothesis 9: Relation between Population and the Unemployment Rate
   - Expansion on Hypothesis 9: But given the huge size of the population, annual changes in population size may be difficult to detect directly by looking at changes in the total population. So I first calculated the growth rate of the population and followed it to observe the relationship between population change and unemployment rate
   - Expansion on Hypothesis 9 (Continue): There is a relationship between population growth rate and Unemployment Rate of European Union
   - Hypothesis 10: There is a relationship between minimum wage and unemployment rate
4. [Data Sources](#data-sources)
5. [Unit Tests for the DownloadTable Function in Scraper](#unit-tests-for-the-downloadtable-function-in-scraper)
6. [Contribution](#contribution)

---

## Overview
This project is built upon a [previous project](https://github.com/Ankita-Khiratkar/2021Fall_finals) in 2021 Fall IS597 
course by Ankita Khiratkar (aak13) and Divyaang Agarwal (dagarw5).
In their work, they have analyzed the unemployment rate of the United States from several aspects, we want to perform analysis
with the most up-to-date data from the same aspects to see if their hypothesis is still valid.
(since now is 3 years after their work and the relevant dataset should be updated).
Furthermore, we also performed analysis from other aspects that they did not consider, to expand the breath of the analysis.

---

## Environment Setup

To replicate the Conda environment, follow these steps:

1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/individual) if you haven't already.
2. Clone the repository or download the project files, including the `environment.yml` file.
3. Open your terminal and navigate to the project directory.
4. Create the Conda environment by running:

   ```bash
   conda env create -f environment.yml
5. Activate the environment:

   ```bash
   conda activate env-name
6. You are now ready to run the project files. Our main work are in the three jupyter notebook files: `Final_project_zl.ipynb`, `Final_project_wjh.ipynb`, and `US_Industry_Analysis.ipynb`.

---
## Analysis
### Vlidation of Hypothesis 1: The unemployment rate in the United States is independent of Age
This part is for validating the hypothesis 1 made in previous work using the most up-to-date dataset (till year 2024). <br>
They have the following hypothesis:
**Null Hypothesis: Unemployment rate in the United States is independent of Age
Alternative Hypothesis: Unemployment rate in the United States is NOT independent of Age**

<img alt="US unemployment level with age.png" src="./chart/US unemployment level with age.png" title="US unemployment level with age"/>

### Observation
The conclusion of previous project is that Unemployment rate is highest for the age group 16 to 24 years followed by 25 
to 34 years, then 35 to 44 years, then 45 to 54 years, followed by 55 to 64 years, and lastly 65 years and above. 
Unemployment rate in the United States is not independent of age group. The null hypothesis is rejected.

I assume the conclusion made in previous work is **valid** for now.

### Expansion on Hypothesis 1: Unemployment RATE in the United States
For the expansion of the hypothesis 1, I will first analyze the unemployment rate of the United States. 
Since the previous work was performed on the unemployment level dataset which represents the change of 
number of unemployed people, but there is no visualization of the proportion of unemployed people in the 
total population. Therefore, I will perform analyze on the unemployment rate dataset which represents 
the proportion of unemployed people in the total population.

<img alt="US Unemployment Rate with age.png" src="./chart/US Unemployment Rate with age.png" title="US Unemployment Rate with age"/>

### Observation
If we compare with the plot derived from unemployment level associated with age groups, we can see there are differences. 
Although the age group '16-24' years still shows a high value in both unemployment level and unemployment rate, the other 
groups does not show a clear trend that the unemployment rate is inversely proportional to the age group. Most of the 
lines are pretty close, or even intersect multiple times at some time point.

Therefore, this is a **weakness** of the previous analysis. The majority reason of causing this weakness is that their 
hypothesis is not based on precisely matched dataset. Overall, the  conclusion unemployment rate is not independent of 
age is still **valid** since we can see from the '16-24' age groups.

### Expansion on Hypothesis 1 (Continue): Unemployment Rate in the European Union is independent of Age
This part is to check whether the unemployment rate in the European Union is independent on the Age of individuals.

We have the following hypothesis:
**Null Hypothesis: Unemployment rate in the European Union is independent of Age.
Alternative Hypothesis: Unemployment rate in the European Union is NOT independent of Age.**

<img alt="European Unemployment Rate with Age.png" src="./chart/European Unemployment Rate with Age.png" title="European Unemployment Rate with Age"/>

### Observation
* From the plot derived from the unemployment rate associated with age groups in the European Union, we can see that the unemployment rate is not independent of age group. The age group '15-24' years shows a high value in unemployment rate, which is similar to the United States. the other age groups also show a similar trend that the unemployment rate is inversely proportional to the age group. 

* **Conclusion:** the unemployment rate in the European Union is not independent of age group. The null hypothesis is rejected.  

### Vlidation of Hypothesis 2: The unemployment rate in the United States is Independent of Race
This part is for validating the hypothesis 2 made in previous work using the most up-to-date dataset (till year 2024). <br>
They have the following hypothesis:

**Null Hypothesis: Unemployment rate in the United States is independent of Race <br>
Alternative Hypothesis: Unemployment rate in the United States is NOT independent of Race**

<img alt="US Unemployment Rate with Race.png" src="./chart/US Unemployment Rate with Race.png" title="US Unemployment Rate with Race"/>

### Observation
The plot shows unemployment rate is highest for Black Americans followed by Hispanic or Latino then White and then Asians. 

Therefore, we can unemployment rate is not independent of race, the conclusion made in previous work is **valid** for now.

One particular detail I could see from here is that, no matter what race group, the unemployment rate almost drop to the lowest point after the end of COVID-19 pandemic, compared to previous 40 years. The reason might be thanks to the recover of economic after pandemic, which is a notable observation.

### Expansion on Hypothesis 2: Unemployment Rate in the U.K. is independent of Race
This part is to check whether the unemployment rate in the United Kingdom is independent on the Race of individuals.

We have the following hypothesis:
**Null Hypothesis: Unemployment rate in the United Kingdom is independent of Race.
Alternative Hypothesis: Unemployment rate in the United Kingdom is NOT independent of Race.**

<img alt="UK Unemployment Rate with Race.png" src="./chart/UK Unemployment Rate with Race.png" title="UK Unemployment Rate with Race"/>

### Observation
The plot shows unemployment rate is always low for White. In most of the time, Black holds the highest unemployment rate among those groups.

Therefore, we can say unemployment rate is not independent of race in the United Kingdom, the **null hypothesis is rejected**. The trend we observed is similar to the United States.

One interesting observation is that the unemployment rate in the U.K. seems no increase during the COVID-19 pandemic, which is different from the United States. The reason might be the different policies and economic conditions in the two countries.

### Validation of Hypothesis 3: Unemployment rate in the United States is independent of Education Level
This part is for validating the hypothesis 3 made in previous work using the most up-to-date dataset (till year 2024). <br>
They have the following hypothesis:

**Null Hypothesis: Unemployment rate in the United States is independent of Race <br>
Alternative Hypothesis: Unemployment rate in the United States is NOT independent of Race**

<img alt="US Unemployment Level with Education.png" src="./chart/US Unemployment Level with Education.png" title="US Unemployment Rate with Education"/>

### Observation
The plot shows that the unemployment rate is inversely related to the education level. Even after experiencing the impact of the COVID-19 pandemic on the job market.Unemployment rate still persist the trend that is lower for those with higher education level.

Therefore, we can unemployment rate is not independent of educational level, the conclusion made in previous work is **valid** for now.

### Expansion on Hypothesis 3: Unemployment Rate in the European Union is independent of Education Level
This part is to check whether the unemployment rate in the European Countries is independent on the education level of individuals.

We have the following hypothesis:
**Null Hypothesis: Unemployment rate in the European Countries is independent of Education Level.
Alternative Hypothesis: Unemployment rate in the European Countries is NOT independent of Education Level.**

<img alt="European Unemployment Rate by Education Level.png" src="./chart/European Unemployment Rate by Education Level.png" title="European Unemployment Rate by Education Level"/>

### Observation
The plot shows unemployment rate is always low for group with less than a high school diploma in most of those European Countries. If we look at the detail, we could observe the trend that the unemployment rate is inversely related to the education level.

Therefore, we can say unemployment rate is inversely related to the education level for European Countries. the **null hypothesis is rejected**. The trend we observed is similar to the United States.

### Expansion on Hypothesis 3 (Continue): The Unemployment Rate detail about countries with relatively high employment-education equity in the European Countries
Using standard deviation as a measure to show how spread out the unemployment rates are for different education levels within each country. A smaller standard deviation would indicate that the unemployment rates are more uniform across different education levels, suggesting higher equity.

<img alt="Unemployment Rate in Iceland by Education Level.png" src="./chart/Unemployment Rate in Iceland by Education Level.png" title="Unemployment Rate in Iceland by Education Level">
<img alt="Unemployment Rate in Luxembourg by Education Level.png" src="./chart/Unemployment Rate in Luxembourg by Education Level.png" title="Unemployment Rate in Luxembourg by Education Level">
<img alt="Unemployment Rate in Netherlands by Education Level.png" src="./chart/Unemployment Rate in Netherlands by Education Level.png" title="Unemployment Rate in Netherlands by Education Level">
<img alt="Unemployment Rate in UK by Education Level.png" src="./chart/Unemployment Rate in UK by Education Level.png" title="Unemployment Rate in UK by Education Level">

### Observation
The plot shows that the unemployment rate is relatively low for all education levels in those countries. Even though among those countries, the unemployment rate is still related to the education level. As we can see most of the time, the unemployment rate is always higher for those with less than a high school diploma. One exception is Iceland, there shows no obvious unemployment rate difference among different education level groups.

Also, the unemployment rate in those countries did not show a significant fluctuation during the COVID-19 pandemic, which is different from the United States. Seems like the job market circumstance in those countries is more stabled during the pandemic.

### Expansion on Hypothesis 3 (Continue): The disparity difference of Educational-Level-associated Unemployment Rate in the United States and Iceland 
Since we found that Iceland has the least disparity between different education-level groups. We want to see how the United States' disparity compared with Iceland over time.

<img alt="US Iceland std of Unemployment Rate.png" src="./chart/US Iceland std of Unemployment Rate.png" title="US Iceland Standard Deviation of Unemployment Rate across Education Level">

### Expansion on Hypothesis 3 (Continue): The Unemployment Rate is independent of average educated years in China
This part is to check whether the unemployment rate in the China is independent of the average educated years of individuals.

We have the following hypothesis:
**Null Hypothesis: Unemployment rate in China is independent of average educated years.
Alternative Hypothesis: Unemployment rate in China is NOT independent of average educated years.

<img alt="China Unemployment Rate by Average Educated Year.png" src="./chart/China Unemployment Rate by Average Educated Year.png" title="China Unemployment Rate by Average Educated Year">

### Observation
The plot shows that the unemployment rate is not independent of the average educated years in China. As the average educated year is increasing, the unemployment rate is decreasing annually in China. The unemployment rate is inversely related to the average educated years. 
The null hypothesis is **rejected**.
One interesting observation is the there shows a drop in the average educated year and an increase in the unemployment rate in 2020, which is different from the trend in other years. The reason might be the impact of the anti-covid policy in China.


### Vlidation of Hypothesis 7: There is no relationship between Gross Domestic Product (GDP) and Unemployment Rate
This part is for validating the hypothesis 1 made in previous work using the most up-to-date dataset (till year 2024).

They have the following hypothesis: 

Null Hypothesis: There is NO relationship between Gross Domestic Product (GDP) and Unemployment Rate

Alternative Hypothesis: There is relationship between Gross Domestic Product (GDP) and Unemployment Rate

<img alt="USA Unemployment Rate.png" src="./chart/USA Unemployment Rate.png" title="USA Unemployment Rate"/>

### Observation
1.From the above plot, we observe that the unemployment rate is inversely related to the GDP. Notice, whenever the GDP increases and the unemployment rate decreases.

2.Around 2003 and during the Great Recession in 2008, there was a slight decrease in the GDP of United States and during both the times we notice that the unemployment rate increases.

3.Thus, we conclude that there is a relationship between the Gross Domestic Product (GDP) and the Unemployment Rate, and we reject the null hypothesis.

I assume the conclusion made in previous work is valid for now. Because the exact amount of GDP is too large and not easy to observe changes from one year to the next. Therefore, I calculated the annual growth rate to better reflect the relationship between the rate of change and the unemployment rate.

### Expansion on Hypothesis 7:
The relationship between Gross Domestic Product (GDP) growth and Unemployment Rate.   

Instead of looking directly at total GDP and the unemployment rate, it is easier to see the relationship between them by calculating the annual GDP growth.

<img alt="USA Unemployment Rate Growth.png" src="./chart/USA Unemployment Rate Growth.png" title="USA Unemployment Rate Growth"/>

### Observations
From the above graph we can easily see that unemployment rate is inversely proportional to GDP. Note that whenever GDP increases, the unemployment rate decreases.

The GDP of the United States declined slightly around 2003 and during the Great Recession of 2008, and we note that the unemployment rate increased during both of these periods.

During the Covid_19 around 2019, the rapid increase in unemployment was accompanied by a relatively large decrease in DGP.

### Expansion on Hypothesis 7 (Continue): There is no relationship between Gross Domestic Product (GDP) and Unemployment Rate of European Union
Through this hypothesis we aim to check whether there is a relationship between the European Union Gross Domestic Product (GDP) and Unemployment Rate or not. And similarly, I have calculated the annual GDP growth rate from the GDP data and compared the relationship between the GDP growth rate and the unemployment rate.

We test the following hypothesis:

Null Hypothesis: There is NO relationship between Gross Domestic Product (GDP) and Unemployment Rate

Alternative Hypothesis: There is relationship between Gross Domestic Product (GDP) and Unemployment Rate

<img alt="European union Unemployment Rate.png" src="./chart/European union Unemployment Rate.png" title="European union Unemployment Rate"/>
<img alt="European union Unemployment Rate Growth.png" src="./chart/European union Unemployment Rate Growth.png" title="European union Unemployment Rate Growth"/>

### Observations
The EU GPD data seems to be more volatile than the US GDP data.

Unlike the US data, it seems difficult to detect a clear relationship between GDP and unemployment in the EU data.

But probably because this is the EU GDP data as a whole, it is affected by each EU member state. For example, we can observe that in 2015, the Greek debt crisis had a huge impact on the GDP of the EU as a whole.



### Vlidation Hypothesis 8: There is no relationship between the President's Political Party and Unemployment Rate
Through this hypothesis we aim to check whether there is a relationship between the President's Political Party and Unemployment Rate.

They have the following hypothesis:

Null Hypothesis: There is NO relationship between President's Political Party and the Unemployment Rate

Alternative Hypothesis: There is relationship between President's Political Party and the Unemployment Rate

<img alt="USA Politicial Party.png" src="./chart/USA Politicial Party.png" title="USA Politicial Party"/>


### Observation
Though there are many factors that contribute to the Unemployment rate in the country, from the above plot we notice that most of the times when Democratic Party's President was in power, the unemployment rate reduced. But, there are also some instances when the unemployment rate increased under Democratic Party like in the year 1961, 1980, and 2009.

While in the rule of Republican party, we observe that the unemployment rate trend is random.

Thus, we can say that there is no relationship between the President's Political Party and the Unemployment Rate in the United States and we accept the null hypothesis.

There is nothing wrong with their results, but perhaps the final results that show up are not very obvious because there is so much correlation between political parties and unemployment. And there is no similar ruling party in the EU organization, so it is abandoned to do the expansion of hypothesis8.

### Vlidation Hypothesis 9: Relation between Population and the Unemployment Rate

They have the following hypothesis:   

Null Hypothesis: There is NO relationship between the population and the Unemployment Rate

Alternative Hypothesis: There is relationship between the population and the Unemployment Rat

<img alt="Midwest Region Unemployment rate.png" src="./chart/Midwest Region Unemployment rate.png" title="Midwest Region Unemployment rate"/>
<img alt="NorthEAST Region Unemployment rate.png" src="./chart/NorthEAST Region Unemployment rate.png" title="Northeast Region Unemployment rate"/>
<img alt="South Region Unemployment rate.png" src="./chart/South Region Unemployment rate.png" title="South Region Unemployment rate"/>
<img alt="West Region Unemployment rate.png" src="./chart/West Region Unemployment rate.png" title="West Region Unemployment rate"/>


### Observation:
The barplots above represents the mean of the unemployment rates of all states in a region and sum of the population (x10^7) for all the states in that region.

From the barplots above we notice that in Midwest and Northeast region there is not much significant change in population over the years (2011-2020) while for South and West region there is a notable increase in population in these years. But we notice that for all the regions the unemployment rate decreases from 2011 to 2019.

In 2020, due to the Covid-19 pandemic there is a rise in the unemployment rate for all the regions in the United States.

For Hypothesis 9, I calculated the population growth rate and compared the relationship between unemployment rates due to the large and insignificant changes in the population.

### Expansion on Hypothesis 8：
But given the huge size of the population, annual changes in population size may be difficult to detect directly by looking at changes in the total population. So I first calculated the growth rate of the population and followed it to observe the relationship between population change and unemployment rate.

<img alt="Midwest Region Unemployment rate growth.png" src="./chart/Midwest Region Unemployment rate growth.png" title="Midwest Region Unemployment rate growth"/>
<img alt="Northeast Region Unemployment rate growth.png" src="./chart/Northeast Region Unemployment rate growth.png" title="Northeast Region Unemployment rate growth"/>
<img alt="South Region Unemployment rate growth.png" src="./chart/South Region Unemployment rate growth.png" title="South Region Unemployment rate growth"/>
<img alt="West Region Unemployment rate growth.png" src="./chart/West Region Unemployment rate growth.png" title="West Region Unemployment rate growth"/>

### Observation:
By looking at the Midwestern, Northeastern, and Southern regions of the United States, you can actually see that there are some connections between them.

The population growth rate is affected by the unemployment rate. When the unemployment rate increased rapidly during 2020, the population growth rate also witnessed an increase the following year.

The population growth rate appears to be positively related to the unemployment rate, but changes in population will respond more slowly than the unemployment rate.

Therefore, we reject the null hypothesis that there is a relationship between population and unemployment.

### Expansion on Hypothesis 9 (Continue): There is a relationship between population growth rate and Unemployment Rate of European Union

Null Hypothesis: There is NO relationship between the population and the Unemployment Rate

Alternative Hypothesis: There is relationship between the population and the Unemployment Rate

<img alt="European union Unemployment Rate and Population.png" src="./chart/European union Unemployment Rate and Population.png" title="European union Unemployment Rate and Population.png"/>
<img alt="European union Population Growth and Unemployment Rates.png" src="./chart/European union Population Growth and Unemployment Rates.png" title="European union Population Growth and Unemployment Rates"/>


### Observation:
Look at the European data reveals that there is also some influential relationship between the population growth rate and the unemployment rate.

The relationship seems to be the same as that shown in the United States: there is a positive relationship between the unemployment rate and the population growth rate, but the population growth rate takes longer to reflect this than the unemployment rate.

Therefore, we reject the null hypothesis that there is a relationship between population and unemployment.


### Hypothesis 10: There is a relationship between minimum wage and unemployment rate The purpose of this hypothesis is to test whether there is a relationship between the minimum wage and the unemployment rate for USA and European Union

We test the following hypothesis:

Null Hypothesis: There is a relationship between the minimum wage and the unemployment rate.

Alternative hypothesis: There is no relationship between the minimum wage and the unemployment rate.

<img alt="USA minimum Wage and Unemployment Rate.png" src="./chart/USA minimum Wage and Unemployment Rate.png" title="USA minimum Wage and Unemployment Rate"/>

### Observation
According to the chart, we can clearly find that there is a positive relationship between the minimum wage and the unemployment rate in the United States. However, it seems difficult to distinguish the order of causality between them.   

It can be seen that the minimum wage in the United States reached its highest value in 2010, and has been in a downward trend since then.   

As a result of the impact of Covid-19, the U.S. minimum wage has been declining more and more rapidly in recent years.   

Thus, we can say that there is relationship between the minimum wage and the Unemployment Rate in the United States and we accept the null hypothesis.

<img alt="European union minimum Wage and Unemployment Rate.png" src="./chart/European union minimum Wage and Unemployment Rate.png" title="European union minimum Wage and Unemployment Rate"/>

### Observation
According to the graph, we can see that the minimum wage in the European Union has been in a steady upward trend until recently, when it declined a little bit. However, the overall amount is still lower than that of the United States. 

However, we can find that there is some influence between the minimum wage and the unemployment rate in the European Union, in the interval of 2004 to 2008 and 2013 to 2019, the rapid decline in the unemployment rate will lead to a rapid increase in the minimum wage.

During periods of rising unemployment, the minimum wage rises very slowly.

Thus, we can say that there is relationship between the minimum wage and the Unemployment Rate in the European Union and we accept the null hypothesis.

---


# Data Sources:
* https://data.bls.gov/PDQWeb/ln
* https://ec.europa.eu/eurostat/databrowser/view/tepsr_wc170__custom_11059624/default/table?lang=en
* https://www.ethnicity-facts-figures.service.gov.uk/work-pay-and-benefits/unemployment-and-economic-inactivity/unemployment/latest/#data-sources
* https://www.ons.gov.uk/employmentandlabourmarket/peoplenotinwork/unemployment/timeseries/mgsx/lms
* https://stats.oecd.org/viewhtml.aspx?datasetcode=EAG_NEAC&lang=en# 
* https://www.stats.gov.cn/sj/   
* https://www.census.gov/programs-surveys/popest/technical-documentation/research/evaluation-estimates/2020-evaluation-estimates/2010s-state-total.html   
* https://www.bls.gov/charts/state-employment-and-unemployment/state-unemployment-rates-animated.htm


---

## Unit Tests for the `DownloadTable` Function in Scraper

The unit tests designed for the `DownloadTable` function cover various scenarios to ensure the function behaves as expected under different conditions:

1. **File Already Exists Test**:
   - This test verifies the behavior of the `DownloadTable` function when the target file already exists in the specified directory. The expected behavior is that the function should return immediately without performing any download actions. The `os.path.exists` function is mocked to return `True` to simulate the scenario where the file already exists.

2. **Successful Download Test**:
   - This test checks if the function correctly handles file downloads when all parameters are correct, and the network request succeeds. `requests.get` is mocked to return a successful response (HTTP status code 200), and the test checks if the function executes correctly without returning any errors. File writing operations are simulated using `mock_open`.

3. **Retry Logic Test**:
   - This test assesses whether the function properly retries the download attempt when it fails (due to network issues or server errors, for example). In this scenario, `requests.get` is set with a `side_effect` to return several failed responses (HTTP status code 404) consecutively, and the test verifies if the function retries the specified number of times. This test ensures that the retry mechanism works correctly in response to download failures.

These tests are intended to guarantee that the `DownloadTable` function operates reliably across different scenarios, helping to prevent issues during practical usage.

--- 
## Contribution
* Zhen Li:
  - Final_project_zl.ipynb
  - utils.py
* Jiahe Wei:
  - Final_project_wih.ipynb
  - main.py
* Zisong Ma:
  - US_Industry_Analysis.ipynb
  - BLS_scraper_with_tests.py