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

---

-   Hypothesis 1: Average daily use of social media will have a negative impact on sleep per night.
    H₀ - Null hypothesis: There is no relationship between average daily social media use and sleep per night.
    H₁ - Alternative Hypothesis Higher average daily social media use has a negative impact on sleep per night.

_This will be tested statistically using spearman's rank but will also be visualised on a scatter plot to see whether there is a relationship between the two values_

**Result:** We can reject the null hypothesis that there is no relationship between daily social media usage and sleep time.
**The correlation score between the two values was -0.81** meaning that in most cases as one value increased the other decreased. An increase in screen time resulted in sleep deficit which could have a knock on effect to academic studies and mental health score, leading to strained relationships with friends, family members and peers.
**With a pval < 0.05 (3.13 × 10⁻¹⁶⁶)** that is below the threshold of 0.05 to reject the null hypothesis and state that the relationship between the two values has not occured by chance.

![Average use of social media versus sleep score](/images/h1_usage_v_sleep.png)

---
