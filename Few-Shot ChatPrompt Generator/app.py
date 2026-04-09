from langchain_core.prompts import (ChatPromptTemplate,
                                    FewShotChatMessagePromptTemplate,
                                    HumanMessagePromptTemplate,
                                    AIMessagePromptTemplate)
from langchain_openai import ChatOpenAI
model = ChatOpenAI(
    openai_api_key="secret",
    model="gpt-4o",
    max_tokens=500
)

Human_T = "i've bought a {pet} can you give me suggested name for my {pet}"
Ai_T = "Suggested name: {response}"

Human_Template = HumanMessagePromptTemplate.from_template(Human_T)
Ai_Template  = AIMessagePromptTemplate.from_template(Ai_T)

# blue-print
example_prompt = ChatPromptTemplate.from_messages([Human_Template,Ai_Template])

examples = [
    {"pet": "dog", "response": "Max, Lily, Buddy"},
    {"pet": "cat", "response": "Whiskers, Luna, Milo"},
    {"pet": "bird", "response": "Sky, Coco, Kiwi"}
]

fsprompt= FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
    input_variables=["pet"]
)

chatPrompt = ChatPromptTemplate.from_messages([
    fsprompt,
    Human_Template 
])
chat_tvalue= chatPrompt.invoke({"pet":"dragon"})
response = model.invoke(chat_tvalue.to_messages())
print(response.content)




