from thinkgrid.models.llm import llm
from thinkgrid.prompts.critic_prompt import CRITIC_PROMPT


class CriticAgent:

    def run(self, report: str):

        prompt = CRITIC_PROMPT.format(
            report=report
        )

        response = llm.invoke(prompt)

        return response.content