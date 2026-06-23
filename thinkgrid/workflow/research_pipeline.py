from thinkgrid.agents.search_agent import SearchAgent
from thinkgrid.agents.reader_agent import ReaderAgent
from thinkgrid.agents.writer_agent import WriterAgent
from thinkgrid.agents.critic_agent import CriticAgent


class ResearchPipeline:

    def __init__(self):
        self.search_agent = SearchAgent()
        self.reader_agent = ReaderAgent()
        self.writer_agent = WriterAgent()
        self.critic_agent = CriticAgent()

    def run(self, topic: str):

        try:

            print(f"\n🔍 Starting research on: {topic}")

            print("📋 Creating research plan...")
            search_output = self.search_agent.run(topic)

            research_plan = search_output["research_plan"]
            sources = search_output["sources"]

            print(f"✅ Found {len(sources)} sources")

            print("📖 Analyzing sources...")
            summary = self.reader_agent.run(sources)

            print("✍️ Generating report...")
            report = self.writer_agent.run(
                topic=topic,
                research_summary=summary
            )

            print("🧐 Reviewing report...")
            review = self.critic_agent.run(report)

            print("✅ Research completed successfully")

            return {
                "success": True,
                "topic": topic,
                "research_plan": research_plan,
                "sources": sources,
                "summary": summary,
                "report": report,
                "review": review,
            }

        except Exception as e:

            print(f"❌ Pipeline Error: {e}")

            return {
                "success": False,
                "topic": topic,
                "error": str(e),
            }