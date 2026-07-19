"""
AI Summary Generator

Uses OpenAI to summarize ticket execution
"""

from langchain_openai import ChatOpenAI

from langchain.prompts import PromptTemplate


class AISummary:

    def __init__(self):

        self.llm = ChatOpenAI(

            model="gpt-4o",

            temperature=0

        )

    def summarize(self, execution_log):

        prompt = PromptTemplate(

            input_variables=["log"],

            template="""

You are Telecom AI Support.

Summarize below execution.

Provide:

Issue

Root Cause

Resolution

Recommendation

Execution Log:

{log}

"""

        )

        chain = prompt | self.llm

        return chain.invoke(

            {

                "log": execution_log

            }

        ).content