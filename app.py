import streamlit as st

from thinkgrid.workflow.research_pipeline import ResearchPipeline


st.set_page_config(
    page_title="ThinkGrid",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 ThinkGrid")
st.subheader("AI-Powered Deep Research Assistant")

st.markdown(
    """
Enter a research topic and ThinkGrid will:

- Create a research plan
- Search the web
- Analyze sources
- Generate a research report
- Critique its own report
"""
)

topic = st.text_input(
    "Research Topic",
    placeholder="e.g. Future of AI Agents"
)

generate_btn = st.button(
    "Generate Research",
    type="primary"
)

if generate_btn:

    if not topic.strip():
        st.warning("Please enter a research topic.")
        st.stop()

    pipeline = ResearchPipeline()

    with st.spinner(
        "ThinkGrid is conducting research..."
    ):
        result = pipeline.run(topic)

    if not result["success"]:
        st.error(result["error"])
        st.stop()

    st.success("Research Completed")

    with st.expander(
        "📋 Research Plan",
        expanded=True
    ):
        st.markdown(
            result["research_plan"]
        )

    with st.expander(
        "🔍 Sources"
    ):

        sources = result["sources"]

        for idx, source in enumerate(
            sources,
            start=1
        ):

            st.markdown(
                f"### {idx}. {source['title']}"
            )

            st.markdown(
                f"**URL:** {source['url']}"
            )

            st.write(
                source["content"]
            )

            st.divider()

    with st.expander(
        "📖 Research Summary"
    ):
        st.markdown(
            result["summary"]
        )

    st.markdown("## 📑 Research Report")

    st.markdown(
        result["report"]
    )

    with st.expander(
        "🧐 Critic Review"
    ):
        st.markdown(
            result["review"]
        )

    st.download_button(
        label="⬇️ Download Report",
        data=result["report"],
        file_name=f"{topic.replace(' ', '_')}.md",
        mime="text/markdown"
    )

    if result.get("saved_path"):

        st.info(
            f"Report saved to: {result['saved_path']}"
        )