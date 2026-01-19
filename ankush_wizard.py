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
    "Relations & Functions": {
        "Easy": [
            {"q": "If $n(A) = 3$, how many reflexive relations can be defined on $A$?", "a": "64", "sol": "Formula: $2^{n^2 - n}$. For $n=3$, $2^{9-3} = 2^6 = 64$."},
            {"q": "Check if the relation $R = \{(1,2), (2,1)\}$ on set $\{1,2,3\}$ is transitive.", "a": "No", "sol": "For transitivity, if $(1,2) \in R$ and $(2,1) \in R$, then $(1,1)$ must be in $R$. Since $(1,1) \notin R$, it is not transitive."},
            {"q": "Define a void relation.", "a": "Empty set", "sol": "A relation $R$ on set $A$ is void if no element of $A$ is related to any element of $A$, i.e., $R = \emptyset$."},
            {"q": "Is the identity relation on a non-empty set symmetric?", "a": "Yes", "sol": "In an identity relation, $(a,a) \in R$ for all $a$. If $(a,b) \in R$, then $a=b$, so $(b,a)$ is also in $R$."},
            {"q": "What is the range of a constant function $f(x) = k$?", "a": "{k}", "sol": "A constant function maps every input to the same single output value $k$."}
        ],
        "Medium": [
            {"q": "Let $f: R \rightarrow R$ be defined by $f(x) = 3x$. Is $f$ onto?", "a": "Yes", "sol": "For any $y \in R$, let $3x = y \implies x = y/3$. Since $y/3$ is always a real number, every $y$ has a pre-image. Thus, it is onto."},
            {"q": "If $f(x) = x+7$ and $g(x) = x-7$, find $fog(x)$.", "a": "x", "sol": "$f(g(x)) = f(x-7) = (x-7) + 7 = x$."},
            {"q": "Find the number of binary operations on a set with 2 elements.", "a": "16", "sol": "Formula: $n^{n^2}$. For $n=2$, $2^{2^2} = 2^4 = 16$."},
            {"q": "Is $f(x) = |x|$ a one-one function from $R \rightarrow R$?", "a": "No", "sol": "$f(1) = 1$ and $f(-1) = 1$. Since different inputs give the same output, it is not one-one."},
            {"q": "Let $R$ be a relation in $N$ given by $R = \{(a,b) : a = b-2, b > 6\}$. Is $(2,4) \in R$?", "a": "No", "sol": "Although $2 = 4-2$, the condition $b > 6$ is not met since $b=4$."}
        ],
        "Hard": [
            {"q": "Let $L$ be the set of all lines in a plane and $R$ be the relation 'is perpendicular to'. Is $R$ transitive?", "a": "No", "sol": "If $L_1 \perp L_2$ and $L_2 \perp L_3$, then $L_1$ is parallel to $L_3$, not perpendicular. So it's not transitive."},
            {"q": "Show that the signum function $f: R \rightarrow R$ is neither one-one nor onto.", "a": "Not one-one", "sol": "$f(1)=1$ and $f(2)=1$, so not one-one. Range is $\{-1, 0, 1\}$, which is not equal to Codomain $R$, so not onto."},
            {"q": "Let $A = \{1,2,3\}$. Find the number of equivalence relations containing $(1,2)$ and $(2,1)$.", "a": "2", "sol": "Smallest is $\{(1,1),(2,2),(3,3),(1,2),(2,1)\}$. Largest is the universal relation $A \times A$."},
            {"q": "Check the injectivity of $f(n) = n^2$ where $f: N \rightarrow N$.", "a": "Injective", "sol": "Since $n_1, n_2$ are natural numbers, $n_1^2 = n_2^2$ always implies $n_1 = n_2$."},
            {"q": "If $R = \{(a,b) : a \le b^2\}$, is $R$ reflexive?", "a": "No", "sol": "For $a=1/2$, $(1/2)^2 = 1/4$. $1/2 \le 1/4$ is false. So $(1/2, 1/2) \notin R$."}
        ],
        "Expert": [
            {"q": "Let $A = R - \{3\}$ and $B = R - \{1\}$. $f: A \rightarrow B$ is $f(x) = (x-2)/(x-3)$. Is $f$ bijective?", "a": "Yes", "sol": "Check one-one: $f(x_1)=f(x_2)$ leads to $x_1=x_2$. Check onto: $y = (x-2)/(x-3) \implies x = (3y-2)/(y-1)$. Since $y \ne 1$, $x$ is always defined in $A$."},
            {"q": "Number of onto functions from $\{1,2,...,n\}$ to $\{a,b\}$ is?", "a": "2^n - 2", "sol": "Total functions are $2^n$. Two functions are not onto (where all map to $a$ or all map to $b$). Hence $2^n - 2$."},
            {"q": "Determine if $R = \{(x,y) : x-y \text{ is an integer}\}$ is an equivalence relation on $R$.", "a": "Yes", "sol": "Reflexive ($x-x=0$), Symmetric ($x-y \in Z \implies y-x \in Z$), and Transitive ($x-y+y-z = x-z \in Z$)."},
            {"q": "Find total number of equivalence relations on $\{1,2,3\}$.", "a": "5", "sol": "These correspond to Partitions of the set: {1,2,3}, {{1},{2,3}}, {{2},{1,3}}, {{3},{1,2}}, {{1},{2},{3}}."},
            {"q": "Let $f(x) = [x]$ be the greatest integer function. Is it onto $R \rightarrow R$?", "a": "No", "sol": "The range of $f$ is the set of integers $Z$. Since the codomain is $R$ and $Z \ne R$ (e.g., $0.5$ has no pre-image), it is not onto."}
        ]
    },
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
    "Integrals": {
        "Easy": [
            {"q": "Find $\int x^2 dx$.", "a": "x^3/3 + C", "sol": "Using $\int x^n dx = x^{n+1}/(n+1)$."},
            {"q": "Evaluate $\int \sec^2 x dx$.", "a": "tan x + C", "sol": "Standard derivative of $\tan x$ is $\sec^2 x$."},
            {"q": "Find $\int e^{2x} dx$.", "a": "(e^2x)/2 + C", "sol": "Using $\int e^{ax} dx = \frac{e^{ax}}{a} + C$."},
            {"q": "Evaluate $\int \frac{1}{x} dx$.", "a": "log|x| + C", "sol": "Standard integral form."},
            {"q": "Integrate $\int \sin(2x) dx$.", "a": "-cos(2x)/2 + C", "sol": "Integral of $\sin(ax)$ is $-\frac{\cos(ax)}{a}$."}
        ],
        "Medium": [
            {"q": "Evaluate $\int \tan x dx$.", "a": "log|sec x| + C", "sol": "Write as $\int \frac{\sin x}{\cos x} dx$ and use substitution $u = \cos x$."},
            {"q": r"Evaluate $\int \frac{dx}{x^2 - a^2}$.", "a": "1/2a log|(x-a)/(x+a)| + C", r"sol": r"Using partial fractions: $\displaystyle \frac{1}{x^2-a^2} = \frac{1}{2a} \left[ \frac{1}{x-a} - \frac{1}{x+a} \right]$. Integrating gives $\displaystyle \frac{1}{2a} \log \left| \frac{x-a}{x+a} \right| + C$."},
            {"q": "Find $\int x e^x dx$.", "a": "(x-1)e^x + C", "sol": "Use Integration by Parts (ILATE rule): $u=x, v=e^x$."},
            {"q": "Evaluate $\int_0^{\pi/2} \cos x dx$.", "a": "1", "sol": "$[\sin x]_0^{\pi/2} = \sin(\pi/2) - \sin(0) = 1 - 0 = 1$."},
            {"q": "Integrate $\int \frac{1}{\sqrt{1-x^2}} dx$.", "a": "sin^-1 x + C", "sol": "Standard inverse trig integral."}
        ],
        "Hard": [
            {"q": "Evaluate $\int \frac{2x}{(x^2+1)(x^2+3)} dx$.", "a": "log|(x^2+1)/(x^2+3)| + C", "sol": "Substitute $u = x^2 \implies du = 2x dx$. Then use partial fractions."},
            {"q": "Evaluate $\int e^x (\sin x + \cos x) dx$.", "a": "e^x sin x + C", "sol": "Use formula $\int e^x [f(x) + f'(x)] dx = e^x f(x) + C$."},
            {"q": "Find $\int \sqrt{a^2 - x^2} dx$.", "a": "x/2 sqrt(a^2-x^2) + a^2/2 sin^-1(x/a) + C", "sol": "Use trigonometric substitution $x = a \sin \theta$."},
            {"q": "Evaluate $\int_0^{\pi} \frac{x \sin x}{1 + \cos^2 x} dx$.", "a": "pi^2/4", "sol": "Use property $P_4$ ($\int f(a-x)$) to remove $x$, then substitute $u = \cos x$."},
            {"q": "Integrate $\int \frac{dx}{\sin(x-a)\sin(x-b)}$.", "a": "1/sin(a-b) log|sin(x-a)/sin(x-b)| + C", "sol": "Multiply and divide by $\sin(a-b)$, then write numerator as $\sin((x-b)-(x-a))$."}
        ],
        "Expert": [
            {"q": "Evaluate $\int \sqrt{\tan x} dx$.", "a": "Complex form", "sol": "Substitute $\tan x = t^2$, resulting in a rational function $\int \frac{2t^2}{t^4+1} dt$ which is solved by dividing by $t^2$."},
            {"q": "Evaluate $\int_0^1 \frac{\log(1+x)}{1+x^2} dx$.", "a": "pi/8 log 2", "sol": "Substitute $x = \tan \theta$, then use properties of definite integrals."},
            {"q": "Find the value of $\int_0^{\pi/2} \log(\sin x) dx$.", "a": "-pi/2 log 2", "sol": "Use property $\int f(a-x)$ and combine integrals to get $2I = \int \log(\sin 2x) - \log 2$."},
            {"q": "Evaluate $\int \frac{x^2+1}{x^4+1} dx$.", "a": "1/sqrt(2) tan^-1((x^2-1)/(x sqrt(2))) + C", "sol": "Divide numerator and denominator by $x^2$, then substitute $u = x - 1/x$."},
            {"q": "Find $\int \frac{dx}{(x+1)\sqrt{x^2-1}}$.", "a": "sqrt((x-1)/(x+1)) + C", "sol": "Substitute $x+1 = 1/t$."}
        ]
    },
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




