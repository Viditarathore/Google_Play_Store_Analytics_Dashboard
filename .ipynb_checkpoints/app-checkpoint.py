import streamlit as st
    
# List of HTML files containing the plots
html_files = ["top_10_categories.html","category_pie_Graph2.html","type_Graph3.html","Rating_Graph4.html","Sentiment_Distribution.html","Install_graph6.html","Updates_over_the_year_graph07.html","Revenue_by_category graph6.html","Genres_Graph9.html","updates_vs_rating_graph.html","PaidFree_rating_graph11.html"]  
# Replace with your file paths

# Streamlit App
st.title("Google Play Store Review Analytics")
st.header("Plots Visualization")

# Loop through the HTML files and display each
for i, html_file in enumerate(html_files):
    st.subheader(f"Plot {i + 1}")
    with open(html_file, "r", encoding="utf-8") as file:
        html_content = file.read()
        st.components.v1.html(html_content, height=400)  # Adjust height as needed
