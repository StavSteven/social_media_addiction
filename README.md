# Social media addiction

![social media header](images/readme_header.jpg)

Project bookmarks:

-   [README](/README.md)
-   [Project board](https://github.com/users/StavSteven/projects/10)
-   [Raw data](/data/raw_data/student_social_media_addiction.csv) | [Clean data](/data/cleaned_data/student_social_media_addiction_cleaned.csv)
-   [ETL Notebook](/jupyter_notebooks/1_data_cleaning_student_social_media_addiction.ipynb)
-   [Visualisation & Statistical analysis Notebook](/jupyter_notebooks/2_visualisations_student_social_media_addiction.ipynb)
-   [Machine Learning Notebook](/jupyter_notebooks/3_machine_learning.ipynb)
-   [Power BI dashboard](/dashboard/social_media_addiction_dashboard.pbix)
-   [Conclusion and discussion](#conclusion-and-discussion)

## Contents

1. [Project Overview](#project-overview)
2. [Dataset Content](#dataset-content)
3. [Business Requirements](#business-requirements)
4. [Hypothesis Testing and Validation](#hypothesis-testing-and-validation)
5. [Rationale to map business requirements](#rationale-to-map-business-requirements)
6. [Project plan](#project-plan)
7. [Data Analysis Methods Used](#data-analysis-methods-used)
8. [Development Roadmap](#development-roadmap)
9. [Deployment](#deployment)
10. [Main Data Analysis Libraries](#main-data-analysis-libraries)
11. [Conclusion and discussion](#conclusion-and-discussion)
12. [Limitations in the data](#limitations-in-the-data)
13. [Overall summary](#overall-summary)
14. [Credits](#credits)
15. [Acknowledgements](#acknowledgements)

## Project overview

This project focuses on exploring the relationship between an student's social media habits and their wider life, how does it affect their sleep, their mental health and does it have an effect on their academic studies and are they ready to accept that they're addicted to social media?

## Dataset Content

The student social media dataset was sourced from Kaggle: https://www.kaggle.com/datasets/adilshamim8/social-media-addiction-vs-relationships

It contains records of students ranging from 18-25, from all over the world. It records their social media usage, preferred platform, health and relationship dynamics.

| Field Name                     | Description                                                                               |
| ------------------------------ | ----------------------------------------------------------------------------------------- |
| `new_student_id`               | Unique identifier for each student in the dataset.                                        |
| `age`                          | Age of the student (in years).                                                            |
| `gender`                       | Gender of the student (e.g., Male, Female, Other).                                        |
| `relationship_status`          | Current relationship status (e.g., Single, In a Relationship, Married).                   |
| `academic_level`               | Student's education level (e.g., High School, Undergraduate, Graduate).                   |
| `country`                      | Country where the student resides.                                                        |
| `continents`                   | Continent corresponding to the student's country.                                         |
| `most_used_platform`           | Social media platform the student uses most frequently.                                   |
| `average_daily_usage_minutes`  | Average time spent on social media per day (in minutes).                                  |
| `average_daily_use_by_hour`    | Distribution of social media usage across hours of the day.                               |
| `sleep_per_night_minutes`      | Total sleep time per night (in minutes).                                                  |
| `sleep_hours_per_night`        | Total sleep time per night (in hours).                                                    |
| `conflicts_over_social_media`  | Indicates whether social media usage causes conflicts in personal relationships (Yes/No). |
| `affects_academic_performance` | Indicates whether social media usage negatively affects academic performance (Yes/No).    |
| `addicted_score`               | Score measuring the level of social media addiction (based on survey responses).          |
| `mental_health_score`          | Score measuring mental health status or impact (based on survey responses).               |

## Business requirements

There were no business requirements supplied with this dataset so I have created a scenario where the dataset has been provided by a health professional working in education providing wellbeing advice to students.
They have asked to find out how social media activity affects students academic performance, whether there are any other patterns that could provide causation for lower attainment levels and mental health scores. This could highlight a group of students that are at risk and could be targeted for intervention by their educational institution.

## Hypothesis testing and validation

### Format:

-   Hypothesis:  
    H₀ -  
    H₁ -  
    _This will be tested by_

**Result:**

**_Business decision_**

---

-   **Hypothesis 1: Average daily use of social media will have a negative impact on sleep per night.**
    H₀ - Null hypothesis: There is no relationship between average daily social media use and sleep per night.
    H₁ - Alternative Hypothesis Higher average daily social media use has a negative impact on sleep per night.

_This will be tested statistically using spearman's rank and visualised on a scatter plot to see whether there is a relationship between the two values_

**Result:** We can reject the null hypothesis that there is no relationship between daily social media usage and sleep time.
**The correlation score between the two values was -0.81** meaning that in most cases as one value increased the other decreased. An increase in screen time resulted in sleep deficit which could have a knock on effect to academic studies and mental health score, leading to strained relationships with friends, family members and peers.
**With a pval < 0.05 (3.13 × 10⁻¹⁶⁶)** that is below the threshold of 0.05 to reject the null hypothesis and state that the relationship between the two values has not occured by chance.

![Average use of social media versus sleep score](/images/h1_usage_v_sleep.png)

**_Business decision_** There have been many wider studies that show the importance for any individual to get the required amount of sleep (between 6-9 hours per night), no less people in full time education studying for exams. We would recommend people try to cut down on time spent on social media by putting time limits on their apps or staying off their phone close to a sensibly scheduled bedtime.

---

-   **Hypothesis 2: An increased amount of conflicts over social media will lead to a lower mental health score**
    H₀ - Null hypothesis: There is no relationship between conflicts on social media and mental health score
    H₁ - Alternative Hypothesis Having a higher number of conflicts over social media will be associated to lower mental health scores

_This will be tested statistically using spearman's rank and visualised on a violin plot to determine whether there is a relationship between the two values_

**Result:** We can reject the null hypothesis that there is no relationship between an increase in social media conflicts having no bearing on mental health scores.
**The correlation score between the two values was -0.91.** This means there is strong correlation between the two values, individuals that find themselves getting into public spats on social media often see their mental health suffer as a result.
**With a pval < 0.05 (4.49 × 10⁻²⁶⁶)** we can reject the null hypothesis that there is no relationship between the two values.

![Mental health scores versus the number of conflicts on social media](/images/h2_mental_health_conflicts.png)

**_Business decision_** Looking at the violin plot we can see that there is a horrible trend between the two values that as the number of conflicts increases, the range of mental health scores those people have gets progressively lower. The median jumps down an entire mental health score per extra argument, so it pays to use the block button or take timeout instead of getting irate over social media. Lower mental health scores may have consequences beyond social media so it isn't worth getting involved in online spats.

---

-   **Hypothesis 3: TikTok users will have the lowest mental health scores**
    H₀ - Null hypothesis: There is no distinction to be made between the mental health score of TikTok users in comparison to other social media platforms
    H₁ - Alternative Hypothesis TikTok users have a lower mental health score than users who used alternative platforms as their main source of social media

_This will be tested statistically using a Kruskal–Wallis test to compare mental health scores across platforms, supported by a Chi-Square test to examine whether academic performance impact differs between platforms. A Plotly bar chart with line overlay was used to visualise user counts, mental health scores, and reported academic effects._

For this hypothesis, the analysis focused on the three platforms with the largest user counts (TikTok, Instagram, Facebook). Other platforms were excluded from statistical testing due to insufficient sample sizes and unstable average mental health scores.

**Result:** We can reject the null hypothesis as at least one platform differs significantly in mental health scores, supporting the observation that TikTok users experience lower wellbeing.
**The Kruskal-Wallis test returned a H value of 58.90 & pval < 0.05 (1.62 × 10⁻¹³)** together demonstrate that there are differences between the platform user's mental health scores that are far too large to be random variation. The larger the H value indicates stronger evidence that at least one group differs.
As I have included whether specific platforms have effected academic performance on the plot then it made sense to carry out a statistical test on that too.
**The Chi-Square test returned a χ² value of 257.82 & pval < 0.05 (6.43 × 10⁻⁴⁹)** This result means that there is link between platform and impact on academic studies. That TikTok users are far more likely to report an impact on their studies than users of other social media sites. TikTok users demonstrated both the lowest mental health scores and the highest rate of reported academic impact (93.46%), compared with (68.95%) for Instagram and (30.08%) for Facebook, where a majority of users reported no academic effects. This pattern strongly supports the initial hypothesis.

![Top 3 platforms - Mental health scores & academic studies](/images/top_platform_mental_health_plotly.html)

**_Business decision_** Based on the strong association between TikTok use, reduced mental health scores, and frequent reports of academic disruption, it would be advisable for wellbeing and academic support teams to consider targeted interventions for heavy TikTok users, pointing students in the direction of wellbeing services to raise awareness of the importance of balance between online and offline. Reducing excessive TikTok consumption may help improve both mental wellbeing and academic performance.

---

-   **Hypothesis 4: Addiction level has an impact on sleep duration**
    H₀ – Null hypothesis: Addiction level has little to no impact on sleep duration.
    H₁ – Alternative hypothesis: Higher addiction levels will reduce sleep duration.

_This will be tested statistically using Spearman’s rank correlation to assess the relationship between addiction level and sleep duration. The relationship will also be visualised using a combined boxplot and strip plot to show both the distribution and individual data points._

A strip plot was used to show each user’s sleep duration against their addiction score. Because this created a dense cluster of datapoints, a boxplot was added in the background to highlight the median and interquartile ranges for each sleep-duration group.

**Result:** We can reject the null hypothesis, as the data demonstrates that sleep duration decreases as addiction levels rise.
**The correlation score between the two values was -0.79**, indicating a strong negative relationship: individuals with higher addiction levels consistently report fewer hours of sleep.
**With a pval < 0.05 (2.44 × 10⁻¹⁴⁸)** far below the significance threshold there is extremely strong evidence that elevated social media addiction levels are associated with reduced sleep duration. The visualisation supports this finding, showing that users sleeping fewer than 5 hours per night cluster around higher addiction scores with a narrower range, while those sleeping more exhibit lower and more varied addiction levels.

![Addiction level versus sleep score](/images/h4_addiction_v_sleep.png)

**_Business decision_** Given the strong negative association between addiction levels and sleep duration, wellbeing and academic support teams should consider targeted guidance to help students manage excessive social media use, particularly late-night scrolling. Recommendations may include digital curfews, app timers, or structured bedtime routines. Improving sleep hygiene for highly addicted users could support better mental health, higher academic performance, and overall wellbeing.

---

![Hypotheses dashboard](images/hypotheses_dashboard.png)

# Summary of findings v hypothesis

| Hypothesis                                     | Statistical Test            | Statistic / Correlation | p-value       | Interpretation / Result                             |
| ---------------------------------------------- | --------------------------- | ----------------------- | ------------- | --------------------------------------------------- |
| H1: Higher daily social media use → less sleep | Spearman's rank correlation | ρ = -0.813              | 3.13 × 10⁻¹⁶⁶ | Strong negative correlation, reject H₀              |
| H2: More conflicts → lower mental health       | Spearman's rank correlation | ρ = -0.908              | 4.49 × 10⁻²⁶⁶ | Strong negative correlation, reject H₀              |
| H3: TikTok users have lowest mental health     | Kruskal–Wallis H-test       | H = 58.90               | 1.62 × 10⁻¹³  | Significant difference between platforms, reject H₀ |
| H4: Higher addiction → less sleep              | Spearman's rank correlation | ρ = -0.786              | 2.44 × 10⁻¹⁴⁸ | Strong negative correlation, reject H₀              |

---

## Project plan

![Project board](/images/project_board.png)

This project followed a structured data analytics workflow designed to ensure the dataset was handled consistently from collection through to interpretation, implementing data analysis best practices, GDPR regulation and taking an ethical approach to handling the data. The steps below outline the process and the rationale behind each stage.

### 1. Data Collection

-   The dataset was sourced from Kaggle and downloaded as a CSV file.
-   The only field that could be used to identify an individual was the student ID so these were modified during the data transformation stage to protect anonyminity.
-   The dataset contained demographic details, social media usage metrics, addiction scores, mental health scores, and behavioural indicators such as sleep duration and academic impact.

### 2. Data preparation

-   Loaded and inspected the dataset using pandas
-   Checked for missing values, duplicates, and inconsistencies in categorical fields.
-   Standardised column names and data types for ease of use.
-   Created additional calculated fields (e.g., converting minutes to hours).

### 3. Exploratory data analysis (EDA)

-   Generated summary statistics and visualised distributions to understand the shape of the data and outliers.
-   Explored initial relationships using scatter plots, violin plots and strip plots
-   This stage helped guide which hypotheses to test and confirmed that non-parametric methods were more suitable due to skewed data and inconsistent group sizes.

### 4. Hypothesis testing and statistical analysis

-   Used statistical tests such as Spearman’s rank, Kruskal–Wallis and Chi-Square tests to assess relationships and comparisons amongsts different fields in the dataset.
-   These were selected because they do not assume normality and are appropriate for survey-based, unevenly distributed data.

### 5. Interpretation of findings

-   Created user friendly plots using Seaborn, Matplotlib and Plotly, including boxplots, scatter plots, violin plots, and bar charts.
-   Visualisations were used alongside statistical output to provide intuitive explanations of trends.
-   Dashboard created to allow business user to drill down on specific variables to visualise their own findings.
-   Combined statistical and visual elements to provide evidence of findings to reject null hypotheses.
-   Compared findings to identify consistent trends within clusters of points in ml learning model

### 6. Reporting and documentation

-   Consolidated analysis into a structured README with clear sections for hypotheses, methodology, results, limitations, and business decisions.
-   Ensured all steps were reproducible by documenting the code workflow and visual outputs.

### 7. Justifications of methodology

-   The dataset consists mainly of ordinal and non-normal distributions, meaning non-parametric tests (Spearman, Kruskal–Wallis, Chi-Square) are appropriate.
-   Correlation tests were chosen to quantify direction and strength of relationships identified in EDA.
-   Group-comparison tests were selected where platform-based behavioural differences were expected.
-   Visual methods (strip plots, boxplots, violin plots) were chosen because they communicate both the distribution and concentration of responses clearly, especially for survey datasets.
-   The combination of statistical tests and visual analysis ensured findings were interpretable by both technical and non technical users

---

## Rationale to map business requirements

This project’s data visualisations were designed to support the wellbeing professional’s core business requirements by transforming the dataset into meaningful, actionable insights. Each visual was selected to answer a specific analytical question related to student mental health, sleep quality, social media behaviour, and academic impact.

Below is an outline of each requirement and the rationale behind the chosen visual approach.

### 1. Identify and visualise factors that negatively affect student wellbeing and academic performance

Visualisations used:

-   Scatterplots (e.g., social media usage vs. sleep duration)
-   Correlation analysis heatmaps
-   Violin and box plots showing mental health distributions
-   Strip plots illustrating addiction levels across sleep categories

Rationale:
These visuals make it possible to pinpoint which behaviours strongly associated with poor sleep, lower mental health, or academic disruption. These include heavy social media use, addiction score, frequency of conflicts.
The combination of correlations and distribution-based plots highlights both strength and shape of these relationships, helping the wellbeing professional understand the root drivers of risk to student's health and academic attainment.

### 2. Provide actionable wellbeing insights for educational stakeholders

Visualisations used:

-   Mental health vs. conflict violin plots
-   Addiction vs. sleep duration combined box/strip plots
-   Scatterplots showing sleep deficits linked to excessive usage

Rationale:
These visualisations clearly illustrate patterns that have practical wellbeing implications—such as students losing sleep due to excessive social media use or experiencing deteriorating mental health following repeated online conflicts. This allows wellbeing advisors to make evidence-based recommendations, such as digital curfews, support interventions, or student guidance initiatives.

### 3. Compare trends across different social media platforms

Visualisations used:

-   Bar charts comparing mental health and academic impact across TikTok, Instagram, and Facebook
-   Platform-based score distributions
-   Statistical test (Kruskal–Wallis and Chi-Square)

Rationale:
Platform-level comparisons reveal behavioural and wellbeing differences between user groups, highlighting TikTok users as statistically more vulnerable (lower mental health scores and higher academic disruption). These visuals help stakeholders identify which student segments may require the most targeted support.

### 4. Enable exploration of student behaviour across demographics and wellbeing indicators

Visualisations used:

-   Dashboard (Power BI) with filters for academic level, most used platform country, gender, relationship status
-   Line charts, bar charts, and scatterplots that react dynamically to filters

Rationale:
Interactive filtering allows wellbeing teams and educators to explore patterns across demographic groups or behavioural subgroups—helping them understand whether certain populations face disproportionate risks.
This supports scenario-based insights, enabling institutions to tailor interventions to specific student communities.

### 5. Communicate complex behavioural relationships in an accessible way

Visualisations used:

-   Cleanly annotated scatterplots
-   Intuitive distribution plots (violin, box, strip)
-   Colour-coded bar charts for platform comparisons
-   Dashboard with user-friendly drill-down options

Rationale:
Because the final users may not have statistical or analytical expertise, each visual was designed to be intuitive and self-explanatory. Annotated plots and straightforward layouts communicate findings clearly, supporting fast interpretation without requiring technical background knowledge.

### Summary

Every visualisation in this project was chosen not only to support rigorous statistical analysis, but also to make the findings accessible, interpretable, and actionable for stakeholders in an educational wellbeing context. The mapping from business requirement to visual to insights ensures that each output directly contributes to understanding and improving the wellbeing and academic success of students.

![Dashboard screenshot](/dashboard/dashboard_screenshot1.png)

---

## Data Analysis Methods Used

### Exploratory Data Analysis (EDA)

-   Summary statistics (mean, median, variance)
-   Distribution analysis with histograms and KDE plots
-   Transforming the data
-   Dealing with problem values (nulls and duplicates)
-   Initial relationship exploration using scatterplots, violin plots, and boxplots

### Statistical Analysis

-   Spearman's rank to evaluate relationships between variables
-   Kruskal–Wallis test for comparing scores across platforms
-   Chi-Squared test for categorical associations

### Visual Statistics

-   Scatterplots
-   Violin, strip, and box plots
-   Bar charts and histograms
-   Interactive dashboard

### Machine Learning

-   Pipeline for preprocessing and modelling
-   Dimensionality reduction using PCA
-   Clustering (KMeans)
-   Elbow method and silhouette score
-   Cluster profiling

Note:
No supervised ML models were used as the dataset did not include a target variable.
All analysis focused on pattern discovery rather than prediction.

### Limitations of the Dataset

-   Many variables were ordinal, making parametric tests (like Pearson correlation) inappropriate.
-   Uneven group sizes (e.g., TikTok vs. other platforms) reduced reliability of comparisons.
-   Self-reported values (sleep, mental health, addiction) introduced bias.
-   Dataset captured only a single point in time per student — no causal inference possible.
-   No long-term behaviour tracking, academic grades, or medical/clinical data.
-   Some platforms had extremely small sample sizes, preventing reliable statistical testing.

### Alternative Approaches With Better Data

-   Pearson correlation or linear regression if data were continuous and normally distributed.
-   ANOVA for group comparisons if group sizes were balanced.
-   Time-series analysis if behaviour were tracked over multiple days or weeks.

## How Generative AI Tools Supported Ideation, Design Thinking, and Code Optimisation

### Code Optimisation

-   Suggested more efficient approaches to certain pandas operations.
-   Automated repetitive coding tasks through mapping and vectorised operations.
-   Improved plot readability (colour schemes, axis labelling, layout tweaks).
-   Recommended additional statistical tests appropriate for ordinal data.
-   Helped debug common errors during EDA and visualisation (especially Plotly).

### Documentation & Communication

-   Assisted with ideation and framing of hypotheses.
-   Helped refine research questions and business requirements.
-   Improved clarity, technical tone, and flow across documentation and README.

---

## Ethical considerations

-   Dataset was publicly available on Kaggle
-   The dataset contained no information that could be used to trace any individual
-   Data was used for research and analysis only. There were no GDPR violations
-   Student identifiers were modified during cleaning phase
-   Values were self reported so values such as mental health score, affected academic studies, addiction scores could be inaccurate
-   The dataset features some students as the sole participant from that country
-   Social media platforms weren't equally represented and other categorical imbalances were present
-   As a result wellbeing decisions should not be made solely from clustering, they are behavioural patterns not a diagnosis of any individual
-   Limitations in the dataset have been documented
-   Use of AI has been documented throughout the project

---

## Dashboard design

1. KPI cards (top left)
   These are summaries of the key numerical metrics, mental health score and addiction score. These will be updated when a filter is applied. The gauges were added as a visual aid after receiving feedback from a user asking is the score out of 10, 20, 100?

2. Filters (left side)
   These are drop down filters of key categoricals allowing the user to sort the data by:

-   Academic level
-   Most used platform
-   Country
-   Gender
-   Relationship status

Once selected, all other visuals on the page will update too.

3. Visuals
   Bar and line chart (top centre)
   The chart is reporting the number of conflicts each student has had over social media, they have then been split down into male and female for each number of conflicts. I decided to include a line overlay representing mental health score to demonstrate how that will decline as the number of conflicts increases for the individual.

Bar chart (centre)
This bar chart is to illustrate how behaviour varies across education level, again split up into genders but this time measuring against a self confessed addiction level. It shows that as a person matures they find it easier to not spend as much time on social media, but even graduates have a hard time giving it up totally.

Line chart (bottom centre)
This chart compliments the one above it, showing how wellbeing and online activity change from the ages of 18-24 and how mental health may change as a result. It was a conscious effort made to use the same scales on both y-axis to show the crossover between the sweetspot of good mental health and healthy screen time. Either side of that mental health goes up or down.

Country comparison table (top right)
This table shows the correlation between average mental health score versus addiction score by country. It can be viewed as a standalone table or will be updated as a user drills down on other metrics on the dashboard and will return the top 15 countries. This helps identify the countries with the best and worst behaviours that act as a cause of harm to the individual

Donut charts (bottom right)
Relationship chart was to allow the user the chance to see whether there were any patterns present here when other categoricals were being looked in to. It could be useful for cluster interpretation. On average individuals in a relationship had a better mental health score than those not in a harmonious relationship.

Affected academic status was included for a similar reason to the relationship chart, the user can drill down on other metrics to see what habits can cause the individual to have their studies affected and can they put a plan in place to prevent this level of harm occurring in individuals in future.

### Dashboard improvements

I was fortunate enough to receive feedback from someone who suggested some changes to axis labels, colour schemes and kpi card design to make it more user friendly and keep the results interpretable by both technical and non technical users.

### Communicating Insights to Technical and Non-Technical Audiences

As previously mentioned the dashboard has been designed for non technical users too

The dashboard uses:

-   Simple chart types that can be interpreted easily
-   Clear labels and colour coding
-   High-level KPIs and gauges for quick scanning
-   Logical layout grouped by themes: conflict behaviour, addiction, wellbeing, demographics
-   Interactive filters that allow exploration without statistical knowledge

Without reading any of the raw data or possessing statistical knowledge non technical users can see:

-   More conflicts lead to worse mental health
-   Younger students show different trends
-   Some countries have higher addiction scores

Technical users can see:

-   Multi variable comparisons displayed in the same plot (such as combo charts, dual-axis trends)
-   Strong signal patterns visible in the visuals that support EDA findings
-   Country tables showing exact numerical values

During the design phase I made sure to keep the dashboard:

-   Visual orientated, with minimal text
-   Important metrics are prominently displayed
-   Easy to read colour schemes, trying to stick to two colours

## Unfixed bugs

-   No known unfixed bugs
-   There was an issue with displaying images from image folder in notebooks on github. alt text would appear without the image. I tried different images in different notebooks but it didn't work, the issue was resolved by making my repo public.
-   Plotly plot didn't show up initially so saved as .html and stored in repo.

---

## Development Roadmap

Self relection from my first project:
_I struggled to know what to do with outliers and nulls, not knowing whether to get rid of 145 rows because I didn't know whether that was 'too many' rows to lose and maintain the integrity of the dataset_
During this project I was happy to get rid of outliers to be able to plot accurate findings without rogue values obscuring results. Despite it being a small data set of less than 1000 rows I decided to lose any outliers, and fill in nulls where I could.

_Gaps in my knowledge were evident, where I was not able to retain the information I was able to refer to my notes_
In the time between the first project and now, I have been using resources to further my knowledge. Using websites such as codewars, w3schools and AI to put my skills into practice on small datasets.

Facilitator feedback from my first project:
_Use descriptive lowercase names for repositories, folders and files. Consider adding an image folder to maintain clean and professional structure_
As you can see I have tidied up my repository, consistently using lowercase letters and \_ when naming files and folders as well as housing images and dashboards in their own separate folders for easier navigation.

_Aim for code comments to describe what the code is doing and the markdown to explain why_
I have ensured that every code cell has a #codecomment outlining the purpose of the code and markdown to explain the why. In instances where I am explaining why I'm going to use certain code the markdown has been placed before the code whereas when I'm discussing results the markdown will be put after the plot or code.

Skill development has also been demonstrated by:

-   Using machine learning techniques for the first time, implementing and updating and PCA and KMeans pipeline. Using elbow method and silhouette score to determine optimal number of clusters.
-   One hot encoding. Since the first project I have worked on understanding the methods for encoding categorical data and when to use each method.
-   Creating dashboards was something not required on the first project, nor was it something that I was assigned to do in the group project. I think I have created a powerful dashboard here interpretable by users of all technical levels, grouping together relevant data and putting easy to use filters in place.

After this project I plan to focus my learning on:

-   Continuing to master the skills used to inspect, clean and plot raw data
-   Carry on making dashboards that can be used to present actionable business insights to stakeholders
-   Go over the machine learning modules and work with data that allows me to try an alternative to clusters, perhaps linear regression or classification

---

## Deployment

My Power BI dashboard can be found in the dashboard repository folder along with two screenshots of it in action.
[Dashboard](/dashboard/social_media_addiction_dashboard.pbix)

---

## Main Data Analysis Libraries

| **Library / Package**    | **Purpose in Project**                                                                                                                                                                        |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **pandas**               | Data loading, cleaning, wrangling, handling missing values, and managing tabular datasets.                                                                                                    |
| **numpy**                | Core numerical computations, array manipulation, and support for statistical and ML preprocessing.                                                                                            |
| **matplotlib.pyplot**    | Static visualisations including line charts, bar plots, histograms, and cluster plots.                                                                                                        |
| **seaborn**              | Higher-level statistical visualisations such as violin plots, boxplots, KDE distributions, and heatmaps.                                                                                      |
| **plotly.express**       | Interactive visualisations used throughout the dashboard for exploratory insights.                                                                                                            |
| **plotly.graph_objects** | Advanced, fully customisable interactive figures for dashboards and detailed visual outputs.                                                                                                  |
| **os**                   | Accessing project directories and handling file paths during data loading and export.                                                                                                         |
| **scipy.stats**          | Running statistical tests including Spearman correlation, Kruskal–Wallis, Chi-Squared, t-tests, and ANOVA.                                                                                    |
| **pingouin**             | Additional statistical tools, effect sizes, and non-parametric test support beyond SciPy’s core functions.                                                                                    |
| **scikit-learn**         | Machine learning workflow, including preprocessing, encoding, scaling, dimensionality reduction (PCA), clustering (KMeans), pipeline construction, and cluster evaluation (silhouette score). |

---

## Conclusion and discussion

This project provided an exploration of student social media behaviour using a combination of exploratory data analysis, statistical testing, and unsupervised machine learning. Across the three notebooks, the data was loaded and inspected, before being transformed and plotted to help gain a deeper understanding of behaviours, allowing both high-level insights and interpretations of user groups.

### Summary of findings v hypothesis

Statistical testing & hypothesis validation:

Given the nature of the data, primarily ordinal and not normally distributed, non-parametric tests were used throughout. The statistical analysis led to several important findings:

-   Spearman correlations showed moderate relationships between addiction scores, mental health, and academic performance perception.
-   The Kruskal–Wallis test confirmed that usage patterns and addiction levels differ significantly across social media platforms.
-   Chi-Squared results demonstrated a dependence between academic performance impact and platform used.

These tests validated that behavioural differences were not random and justified the use of unsupervised learning to detect deeper structural patterns.

### Findings

| Hypothesis                                     | Statistical Test            | Statistic / Correlation | p-value       | Interpretation / Result                             |
| ---------------------------------------------- | --------------------------- | ----------------------- | ------------- | --------------------------------------------------- |
| H1: Higher daily social media use → less sleep | Spearman's rank correlation | ρ = -0.813              | 3.13 × 10⁻¹⁶⁶ | Strong negative correlation, reject H₀              |
| H2: More conflicts → lower mental health       | Spearman's rank correlation | ρ = -0.908              | 4.49 × 10⁻²⁶⁶ | Strong negative correlation, reject H₀              |
| H3: TikTok users have lowest mental health     | Kruskal–Wallis H-test       | H = 58.90               | 1.62 × 10⁻¹³  | Significant difference between platforms, reject H₀ |
| H4: Higher addiction → less sleep              | Spearman's rank correlation | ρ = -0.786              | 2.44 × 10⁻¹⁴⁸ | Strong negative correlation, reject H₀              |

### Key behavioural patterns:

-   Platform usage varies significantly across gender and academic level, with Instagram and TikTok dominating among younger users.
-   Sleep duration, mental health scores, and conflict over social media exhibited skewed distributions, requiring careful non-parametric handling.
-   Early variable comparisons hinted at relationships between heavy usage, academic disruption, and self-reported addiction, motivating later hypothesis tests.

### Machine learning model - unsupervised

In my third notebook, a full machine-learning pipeline was constructed to identify meaningful user clusters. PCA reduced the dataset to 10 components, retaining 86% of variance and enabling efficient clustering. Both Elbow Method and Silhouette Scores were used to choose an appropriate number of clusters, balancing simplicity and interpretability, although they gave out a different recommended number of clusters, 4 and 2 respectively, both were plotted and it was then decided to carry on the notebook with four clusters Although two clusters produced stronger separation, four clusters offered richer behavioural insight while maintaining adequate cohesion. These profiles provide actionable insights for educators and wellbeing professionals.

The final four clusters revealed distinct behavioural segments:

| **Cluster**   | **High-Level Description**                                                                           |
| ------------- | ---------------------------------------------------------------------------------------------------- |
| **Cluster 0** | Balanced demographic mix, moderate usage, minimal academic interference                              |
| **Cluster 1** | Older/more advanced students, primarily male, low impact on academics                                |
| **Cluster 2** | Heavy social media users, predominantly female undergraduates, highest academic and wellbeing impact |
| **Cluster 3** | Mixed group with balanced platform use and moderate interference                                     |

### Limitations in the data

-   Self-reported metrics introduce subjectivity and potential bias.
-   Data taken from a single point in time, no time comparison available amongst individuals.
-   Uneven category sizes meant potential for misrepresentation and required use of non-parametric methods.

Future work could include:

-   Collecting behavioural data for time-series analysis.
-   Expanding demographics to improve fairness in comparisons.
-   Developing predictive models to estimate risk of academic impact or addiction.

### Overall summary

Through use of exploratory analysis, statistical methods, visual plots and machine-learning techniques, this project provides a detailed, evidence-based picture of student's social media behaviour. The findings suggest that heavy engagement on certain platforms may align with higher academic disruption and lower mental health scores, while other groups maintain balanced usage with minimal negative effects. These patterns demonstrate that the results of this project are just grouped behaviours and may not be a one size fits all for every individual within a certain group.

The interactive dashboard, supported by well thought out methodology and user friendly design design, transforms complex analysis into accessible insights, making this project a valuable tool for understanding digital behaviour in student populations. This analysis reinforces the importance of using evidence-based insights to inform student support strategies, and foster healthier relationships with social media.

### Use of AI in this project

-   Helping create hypotheses
-   Improving code efficiency, particularly in preprocessing and visualisation, or carrying out mapping of large amounts of data
-   Helping with statistical interpretation
-   Offering visualisation improvements to plots
-   Supporting cluster profiling and narrative clarity.
-   Helping debug and issue I had with including images in markdown

## Credits

-   Kaggle for the dataset
-   Code institute LMS for being a tool that I could refer back to
-   Code institute data analytics and readme templates
-   Youtube - Refresher on seaborn/matplotlib
-   OpenAI, ChatGPT and PerplexityAI
-   Header image - https://siddharthrajsekar.substack.com/p/swipe-scroll-repeat-how-instagram

## Acknowledgements

-   Code Institute facilitators and coaches - Emma Lamont, Spencer Barriball, Mark Briscoe, Marcel (123helpmestudy)
-   Fellow September 2025 for support along the way, technical and emotional
-   ChatGPT/PerplexityAI
