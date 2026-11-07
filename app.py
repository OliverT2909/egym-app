import streamlit as st

st.set_page_config(page_title="EGYM Trainingsplan", layout="centered")

st.title("🏋️ EGYM Trainingsplan")
st.write("Einheit 1 – 6 Wochen (2x / Woche)")

# Deine 8 EGYM Übungen aus dem Plan
uebungen = [
    "1. EGYM Beinpresse",
    "2. EGYM Beinstrecker",
    "3. EGYM Schulterpresse",
    "4. EGYM Ruderzug",
    "5. EGYM Brustpresse",
    "6. EGYM Latzug",
    "7. EGYM Glutaeus",
    "8. EGYM Rotator"
]

# Darstellung aller Übungen auf einer Seite
for uebung in uebungen:
    st.subheader(uebung)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.checkbox("Satz 1", key=f"{uebung}_1")
    with col2:
        st.checkbox("Satz 2", key=f"{uebung}_2")
    with col3:
        st.checkbox("Satz 3", key=f"{uebung}_3")
    st.divider()
