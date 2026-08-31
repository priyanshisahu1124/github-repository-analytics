import streamlit as st
import duckdb
import plotly.express as px


# Configure Streamlit page
st.set_page_config(
    page_title="GitHub Repository Analytics",
    page_icon="📊",
    layout="wide"
)


# Dashboard title
st.title("📊 GitHub Repository Analytics Dashboard")

st.write(
    "An interactive dashboard for analyzing GitHub repository data."
)


# Connect to DuckDB
connection = duckdb.connect(
    "data/github.duckdb",
    read_only=True
)


# -----------------------------------
# GET MAIN METRICS
# -----------------------------------

total_repositories = connection.execute("""
    SELECT COUNT(*)
    FROM repositories
""").fetchone()[0]


total_stars = connection.execute("""
    SELECT SUM(stars)
    FROM repositories
""").fetchone()[0]


total_forks = connection.execute("""
    SELECT SUM(forks)
    FROM repositories
""").fetchone()[0]


most_popular_language = connection.execute("""
    SELECT language
    FROM repositories
    GROUP BY language
    ORDER BY COUNT(*) DESC
    LIMIT 1
""").fetchone()[0]


# -----------------------------------
# DISPLAY METRICS
# -----------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Repositories",
    total_repositories
)

col2.metric(
    "Total Stars",
    f"{total_stars:,}"
)

col3.metric(
    "Total Forks",
    f"{total_forks:,}"
)

col4.metric(
    "Most Popular Language",
    most_popular_language
)


# -----------------------------------
# TOP 10 REPOSITORIES
# -----------------------------------

st.subheader("⭐ Top 10 Repositories by Stars")

top_repositories = connection.execute("""
    SELECT name, stars
    FROM repositories
    ORDER BY stars DESC
    LIMIT 10
""").df()


fig1 = px.bar(
    top_repositories,
    x="stars",
    y="name",
    orientation="h",
    title="Top Repositories by Stars"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)


# -----------------------------------
# LANGUAGE DISTRIBUTION
# -----------------------------------

st.subheader(
    "💻 Repository Count by Programming Language"
)

languages = connection.execute("""
    SELECT language,
           COUNT(*) AS total_repositories
    FROM repositories
    GROUP BY language
    ORDER BY total_repositories DESC
""").df()


fig2 = px.bar(
    languages,
    x="language",
    y="total_repositories",
    title="Repositories by Programming Language"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)


# -----------------------------------
# STARS VS FORKS
# -----------------------------------

st.subheader("⭐ Stars vs 🍴 Forks")

comparison = connection.execute("""
    SELECT name, stars, forks, language
    FROM repositories
""").df()


fig3 = px.scatter(
    comparison,
    x="stars",
    y="forks",
    hover_name="name",
    color="language",
    title="Stars vs Forks"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)


# -----------------------------------
# CREATION TREND
# -----------------------------------

st.subheader("📅 Repository Creation Trend")

creation_trend = connection.execute("""
    SELECT
        YEAR(created_at) AS year,
        COUNT(*) AS total_repositories
    FROM repositories
    GROUP BY year
    ORDER BY year
""").df()


fig4 = px.line(
    creation_trend,
    x="year",
    y="total_repositories",
    markers=True,
    title="Repository Creation Trend"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)


# Close database connection
connection.close()