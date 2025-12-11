# Social media addiction

![social media header](images/readme_header.jpg)

Project bookmarks:

-   [README](/README.md)
-   [Project board](https://github.com/users/StavSteven/projects/10)
-   [Raw data](/data/raw_data/student_social_media_addiction.csv) | [Clean data](/data/cleaned_data/student_social_media_addiction_cleaned.csv)
-   [ETL Jupyter Notebook](/jupyter_notebooks/1_data_cleaning_student_social_media_addiction.ipynb)
-   [Visualisation & Statistical analysis Notebook](/jupyter_notebooks/2_visualisations_student_social_media_addiction.ipynb)
-   [Machine Learning Notebook](/jupyter_notebooks/3_machine_learning.ipynb)
-   [Power BI dashboard](/dashboard/social_media_addiction_dashboard.pbix)
-   [Conclusion and discussion]()

## Contents

1. [Project Overview](#project-overview)
2. [Dataset Content](#dataset-content)
3. [Business Requirements](#business-requirements)
4. [Hypothesis Testing and Validation](#hypothesis-testing-and-validation)
5. [Rationale to map business requirements](#rationale-to-map-business-requirements)
6. [Analysis Techniques Used](#analysis-techniques-used)
7. [Development Roadmap](#development-roadmap)
8. [Libraries & External Software Used](#libraries--external-software-used)
9. [Conclusion and discussion](#conclusion-and-discussion)
10. [Limitations](#limitations)
11. [Credits](#credits)
12. [Acknowledgements](#acknowledgements)

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

## Hypothesis and how to validate?

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
