import streamlit as st

# List of HTML files and their descriptions
plots = [
    {"file": "top_10_categories.html","title":"Top Categories with the Highest Number of Apps  ","description":"The distribution of top categories on the Play Store reveals that Tools, Entertainment, and Productivity apps dominate in terms of popularity and prevalence. Tools consistently occupy the largest share, reflecting the high demand for utility apps that enhance functionality and user convenience. Entertainment apps, including streaming platforms and gaming, follow closely, highlighting the growing focus on leisure and recreation. Productivity apps rank third, emphasizing their importance in improving efficiency for personal and professional tasks. Together, these categories capture a significant portion of the Play Store's landscape, indicating user preferences for both utility and leisure."},
    {"file": "category_pie_Graph2.html","title":"Categories Represent  through pie chart","description":"The pie chart illustrates the percentage distribution of the top categories on the Play Store. Tools apps lead, followed by Entertainment and Productivity apps. This visualization highlights the dominance of utility and leisure apps, with productivity-focused apps representing a smaller but significant portion of the Play Store's offerings."},
    {"file": "type_Graph3.html","title":"Type Distribution","description":"Most apps on the App Store are free, a strategy designed to attract a large user base initially. The idea is to provide free access to attract users, and then monetize through in-app advertisements, offering additional revenue streams as the user engagement grows."},
    {"file": "Rating_Graph4.html","title":"Rating Distribution","description":"Ratings on the App Store are skewed towards higher values, indicating that most apps receive favorable reviews from users. This suggests that users generally have positive experiences with the apps they use, contributing to a higher overall rating distribution."},
    {"file": "Sentiment_Distribution.html","title":"Sentiment Distribution","description":"Sentiment analysis of reviews shows a mix of positive and negative feedback, with a slight overall positive sentiment. While users express some dissatisfaction, the majority of reviews are favorable, indicating a generally positive perception of the apps"},
    {"file": "Install_graph6.html","title":"Highly Installed Categories","description":"The category most installed by users is typically Games, reflecting their high demand for entertainment and leisure activities. This trend highlights the popularity of mobile gaming, which often leads to a large number of installs compared to other categories."},
    {"file": "Updates_over_the_year_graph07.html","title":"Updates over the Years","description":"As the years pass, the frequency of updates for apps increases simultaneously. This trend reflects the growing emphasis on improving app functionality, fixing bugs, adding new features, and adapting to changing user needs and platform requirements."},
    {"file": "Revenue_by_category graph6.html","title":"Revenue By Category","description":"Categories like Business and Productivity lead in revenue generation, highlighting their strong monetization potential. These apps often rely on subscription models, in-app purchases, or premium features, making them highly lucrative compared to other categories."},
    {"file": "Genres_Graph9.html","title":"Top Genres","description":"Genres like Action, Casual, Tools, Education, and Entertainment are the most common, reflecting users' preferences for engaging and easy-to-play games and apps. These genres cater to a wide range of interests, offering both interactive experiences and practical functionalities."},
    {"file": "updates_vs_rating_graph.html","title":"Updates Vs Rating","description":"The scatter plot shows a weak correlation between the last update and rating, suggesting that more frequent updates do not always lead to higher ratings. This implies that factors other than updates, such as app quality or user experience, play a more significant role in determining user ratings."},
    {"file": "PaidFree_rating_graph11.html","title":"Type Vs Rating","description":"Paid apps tend to have higher ratings compared to free apps, suggesting that users expect higher quality and better functionality from apps they pay for. This indicates that users are more discerning when it comes to apps with a monetary cost, valuing their investment with a higher standard of performance and features. "},
]

# Streamlit App
st.title("Google Play Store Review Analytics")
st.header("Plots Visualization")

# Loop through the plots and display each with its description
for i, plot in enumerate(plots):
    st.subheader(f"Plot {i + 1} : "+ plot['title'])
    
    st.write(plot["description"])  # Add the description
    with open(plot["file"], "r", encoding="utf-8") as file:
        html_content = file.read()
        st.components.v1.html(html_content, height=400)  # Adjust height as needed
        