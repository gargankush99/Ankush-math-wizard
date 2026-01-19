import streamlit as st
import random

# --- BRANDING & CONFIG ---
st.set_page_config(page_title="Ankush Mathematics Wizard", page_icon="🧙‍♂️", layout="centered")

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
data = {
    "Relations & Functions": {"Easy": [], "Medium": [], "Hard": [], "Expert": []},
    "Inverse Trig Functions": {"Easy": [], "Medium": [], "Hard": [], "Expert": []},
    "Matrices": {
        "Expert": [
            {"q": "If A is a square matrix such that $A^2 = A$, then find the value of $(I + A)^3 - 7A$.", "a": "I", "sol": "Expanding $(I+A)^3$: $I^3 + 3I^2A + 3IA^2 + A^3$. Since $A^2=A$, then $A^3 = A^2 \cdot A = A \cdot A = A$. The expression becomes $I + 3A + 3A + A - 7A = I + 7A - 7A = I$."},
            {"q": "If A = [[cosθ, sinθ], [-sinθ, cosθ]], then prove by induction $A^n$ is [[cos nθ, sin nθ], [-sin nθ, cos nθ]]. What is $A^2$?", "a": "[[cos 2theta, sin 2theta], [-sin 2theta, cos 2theta]]", "sol": "By Matrix Multiplication: $A^2 = [[cosθ, sinθ], [-sinθ, cosθ]] \times [[cosθ, sinθ], [-sinθ, cosθ]]$. Using trig identities $cos^2θ - sin^2θ = cos2θ$ and $2sinθcosθ = sin2θ$."},
            {"q": "Find the matrix X such that $X [[1, 2], [3, 4]] = [[-2, 1], [4, 7]]$.", "a": "[[-5.5, 1.5], [-2.5, 2.5]]", "sol": "Let $A = [[1, 2], [3, 4]]$. $X = B A^{-1}$. First find $|A| = 4-6 = -2$. $A^{-1} = -1/2 [[4, -2], [-3, 1]]$. Multiply $B$ by $A^{-1}$ to get X."},
            {"q": "If A and B are symmetric matrices of the same order, then show that $AB - BA$ is a skew-symmetric matrix.", "a": "skew-symmetric", "sol": "Let $C = AB - BA$. $C' = (AB - BA)' = (AB)' - (BA)' = B'A' - A'B'$. Since A, B are symmetric, $A'=A, B'=B$. So $C' = BA - AB = -(AB - BA) = -C$. Hence skew-symmetric."},
            {"q": "A trust fund has Rs 30,000 that must be invested in two different types of bonds. The first bond pays 5% interest per year, and the second bond pays 7%. Using matrix multiplication, determine how to divide Rs 30,000 among the two types of bonds if the trust fund must obtain an annual total interest of Rs 1800.", "a": "15000, 15000", "sol": "Let investment be $[x, 30000-x]$. Interest matrix is $[0.05, 0.07]^T$. $[x, 30000-x][0.05, 0.07]^T = [1800]$. $0.05x + 2100 - 0.07x = 1800 \implies -0.02x = -300 \implies x = 15000$."}
        ],
        "Easy": [], "Medium": [], "Hard": []
    },
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

# Corrected Logic Block
if generate:
    pool = data.get(chapter, {}).get(level, [])
    
    if len(pool) == 0:
        st.session_state.current_questions = [{"q": "Wizard is still writing these!", "a": "N/A", "sol": "Check back soon."}]
        st.warning("This specific level is currently empty.")
    elif len(pool) < 5:
        st.session_state.current_questions = pool
    else:
        st.session_state.current_questions = random.sample(pool, 5)
    
    st.session_state.submitted = False

# Display logic (This must be outside the 'if generate' block to stay visible)
if 'current_questions' in st.session_state:
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
            # Safe check if answer exists
            correct_ans = item.get('a', "N/A")
            if user_inputs[i].strip().lower() == correct_ans.lower():
                st.success(f"Q{i+1}: Correct!")
                score += 1
            else:
                st.error(f"Q{i+1}: Incorrect. Your answer: {user_inputs[i]}")
                with st.expander(f"View Step-by-Step Solution for Q{i+1}"):
                    st.latex(item.get('sol', "Solution not available yet."))
        
        st.subheader(f"Total Score: {score}/{len(st.session_state.current_questions)}")
        if score < 3:
            st.warning(f"Wizard's Advice: You need to strengthen your fundamentals in **{chapter}**.")
        else:
            st.balloons()
            st.success("Great job! You're mastering this topic.")

