# dsa210_project

## Personal Data Analysis of Pinterest Usage Based on Time and Reflection of Interests

## Project Description
This project explores my Pinterest usage data to uncover patterns in pinning behavior, the most active times of day and the types of boards I interact with the most based on different times and changes in personal interests. I used techniques like exploratory data analysis(EDA) and visualization to identify how my engagement evolves over time and across different categories.

This analysis will provide insights into:
- Trends in my Pinterest pinning behaviour.
- The most active hours during the day that I spend time on the app and how it changes over different years.
- Connections between pinning habits for certain boards and how my intearction with them has evolved thoroughout different years and months.

## Motivation
The reason I chose this project is, to better understand how my offline interests and seasonal habits reflect on my online behavior in the Pinterest app and to gain insight on how relative times in a year can affect my usage frequency of the app. The app offers me inspiration and ideas on certain categories especially in the context of artistic products. Therefore analyzing my Pinterest data offers a unique opportunity to gain self-insights and apply data science techniques to my personal data, and interpret the connections with my real-world life.

## Tools 
- Python  
- Pandas  
- Matplotlib  
- Seaborn  
- Jupyter Notebook  

## Data Source
The data was exported from my Pinterest account using their official data export tool in the HTML format, the relevant parts were scraped and saved as a csv file. The dataset includes information about:
- User profile information and user statistics
- Inferences made based on user activity
- Saved pins with timestamps.
- Boards and their associated pins.
  
The raw data will not be shared publicly, but the analysis scripts will be available.

## Data Processing
The raw Pinterest data required some cleaning and restructuring to be useful for analysis. Key steps in data processing included:

Removing Unnecessary or Invalid Entries:
Entries with incomplete, irrelevant, or corrupted data were filtered out. 

Converting Timestamp Fields to Proper Datetime Formats:
The "Created at" column was converted from string format to a proper datetime object to enable time-based analysis. Errors in this column (e.g., improperly formatted dates) were handled by coercing invalid entries to NaT and removing them from the dataset.

Aggregating Data Based on Attributes:
The data was grouped and summarized based on attributes such as "Board Name" and "Year-Month." This allowed for efficient calculation of metrics such as the number of pins created per board, per month, or per year.

Extracting Relevant Time Components:
For better analysis, components like the hour of the day and year-month were extracted from the datetime field to study trends in activity over time.

## Data Visualizations
To uncover patterns in Pinterest usage, several visualizations were created using Python libraries like Matplotlib and Seaborn. These include:

**Monthly Pinning Activity:**

A bar chart was generated to compare the number of pins created each month. This chart was used to test the hypothesis that pinning behavior correlates with seasonal trends, such as increased activity during summer and less activity during busier school months.

**Active Times of Day:**

A line graph plotted the frequency of pins created at each hour of the day. This helped identify my most active hours and provided insights into when I am most likely to use Pinterest.

**Board Interactions:**

A bar chart was created to display the number of pins associated with each board. This visualization highlights the boards I interacted with most frequently and provided insights into my top areas of interest.

**Heatmap Analysis:**

A heatmap was used to visualize my pinning activity across different boards and time periods (months and years). This detailed visualization highlighted long-term trends in how I engaged with specific boards over time.

## Data Analysis

**Active Times**

To analyze my activity by hour, I first extracted the hour from the timestamps in the Created at column of the Pinterest pin data. I grouped the data by hour and counted the number of pins for each hour of the day. The resulting data was visualized using a line plot, which clearly displayed the distribution of pinning activity throughout a typical day.

**Pinning Behavior Across Months**

To examine how my activity changed across months and years, I extracted the year and month from the pin timestamps and grouped the data accordingly. I conducted a goodness-of-fit test to compare my monthly activity to a uniform distribution, allowing me to assess whether certain months had significantly different pinning activity levels. This analysis was visualized with a bar plot to show the frequency of pinning activity over time.

**Board Interactions**

I analyzed my pinning activity for each board by cleaning and filtering the board name data to exclude invalid entries. After grouping the data by board names, I counted the total number of pins per board. I merged this data with board creation dates from the boards dataset for additional context. Finally, I visualized the results using a horizontal bar plot, displaying the pin counts for each board. 

**Heatmap Analysis**

To investigate my interactions with boards over time, I grouped the data by board name and month-year periods. I counted the number of pins for each board during each period and created a pivot table for visualization. This data was then plotted as a heatmap, with custom color mapping to highlight variations in pinning activity across boards and months.

## Findings
**Active Pinning Times**

From the analysis of hourly pinning activity, I observed that my most active hours were surprisingly in the morning, particularly at 9 AM and 10 AM. Additionally, I showed consistent activity during the late afternoon and early evening, between 4 PM and 7 PM. However, my activity significantly declined around noon, specifically between 12 PM and 2 PM. These patterns may reflect my daily routine and the times when I had the time or need to engage with Pinterest.

**Most Active Boards**

My Pinterest usage primarily revolved around artistic inspiration, as demonstrated by the popularity of boards related to creativity and artistic products. Two standout boards were the "Creation Inspo" board, focused on pottery and DIY projects, and the "Drawing" board. These boards consistently received a high number of pins, indicating their importance in supporting my hobbies.

**Heatmap Insights**

The heatmap analysis revealed clear patterns in how I interacted with specific boards across months and years. For instance, I used the "Drawing" board most actively between June and August 2017, suggesting a period of heightened interest or focus on sketching and illustration. Similarly, the "Creation Inspo" board, associated with pottery projects, showed a peak in activity between August and October 2024. These trends highlight how my creative interests shifted over time, with certain boards becoming more popular during specific periods.

**Pinning Behavior by Month**

My activity also showed clear trends when analyzed on a monthly basis. I was most active during the months of September to December in 2023 and 2024, a period that likely coincided with my personal hobbies or specific projects. Additionally, I showed notable activity during January and March in 2020 and 2021. These patterns do not align with my hypothesis of "using Pinterest more in relatively free months which I did not have a very busy schedule such as classes in school, and using the app more in relatively free months such as summer as I had more time to pursue my hobbies and make artistic creations", however from the data anaylsis it can be derived that I was most active during the time I had more classes. I analyzed the years 2020-2021 also as I was still in high school during those years to see if the hypothesis held with my high school class schedule, however data showed that I was again the most active in school months especially during exam season.

## Limitations
Data Sourced Limitations:
Some timestamps in the data were missing or incomplete, which required cleaning and imputation.
Certain board names were inconsistent or had irrelevant data attached, which was filtered out.

Personal Limitations
The dataset only represents my activity on Pinterest and does not account for external factors that may influence my behavior on the platform.

## Future Work
In the future, I could do:

Include more detailed analysis of user interactions like comments, followed boards of other users and repins.
Integrate data from other platforms to compare cross-platform usage patterns.
Extend the analysis to include time-of-day behavior for each board to see if specific boards are more active at certain times.



