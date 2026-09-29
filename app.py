
import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="GEMINI AI CHATBOT",
    page_icon="🤖",
    layout="centered"
)


# =========================================================
# BEAUTIFUL CSS
# =========================================================

st.markdown("""
<style>

/* =====================================================
   FUTURISTIC AI BACKGROUND
===================================================== */

.stApp {

    background:
        linear-gradient(
            rgba(2, 5, 28, 0.78),
            rgba(8, 3, 35, 0.88)
        ),
        url("https://images.unsplash.com/photo-1635070041078-e363dbe005cb?auto=format&fit=crop&w=2200&q=90");

    background-size: cover;

    background-position: center;

    background-attachment: fixed;

    animation: backgroundMove 18s ease-in-out infinite alternate;
}


/* Background movement */

@keyframes backgroundMove {

    0% {
        background-position: 45% 50%;
    }

    50% {
        background-position: 55% 45%;
    }

    100% {
        background-position: 45% 55%;
    }

}


/* =====================================================
   MAIN CONTENT
===================================================== */

.block-container {

    max-width: 900px;

    padding-top: 35px;

    padding-bottom: 70px;

}


/* =====================================================
   TITLE
===================================================== */

h1 {

    text-align: center !important;

    font-size: 56px !important;

    font-weight: 900 !important;

    letter-spacing: 2px !important;

    margin-bottom: 5px !important;

    background:
        linear-gradient(
            90deg,
            #00f0ff,
            #00aaff,
            #6366ff,
            #c43cff,
            #ff3cac,
            #00f0ff
        );

    background-size: 400%;

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

    animation:
        titleFlow 6s linear infinite;

    filter:
        drop-shadow(
            0 0 18px
            rgba(0, 220, 255, 0.45)
        );
}


/* Title animation */

@keyframes titleFlow {

    0% {
        background-position: 0%;
    }

    100% {
        background-position: 400%;
    }

}


/* =====================================================
   NORMAL TEXT
===================================================== */

.stApp p {

    color: #e5edff;

}


/* =====================================================
   PROMPT LABEL
===================================================== */

.stTextArea label {

    color: #ffffff !important;

    font-size: 17px !important;

    font-weight: 700 !important;

}


/* =====================================================
   TEXT AREA
===================================================== */

textarea {

    background:
        rgba(5, 12, 35, 0.88)
        !important;

    color:
        #ffffff
        !important;

    border:
        1px solid
        rgba(0, 225, 255, 0.65)
        !important;

    border-radius:
        20px
        !important;

    font-size:
        17px
        !important;

    padding:
        18px
        !important;

    box-shadow:
        0 0 20px
        rgba(0, 200, 255, 0.12);

    transition:
        all 0.4s ease
        !important;

}


/* Placeholder */

textarea::placeholder {

    color:
        #94a3b8
        !important;

    opacity:
        1
        !important;

}


/* Hover */

textarea:hover {

    border-color:
        #00eaff
        !important;

    box-shadow:
        0 0 25px
        rgba(0, 234, 255, 0.28)
        !important;

    transform:
        translateY(-2px);

}


/* Focus */

textarea:focus {

    border:
        2px solid
        #00d9ff
        !important;

    box-shadow:
        0 0 20px
        rgba(0, 220, 255, 0.45),

        0 0 45px
        rgba(80, 70, 255, 0.25)
        !important;

}


/* =====================================================
   GENERATE BUTTON
===================================================== */

.stButton > button {

    width: 240px;

    height: 58px;

    margin-top: 15px;

    border: none;

    border-radius: 18px;

    color: white;

    font-size: 16px;

    font-weight: 800;

    letter-spacing: 0.5px;

    background:
        linear-gradient(
            90deg,
            #ec4899,
            #a855f7,
            #6366f1,
            #06b6d4,
            #ec4899
        );

    background-size: 400%;

    animation:
        buttonFlow 5s linear infinite;

    box-shadow:
        0 0 20px
        rgba(99, 102, 241, 0.55);

    transition:
        all 0.3s ease;

}


/* Button color animation */

@keyframes buttonFlow {

    0% {
        background-position: 0%;
    }

    100% {
        background-position: 400%;
    }

}


/* Button hover */

.stButton > button:hover {

    transform:
        translateY(-4px)
        scale(1.04);

    box-shadow:

        0 0 25px
        rgba(0, 234, 255, 0.75),

        0 0 50px
        rgba(217, 70, 239, 0.45);

}


/* Button press */

.stButton > button:active {

    transform:
        scale(0.96);

}


/* =====================================================
   SUCCESS MESSAGE
===================================================== */

div[data-testid="stAlert"] {

    border-radius:
        16px;

    background:
        rgba(10, 80, 80, 0.35);

    backdrop-filter:
        blur(12px);

}


/* =====================================================
   RESPONSE
===================================================== */

[data-testid="stMarkdownContainer"] {

    color:
        #e8efff;

}


/* Response animation */

[data-testid="stMarkdownContainer"] p {

    animation:
        responseFade 0.6s ease;

}


@keyframes responseFade {

    from {

        opacity: 0;

        transform:
            translateY(12px);

    }

    to {

        opacity: 1;

        transform:
            translateY(0);

    }

}


/* =====================================================
   SPINNER
===================================================== */

.stSpinner > div {

    border-top-color:
        #00eaff !important;

}


/* =====================================================
   WARNING
===================================================== */

.stAlert {

    border-radius:
        16px !important;

    backdrop-filter:
        blur(12px);

}


/* =====================================================
   SUBTLE GLOW AROUND INPUT AREA
===================================================== */

[data-testid="stTextArea"] {

    animation:
        softGlow 4s ease-in-out infinite alternate;

}


@keyframes softGlow {

    from {

        filter:
            drop-shadow(
                0 0 0
                rgba(0, 220, 255, 0)
            );

    }

    to {

        filter:
            drop-shadow(
                0 0 12px
                rgba(0, 220, 255, 0.10)
            );

    }

}


/* =====================================================
   HIDE STREAMLIT DEFAULT ELEMENTS
===================================================== */

#MainMenu {

    visibility: hidden;

}

header {

    visibility: hidden;

}

footer {

    visibility: hidden;

}


/* =====================================================
   MOBILE RESPONSIVE
===================================================== */

@media (max-width: 700px) {

    h1 {

        font-size: 38px !important;

    }

    .block-container {

        padding-left: 20px;

        padding-right: 20px;

    }

    .stButton > button {

        width: 100%;

    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# CHATBOT TITLE
# =========================================================

st.title("🤖 GEMINI AI CHATBOT")

st.write(
    "✨ Ask • Explore • Create with Artificial Intelligence ✨"
)


# =========================================================
# USER PROMPT
# =========================================================

prompt = st.text_area(
    "💬 Enter your Prompt:",
    placeholder="Example: Explain Artificial Intelligence in simple words...",
    height=150
)


# =========================================================
# GENERATE RESPONSE
# =========================================================

if st.button("✨ GENERATE RESPONSE"):

    if prompt:

        with st.spinner("🤖 Gemini is thinking..."):

            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt
            )

        st.success("✨ Response generated successfully!")

        st.write(response.text)

    else:

        st.warning("⚠️ Please enter a prompt.")
