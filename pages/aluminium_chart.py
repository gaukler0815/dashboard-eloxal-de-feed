import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def display_aluminium_chart():
    today = datetime.today()
    dates = [today - timedelta(days=30*i) for i in range(5, -1, -1)] + [today + timedelta(days=30*i) for i in range(1, 7)]
    ist = [85, 89, 92, 91, 95, 97]
    prognose = [98, 99, 102, 105, 108, 110]

    all_dates = dates[:6] + dates[6:]
    all_werte = ist + prognose

    df = pd.DataFrame({
        "Monat": [d.strftime("%b %Y") for d in all_dates],
        "Wert": all_werte,
        "Typ": ["IST"]*6 + ["Prognose"]*6
    })

    fig, ax = plt.subplots(figsize=(10, 4))
    for typ in df["Typ"].unique():
        subset = df[df["Typ"] == typ]
        ax.plot(subset["Monat"], subset["Wert"], marker="o", label=typ)

    ax.set_ylabel("Nachfrageindex")
    ax.set_title("Aluminiumnachfrage in Deutschland")
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)


import feedparser
import streamlit as st

# Diagramm bleibt erhalten ...

st.markdown("## Aktuelle Nachrichten zu Aluminium")

feeds = [
    "https://www.alcircle.com/rss",
    "https://www.nasdaq.com/feed/rssoutbound?category=Aluminum"
]

for feed_url in feeds:
    try:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:3]:
            st.markdown(f"""
<div style="border:1px solid #ccc; border-radius:10px; padding:10px; margin-bottom:10px; background-color:#f9f9f9;">
    <a href="{entry.link}" target="_blank" style="text-decoration:none;">
        <strong>{entry.title}</strong>
    </a><br>
    <span style="font-size: 12px;">{entry.published if 'published' in entry else ''}</span><br>
    <p style="margin-top:5px;">{entry.summary[:200]}...</p>
</div>
""", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Fehler beim Laden des Feeds: {feed_url}")
