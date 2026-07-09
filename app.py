import streamlit as st

from src.generation.gemini_chain import GeminiRAG

# --------------------------------------------------------
# Page Config
# --------------------------------------------------------

st.set_page_config(
    page_title="Historical Event Analyst",
    page_icon="📚",
    layout="wide"
)

# --------------------------------------------------------
# Session State
# --------------------------------------------------------

if "rag" not in st.session_state:
    st.session_state.rag = GeminiRAG()

if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------------
# Sidebar
# --------------------------------------------------------

with st.sidebar:

    st.title("⚙️ Historical Event Analyst")

    st.markdown("---")

    st.markdown("### About")

    st.write(
        """
This application uses

- Gemini 2.5 Flash
- Gemini Embeddings
- FAISS Vector Database
- Retrieval Augmented Generation (RAG)

to answer questions from your World War I documents.
"""
    )

    st.markdown("---")

    st.markdown("### Sample Questions")

    examples = [

        "Why did World War I begin?",

        "Explain the July Crisis.",

        "Who was Gavrilo Princip?",

        "What was the Schlieffen Plan?",

        "Describe the Battle of Verdun.",

        "Explain trench warfare.",

        "Why did America enter World War I?",

        "What caused the Russian Revolution?"

    ]

    for question in examples:

        if st.button(question):

            st.session_state.example = question

    st.markdown("---")

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# --------------------------------------------------------
# Title
# --------------------------------------------------------

st.title("📚 Historical Event Analyst")

st.caption(
    "Gemini + FAISS Retrieval-Augmented Generation"
)

st.divider()

# --------------------------------------------------------
# Display Previous Messages
# --------------------------------------------------------

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

        if msg["role"] == "assistant":

            if "sources" in msg:

                with st.expander("📖 Retrieved Sources"):

                    for source in msg["sources"]:

                        meta = source["metadata"]

                        st.markdown(
                            f"""
### {meta['chapter']}

**File:** {meta['filename']}

**Chunk:** {meta['chunk_id']}

---

{source['text']}
"""
                        )

# --------------------------------------------------------
# Input
# --------------------------------------------------------

default_question = st.session_state.pop("example", "")

question = st.chat_input(
    "Ask anything about World War I..."
)

if default_question:
    question = default_question

# --------------------------------------------------------
# Generate Answer
# --------------------------------------------------------

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Searching documents..."):

            try:

                response = st.session_state.rag.ask(question)

                answer = response["answer"]

                docs = response["documents"]

                st.markdown(answer)

                with st.expander("📖 Retrieved Sources"):

                    for source in docs:

                        meta = source["metadata"]

                        st.markdown(
                            f"""
### {meta['chapter']}

**File:** {meta['filename']}

**Chunk:** {meta['chunk_id']}

---

{source['text']}
"""
                        )

                st.session_state.messages.append(

                    {
                        "role": "assistant",

                        "content": answer,

                        "sources": docs
                    }

                )

            except Exception as e:

                st.error(str(e))

# --------------------------------------------------------
# Footer
# --------------------------------------------------------

st.divider()

st.caption(
    "Historical Event Analyst • Gemini 2.5 Flash • FAISS • Streamlit"
)