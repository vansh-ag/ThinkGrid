from thinkgrid.models.llm import llm
from thinkgrid.prompts.reader_prompt import READER_PROMPT


class ReaderAgent:

    def run(self, search_results):

        sources = "\n\n".join(
            [
                f"""
Title: {item['title']}
URL: {item['url']}
Content: {item['content']}
"""
                for item in search_results
            ]
        )

        prompt = READER_PROMPT.format(
            sources=sources
        )

        response = llm.invoke(prompt)

        return response.content