from langchain_core.runnables import RunnableParallel
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

model = ChatOpenAI(
    openai_api_key="sk-Secret",
    model="gpt-4o",
    temperature=0.8,
    max_tokens=500
)


Roadmap_template= ChatPromptTemplate.from_template("Create a step-by-step roadmap to learn {topic} from beginner to advanced")
Resources_template=ChatPromptTemplate.from_template("Suggest best courses, websites, and books for learning {topic}")
Projects_template=ChatPromptTemplate.from_template("Suggest 2 beginner, 2 intermediate, 2 advanced projects for {topic}")
Study_Plan_template=ChatPromptTemplate.from_template("Create a 10-day study plan for learning {topic}")

Roadmap_chain = Roadmap_template | model | parser
Resources_chain = Resources_template | model | parser
Projects_chain = Projects_template | model | parser
Study_Plan_chain = Study_Plan_template | model | parser

runnable = RunnableParallel({'Roadmap':Roadmap_chain,'Resources':Resources_chain,'Projects':Projects_chain,'Study_Plan':Study_Plan_chain})

# chain = runnable | parser

res = runnable.invoke({'topic':'cyper'})
print(res)
