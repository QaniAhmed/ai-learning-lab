from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate,HumanMessagePromptTemplate,SystemMessagePromptTemplate
from langchain_openai import ChatOpenAI
model = ChatOpenAI(
    openai_api_key="secret",
    model="gpt-4o",
    max_tokens=500
)

#Define raw Template string 
user_T = "explain {topic}"
system_T= "you are marvel a helpful asistant ai"

# convert to meassage Template 
system_template = SystemMessagePromptTemplate.from_template(system_T)
user_template = HumanMessagePromptTemplate.from_template(user_T)

# combine both in one chatprompt 
chat_prompt = ChatPromptTemplate.from_messages([system_template,user_template])
chat_prompt_value = chat_prompt.invoke({"topic":"AI"})

#pass to the model 
response = model.invoke(chat_prompt_value.to_messages())
print(response)