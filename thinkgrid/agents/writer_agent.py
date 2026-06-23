from thinkgrid.models.llm import llm
from thinkgrid.prompts.writer_prompt import WRITER_PROMPT


class WriterAgent:

    def run(
        self,
        topic: str,
        research_summary: str
    ):

        prompt = WRITER_PROMPT.format(
            topic=topic,
            summary=research_summary
        )

        response = llm.invoke(prompt)

        return response.content