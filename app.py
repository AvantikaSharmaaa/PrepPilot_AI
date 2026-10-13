import random
import streamlit as st

st.set_page_config(
    page_title="PrepPilot AI | Interview Preparation",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------- Question bank --------------------
QUESTION_BANK = {
    "HR": [
        {
            "question": "Tell me about yourself.",
            "answer": "Give a 60–90 second summary: education, relevant skills, one or two projects, strengths, and the role you want. Keep it specific to the job.",
            "keywords": ["education", "skills", "project", "strength", "role"],
            "difficulty": "Easy",
        },
        {
            "question": "Why should we hire you?",
            "answer": "Connect your skills to the role. Mention that you learn quickly, can explain your projects clearly, work well with others, and are ready to contribute while continuing to learn.",
            "keywords": ["skills", "learn", "contribute", "team", "project"],
            "difficulty": "Easy",
        },
        {
            "question": "What is one strength and one area you are improving?",
            "answer": "Choose a real strength with an example. For the improvement area, explain the steps you are taking to improve rather than giving a fake weakness.",
            "keywords": ["strength", "example", "improve", "practice", "feedback"],
            "difficulty": "Easy",
        },
        {
            "question": "Describe a challenge you faced in a project.",
            "answer": "Use STAR: Situation, Task, Action, Result. Explain the issue, your responsibility, the steps you personally took, and what you learned.",
            "keywords": ["situation", "task", "action", "result", "learned"],
            "difficulty": "Medium",
        },
        {
            "question": "Where do you see yourself in three years?",
            "answer": "Explain that you want to strengthen your technical skills, take responsibility for meaningful work, and become a reliable contributor to the team.",
            "keywords": ["skills", "responsibility", "team", "learn", "contribute"],
            "difficulty": "Easy",
        },
    ],
    "Python": [
        {
            "question": "What is Python?",
            "answer": "Python is a high-level, general-purpose programming language known for readable syntax. It is used in automation, web development, data analysis, and AI/ML.",
            "keywords": ["high-level", "programming", "syntax", "automation", "data"],
            "difficulty": "Easy",
        },
        {
            "question": "What is the difference between a list and a tuple?",
            "answer": "A list is mutable, so its elements can be changed. A tuple is immutable, so its elements cannot be reassigned after creation. Lists use [] and tuples commonly use ().",
            "keywords": ["mutable", "immutable", "list", "tuple"],
            "difficulty": "Easy",
        },
        {
            "question": "What is a dictionary in Python?",
            "answer": "A dictionary stores key-value pairs. Keys must be hashable and unique. Example: student = {'name': 'Asha', 'marks': 90}.",
            "keywords": ["key", "value", "pairs", "unique"],
            "difficulty": "Easy",
        },
        {
            "question": "What is the difference between == and is?",
            "answer": "== checks whether values are equal. 'is' checks whether two references point to the same object.",
            "keywords": ["value", "identity", "object", "equal"],
            "difficulty": "Medium",
        },
        {
            "question": "What is exception handling?",
            "answer": "Exception handling lets a program respond to runtime errors using try and except. A finally block can run cleanup code whether an error occurred or not.",
            "keywords": ["try", "except", "error", "finally"],
            "difficulty": "Medium",
        },
        {
            "question": "What is a list comprehension?",
            "answer": "A concise way to build a list from an iterable. Example: squares = [n * n for n in range(5)].",
            "keywords": ["list", "iterable", "expression", "range"],
            "difficulty": "Medium",
        },
    ],
    "AI/ML": [
        {
            "question": "What is the difference between AI, ML, and deep learning?",
            "answer": "AI is the broad field of systems performing intelligent tasks. ML is a subset of AI that learns patterns from data. Deep learning is a subset of ML using multi-layer neural networks.",
            "keywords": ["artificial intelligence", "machine learning", "subset", "neural networks", "data"],
            "difficulty": "Easy",
        },
        {
            "question": "What is supervised learning?",
            "answer": "Supervised learning trains a model on labelled examples, where input data is paired with the expected output. Classification and regression are common tasks.",
            "keywords": ["labelled", "input", "output", "classification", "regression"],
            "difficulty": "Easy",
        },
        {
            "question": "What is overfitting?",
            "answer": "Overfitting happens when a model learns training data too closely, including noise, and performs poorly on unseen data. It can be reduced with validation, regularization, simpler models, or more data.",
            "keywords": ["training", "unseen", "validation", "regularization", "generalize"],
            "difficulty": "Medium",
        },
        {
            "question": "What is the difference between classification and regression?",
            "answer": "Classification predicts a category, such as spam or not spam. Regression predicts a numeric value, such as a house price.",
            "keywords": ["category", "class", "numeric", "value", "predict"],
            "difficulty": "Easy",
        },
        {
            "question": "Why do we split data into training and test sets?",
            "answer": "The training set is used to fit the model. The test set estimates performance on data the model has not seen, helping assess generalization.",
            "keywords": ["training", "test", "unseen", "performance", "generalization"],
            "difficulty": "Medium",
        },
    ],
    "SQL": [
        {
            "question": "What is SQL?",
            "answer": "SQL stands for Structured Query Language. It is used to create, read, update, and delete data in relational database systems.",
            "keywords": ["structured query language", "database", "relational", "data"],
            "difficulty": "Easy",
        },
        {
            "question": "What is the difference between WHERE and HAVING?",
            "answer": "WHERE filters rows before grouping. HAVING filters groups after GROUP BY, often using aggregate functions.",
            "keywords": ["rows", "groups", "group by", "aggregate"],
            "difficulty": "Medium",
        },
        {
            "question": "What is a primary key?",
            "answer": "A primary key uniquely identifies each row in a table. It must be unique and cannot contain NULL values.",
            "keywords": ["unique", "row", "null", "identify"],
            "difficulty": "Easy",
        },
        {
            "question": "What is a JOIN?",
            "answer": "A JOIN combines rows from two or more tables using a related column or join condition. Common types include INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN.",
            "keywords": ["tables", "related", "inner", "left", "condition"],
            "difficulty": "Medium",
        },
    ],
    "Software Development": [
        {
            "question": "What is object-oriented programming?",
            "answer": "OOP organizes code around objects that combine data and behavior. Its common principles are encapsulation, abstraction, inheritance, and polymorphism.",
            "keywords": ["objects", "encapsulation", "abstraction", "inheritance", "polymorphism"],
            "difficulty": "Easy",
        },
        {
            "question": "What is Git used for?",
            "answer": "Git is a version-control system that tracks changes, supports branches, and helps developers collaborate and restore earlier versions of a project.",
            "keywords": ["version control", "changes", "branches", "collaborate"],
            "difficulty": "Easy",
        },
        {
            "question": "What is an API?",
            "answer": "An API defines how software components communicate. A web API often allows a client to request or update data on a server using HTTP methods.",
            "keywords": ["communication", "client", "server", "request", "HTTP"],
            "difficulty": "Easy",
        },
        {
            "question": "What is the purpose of testing software?",
            "answer": "Testing checks whether software behaves as expected, helps find defects, and reduces the risk of regressions when code changes.",
            "keywords": ["expected", "defects", "quality", "regression"],
            "difficulty": "Easy",
        },
    ],
}

CODING_QUESTIONS = [
    {
        "title": "Reverse a string",
        "prompt": "Write a function that returns a string in reverse order.",
        "solution": 'def reverse_string(text):\n    return text[::-1]\n\nprint(reverse_string("python"))  # nohtyp',
        "hint": "Python slicing can use a step of -1.",
    },
    {
        "title": "Check for a palindrome",
        "prompt": "Return True when a word reads the same forward and backward. Ignore letter case.",
        "solution": 'def is_palindrome(text):\n    cleaned = text.lower().replace(" ", "")\n    return cleaned == cleaned[::-1]\n\nprint(is_palindrome("Level"))  # True',
        "hint": "Normalize the text, then compare it with its reverse.",
    },
    {
        "title": "Find the largest number",
        "prompt": "Write a function that returns the largest value in a list.",
        "solution": 'def largest_number(numbers):\n    if not numbers:\n        raise ValueError("List cannot be empty")\n    return max(numbers)\n\nprint(largest_number([4, 9, 2, 7]))  # 9',
        "hint": "Consider the built-in max() function and the empty-list case.",
    },
    {
        "title": "Count vowels",
        "prompt": "Count the vowels a, e, i, o, u in a string.",
        "solution": 'def count_vowels(text):\n    return sum(1 for char in text.lower() if char in "aeiou")\n\nprint(count_vowels("Interview"))  # 4',
        "hint": "Loop through each character and check membership in a string of vowels.",
    },
    {
        "title": "Remove duplicates",
        "prompt": "Return a list with duplicates removed while preserving the original order.",
        "solution": 'def remove_duplicates(items):\n    result = []\n    for item in items:\n        if item not in result:\n            result.append(item)\n    return result\n\nprint(remove_duplicates([1, 2, 1, 3, 2]))  # [1, 2, 3]',
        "hint": "Build a new list and append an item only when it has not appeared yet.",
    },
]

def score_answer(user_answer, question):
    """A transparent practice score based on answer length and keyword coverage, not an AI judgment."""
    answer = user_answer.strip().lower()
    if not answer:
        return 0, []
    matched = [word for word in question["keywords"] if word.lower() in answer]
    keyword_score = round((len(matched) / max(len(question["keywords"]), 1)) * 70)
    length_score = 30 if len(answer.split()) >= 25 else 20 if len(answer.split()) >= 12 else 10
    return min(100, keyword_score + length_score), matched

# -------------------- UI styling --------------------
st.markdown("""
<style>
.stApp { background: #0b1020; color: #edf2ff; }
[data-testid="stSidebar"] { background: #11182b; }
.block-container { padding-top: 2rem; max-width: 1250px; }
.hero {
  padding: 28px; border-radius: 22px;
  background: linear-gradient(120deg, #18284b 0%, #24204c 55%, #173a4b 100%);
  border: 1px solid rgba(255,255,255,.12); margin-bottom: 22px;
}
.hero h1 { font-size: 2.35rem; margin: 0 0 8px 0; color: #ffffff; }
.hero p { color: #cbd5f5; margin-bottom: 0; }
.small-muted { color: #aab6d4; font-size: .92rem; }
div[data-testid="stMetric"] {
  background: #141d33; padding: 16px; border-radius: 15px;
  border: 1px solid rgba(255,255,255,.08);
}
div.stButton > button {
  border-radius: 10px; border: 1px solid #5566aa; font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

if "attempted" not in st.session_state:
    st.session_state.attempted = []
if "mock_index" not in st.session_state:
    st.session_state.mock_index = 0
if "mock_category" not in st.session_state:
    st.session_state.mock_category = "Python"
if "mock_order" not in st.session_state:
    st.session_state.mock_order = []

st.sidebar.markdown("## 🎯 PrepPilot AI")
st.sidebar.caption("Your interview practice workspace")
page = st.sidebar.radio(
    "Navigate",
    ["Dashboard", "Question Practice", "Mock Interview", "Coding Round", "Resume & Projects", "About"],
)
st.sidebar.divider()
st.sidebar.markdown("**Suggested routine**")
st.sidebar.write("• 10 technical questions")
st.sidebar.write("• 2 coding problems")
st.sidebar.write("• 1 project explanation")
st.sidebar.write("• 10 minutes of HR practice")

attempt_count = len(st.session_state.attempted)
avg_score = round(sum(item["score"] for item in st.session_state.attempted) / attempt_count) if attempt_count else 0

if page == "Dashboard":
    st.markdown("""
    <div class="hero">
      <h1>Prepare smarter. Interview confidently. ✨</h1>
      <p>Practice technical concepts, HR questions, coding challenges, and project explanations in one place.</p>
    </div>
    """, unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("Answers practiced", attempt_count)
    c2.metric("Average practice score", f"{avg_score}%")
    c3.metric("Question categories", len(QUESTION_BANK))
    st.subheader("Your practice areas")
    cols = st.columns(3)
    cards = [
        ("🧠", "Technical Questions", "Python, AI/ML, SQL and software fundamentals."),
        ("🎙️", "Mock Interview", "Answer one question at a time and review your response."),
        ("💻", "Coding Round", "Practice beginner-friendly coding questions with hints."),
    ]
    for col, card in zip(cols, cards):
        with col:
            st.markdown(f"### {card[0]} {card[1]}")
            st.write(card[2])
    st.info("Start with Question Practice, then use Mock Interview to rehearse answers without looking at the sample response.")
    st.subheader("Placement preparation checklist")
    for task in [
        "Prepare a 60–90 second self-introduction",
        "Revise Python fundamentals and OOP",
        "Explain one project from problem to result",
        "Practice SQL queries and basic coding",
        "Prepare examples of teamwork and problem-solving",
    ]:
        st.checkbox(task, key="check_" + task)

elif page == "Question Practice":
    st.markdown("## 📚 Question Practice")
    st.write("Choose a topic, write your answer, then reveal the sample answer and receive a transparent practice score.")
    category = st.selectbox("Choose a category", list(QUESTION_BANK.keys()))
    questions = QUESTION_BANK[category]
    question_labels = [f"{i+1}. {q['question']}" for i, q in enumerate(questions)]
    selected_label = st.selectbox("Select a question", question_labels)
    q_index = question_labels.index(selected_label)
    q = questions[q_index]
    st.markdown(f"### {q['question']}")
    st.caption(f"Difficulty: {q['difficulty']}")
    answer_key = f"answer_{category}_{q_index}"
    user_answer = st.text_area("Your answer", key=answer_key, height=180, placeholder="Write your answer here...")
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Evaluate my practice answer", type="primary"):
            score, matched = score_answer(user_answer, q)
            st.session_state.attempted.append({
                "category": category,
                "question": q["question"],
                "score": score,
                "matched": matched,
            })
            st.session_state[f"result_{category}_{q_index}"] = (score, matched)
    with col2:
        if st.button("Show sample answer"):
            st.session_state[f"show_{category}_{q_index}"] = True
    result_key = f"result_{category}_{q_index}"
    if result_key in st.session_state:
        score, matched = st.session_state[result_key]
        st.metric("Practice score (keyword-based)", f"{score}%")
        st.caption("This is a simple self-study indicator based on answer length and topic keywords. It is not an AI assessment or a measure of your real interview performance.")
        if matched:
            st.write("Keywords covered:", ", ".join(matched))
        else:
            st.write("Try including more of the main concepts from the question.")
    if st.session_state.get(f"show_{category}_{q_index}", False):
        st.markdown("#### Sample answer / key points")
        st.success(q["answer"])
    st.caption("Tip: Explain the concept in your own words and include an example when possible.")

elif page == "Mock Interview":
    st.markdown("## 🎙️ Mock Interview")
    st.write("Practice answering one question at a time. Try not to reveal the sample answer until after you respond.")
    category = st.selectbox("Interview focus", list(QUESTION_BANK.keys()), key="mock_category_select")
    if st.button("Start / restart mock interview", type="primary"):
        st.session_state.mock_category = category
        st.session_state.mock_order = list(range(len(QUESTION_BANK[category])))
        random.shuffle(st.session_state.mock_order)
        st.session_state.mock_index = 0
        st.session_state.mock_answers = {}
        st.session_state.mock_revealed = False
    active_category = st.session_state.mock_category
    if not st.session_state.mock_order:
        st.session_state.mock_order = list(range(len(QUESTION_BANK[active_category])))
    order = st.session_state.mock_order
    idx = min(st.session_state.mock_index, len(order) - 1)
    q = QUESTION_BANK[active_category][order[idx]]
    st.progress((idx + 1) / len(order), text=f"Question {idx + 1} of {len(order)}")
    st.markdown(f"### {q['question']}")
    mock_answer = st.text_area("Your spoken answer, typed here", key=f"mock_answer_{active_category}_{idx}", height=160)
    a, b, c = st.columns(3)
    with a:
        if st.button("Reveal key points"):
            st.session_state.mock_revealed = True
    with b:
        if st.button("Save answer"):
            score, matched = score_answer(mock_answer, q)
            st.session_state.attempted.append({
                "category": active_category,
                "question": q["question"],
                "score": score,
                "matched": matched,
            })
            st.success(f"Saved for practice review. Keyword-based score: {score}%")
    with c:
        if st.button("Next question", type="primary"):
            st.session_state.mock_index = (idx + 1) % len(order)
            st.session_state.mock_revealed = False
            st.rerun()
    if st.session_state.get("mock_revealed", False):
        st.info(q["answer"])
    st.caption("For realistic practice, answer aloud first, then type a short summary of what you said.")

elif page == "Coding Round":
    st.markdown("## 💻 Coding Round")
    st.write("Try each problem before opening the hint or solution.")
    coding_titles = [item["title"] for item in CODING_QUESTIONS]
    chosen = st.selectbox("Choose a problem", coding_titles)
    problem = next(item for item in CODING_QUESTIONS if item["title"] == chosen)
    st.markdown(f"### {problem['title']}")
    st.write(problem["prompt"])
    st.text_area("Write your solution here (practice editor)", height=170, key=f"code_{chosen}", placeholder="def solution(...):")
    with st.expander("Show hint"):
        st.write(problem["hint"])
    with st.expander("Show sample solution"):
        st.code(problem["solution"], language="python")
    st.warning("This practice editor does not execute or automatically test your code. Run your solution in a local Python file to verify it.")

elif page == "Resume & Projects":
    st.markdown("## 🧩 Resume & Project Preparation")
    st.write("Use these prompts to prepare clear, honest explanations of your work.")
    st.subheader("Project explanation builder")
    project_name = st.text_input("Project name", placeholder="e.g., SkillSync-AI")
    problem = st.text_area("What problem does it solve?", placeholder="Describe the real problem...")
    technologies = st.text_input("Technologies used", placeholder="Python, Streamlit, scikit-learn...")
    contribution = st.text_area("What did you personally build?", placeholder="Mention your own work...")
    challenge = st.text_area("One challenge and how you solved it", placeholder="Explain the issue and steps...")
    if st.button("Create project speaking notes", type="primary"):
        if not project_name.strip() or not problem.strip() or not technologies.strip():
            st.error("Please enter at least the project name, problem, and technologies.")
        else:
            notes = (
                f"Project: {project_name.strip()}\\n\\n"
                f"Problem: {problem.strip()}\\n\\n"
                f"Technologies: {technologies.strip()}\\n\\n"
                f"My contribution: {contribution.strip() or 'Add your specific contribution.'}\\n\\n"
                f"Challenge and solution: {challenge.strip() or 'Add one real challenge and how you solved it.'}"
            )
            st.text_area("Your project notes", value=notes, height=240)
            st.download_button("Download notes as TXT", data=notes, file_name="project_interview_notes.txt", mime="text/plain")
    st.subheader("Useful project questions")
    for item in [
        "Why did you choose this project?",
        "What is the architecture or workflow?",
        "Why did you choose these technologies?",
        "What was the hardest bug you fixed?",
        "How did you test the project?",
        "What would you improve next?",
    ]:
        st.markdown(f"- {item}")
    st.subheader("Self-introduction outline")
    st.code(
        "1. Education and current status\\n"
        "2. Relevant technical skills\\n"
        "3. One or two projects and your contribution\\n"
        "4. Strengths supported by examples\\n"
        "5. Why this role interests you",
        language="text",
    )

elif page == "About":
    st.markdown("## ℹ️ About PrepPilot AI")
    st.write(
        "PrepPilot AI is a local interview-preparation practice app built with Python and Streamlit. "
        "It includes a curated question bank, sample answers, coding prompts, project speaking notes, "
        "and simple local session progress."
    )
    st.warning(
        "The current version works offline after dependencies are installed. It does not call an external AI model, "
        "does not upload your answers, and its practice score uses simple keyword matching rather than semantic AI evaluation."
    )
    st.markdown("### Tech stack")
    st.write("Python · Streamlit")
    st.markdown("### Suggested future upgrades")
    st.write("- Add an LLM API for detailed answer feedback")
    st.write("- Add user login and a persistent database")
    st.write("- Add resume PDF parsing")
    st.write("- Add speech-to-text for spoken mock interviews")

st.sidebar.divider()
st.sidebar.caption("PrepPilot AI • Local practice app")
