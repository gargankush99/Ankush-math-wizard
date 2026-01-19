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
data = {
    "Relations & Functions": {
        "Hard": [
            {"q": "Let $A = \{1, 2, 3\}$. Find the number of equivalence relations containing $(1, 2)$.", "a": "2", "sol": "The smallest equivalence relation is $R_1 = \{(1,1), (2,2), (3,3), (1,2), (2,1)\}$. To keep it equivalence, we can add $(2,3), (3,2), (1,3), (3,1)$. This gives $R_2$ (the universal relation). Total = 2."},
            {"q": "Check if $f: R \\rightarrow R$ defined by $f(x) = x^3$ is a bijection.", "a": "Yes", "sol": "1. **One-to-one:** $x_1^3 = x_2^3 \\implies x_1 = x_2$. 2. **Onto:** For every $y \in R$, there exists $x = \sqrt[3]{y} \in R$. Thus, it is a bijection."}
        ],
        "Easy": [
            {"q": "If $n(A) = 3$, find the number of reflexive relations on A.", "a": "64", "sol": "Formula: $2^{n^2 - n}$. Here $2^{9-3} = 2^6 = 64$."}
        ]
    },
    "Calculus": {
        "Expert": [
            {"q": "Evaluate $\int_{0}^{\pi/2} \\frac{\sqrt{\sin x}}{\sqrt{\sin x} + \sqrt{\cos x}} dx$.", "a": "pi/4", "sol": "Using property $\int_{0}^{a} f(x)dx = \int_{0}^{a} f(a-x)dx$, the integral $I$ becomes $\int \frac{\sqrt{\cos x}}{\sqrt{\cos x} + \sqrt{\sin x}}$. Adding both: $2I = \int_{0}^{\pi/2} 1 dx = [x]_{0}^{\pi/2} = \pi/2$. So $I = \pi/4$."}
        ]
    }
}

# --- APP LOGIC ---
with st.sidebar:
    st.header("Wizard's Controls")
    chapter = st.selectbox("Select Chapter", list(data.keys()))
    level = st.selectbox("Difficulty Level", ["Easy", "Medium", "Hard", "Expert"])
    generate = st.button("✨ Generate 5 New Questions")

if generate or 'current_questions' in st.session_state:
    if generate:
        # Pick random questions from the selected pool
        pool = data.get(chapter, {}).get(level, [{"q": "Coming soon...", "a": "N/A", "sol": "Work in progress."}])
        st.session_state.current_questions = random.sample(pool * 5, 5) # Multiplying to ensure 5 exist for demo
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