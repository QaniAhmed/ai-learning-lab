from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

parser = StrOutputParser()

model = ChatOpenAI(
    openai_api_key="secret",
    model="gpt-4o",
    max_tokens=100
)

# Prompt 1: explanation
explain_template = ChatPromptTemplate.from_template(
    "Explain {topic}"
)

# Prompt 2: examples
example_template = ChatPromptTemplate.from_template(
    "Give me two examples about {topic}"
)

# Chains
explain_chain = explain_template | model | parser
example_chain = example_template | model | parser

# Run in parallel
runnable = RunnableParallel({
    "explain": explain_chain,
    "examples": example_chain
})

result = runnable.invoke({"topic": "AI"})

print(result)