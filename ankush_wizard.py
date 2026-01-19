import streamlit as st
import random

# --- BRANDING & CONFIG ---
st.set_page_config(page_title="Ankush Mathematics Wizard", page_icon="🧙‍♂️", layout="centered")

# Custom CSS to make it look like a "Wizard" brand
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { background-color: #4B0082; color: white; border-radius: 10px; width: 100%; }
    .stTitle { color: #4B0082; text-align: center; font-family: 'Garamond', serif; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧙‍♂️ Ankush Mathematics Wizard")
st.subheader("Grade 12 CBSE Board Practice Portal (2026 Pattern)")

# --- QUESTION DATABASE ---
# You can expand this list with 100s of questions
# Updated data dictionary with all Grade 12 CBSE Chapters
data = {
    "Relations & Functions": {"Easy": [], "Medium": [], "Hard": [], "Expert": []},
    "Inverse Trig Functions": {"Easy": [], "Medium": [], "Hard": [], "Expert": []},
    "Matrices": {"Easy": [], "Medium": [], "Hard": [], "Expert": []},
    "Determinants": {"Easy": [], "Medium": [], "Hard": [], "Expert": []},
    "Continuity & Differentiability": {"Easy": [], "Medium": [], "Hard": [], "Expert": []},
    "Applications of Derivatives": {"Easy": [], "Medium": [], "Hard": [], "Expert": []},
    "Integrals": {"Easy": [], "Medium": [], "Hard": [], "Expert": []},
    "Applications of Integrals": {"Easy": [], "Medium": [], "Hard": [], "Expert": []},
    "Differential Equations": {"Easy": [], "Medium": [], "Hard": [], "Expert": []},
    "Vector Algebra": {"Easy": [], "Medium": [], "Hard": [], "Expert": []},
    "Three Dimensional Geometry": {"Easy": [], "Medium": [], "Hard": [], "Expert": []},
    "Linear Programming": {"Easy": [], "Medium": [], "Hard": [], "Expert": []},
    "Probability": {"Easy": [], "Medium": [], "Hard": [], "Expert": []}
}
# --- APP LOGIC ---
with st.sidebar:
    st.header("Wizard's Controls")
    chapter = st.selectbox("Select Chapter", list(data.keys()))
    level = st.selectbox("Difficulty Level", ["Easy", "Medium", "Hard", "Expert"])
    generate = st.button("✨ Generate 5 New Questions")

if generate or 'current_questions' in st.session_state:
if generate:
    # This whole block is now indented 4 spaces
    pool = data.get(chapter, {}).get(level, [])
    
    if len(pool) == 0:
        # This line is indented 8 spaces (4 for the first IF, 4 for the second)
        st.session_state.current_questions = [{"q": "Wizard is still writing these!", "a": "N/A", "sol": "Check back soon."}]
        st.warning("This specific level is currently empty.")
    elif len(pool) < 5:
        st.session_state.current_questions = pool
    else:
        st.session_state.current_questions = random.sample(pool, 5)
    
    st.session_state.submitted = False

    st.info(f"Practicing: **{chapter}** | Level: **{level}**")
    
    user_inputs = []
    for i, item in enumerate(st.session_state.current_questions):
        st.write(f"**Q{i+1}:** {item['q']}")
        user_inputs.append(st.text_input(f"Your Answer for Q{i+1}", key=f"q{i}"))

    if st.button("Submit to the Wizard"):
        st.session_state.submitted = True
        
    if st.session_state.get('submitted'):
        score = 0
        st.write("---")
        for i, item in enumerate(st.session_state.current_questions):
            if user_inputs[i].strip().lower() == item['a'].lower():
                st.success(f"Q{i+1}: Correct!")
                score += 1
            else:
                st.error(f"Q{i+1}: Incorrect. Your answer: {user_inputs[i]}")
                with st.expander(f"View Step-by-Step Solution for Q{i+1}"):
                    st.latex(item['sol'])
        
        st.subheader(f"Total Score: {score}/5")
        if score < 3:
            st.warning(f"Wizard's Advice: You need to strengthen your fundamentals in **{chapter}**. Focus on NCERT Exemplar problems.")
        else:
            st.balloons()

            st.success("Great job! You're mastering this topic.")



