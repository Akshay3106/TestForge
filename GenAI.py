import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API key not found in the environment. Make sure the .env file is correctly configured.")

llm = ChatGoogleGenerativeAI(api_key=api_key, model="gemini-1.5-flash-latest")


def output_Generator(newfeatures_comment,single_test_case):

    prompt_template = ChatPromptTemplate.from_messages(
    [
         ("system", 
     "You are an expert software test engineer with extensive experience in updating and optimizing test cases."),
    ("human", 
     "You need to update the provided test case based on the new feature information. Modify the test case JSON according to the latest feature update. \n\n"
     "Instructions:\n"
     "1. Review the provided feature update information.\n"
     "2. Apply necessary changes to the test case JSON.\n"
     "3. Return the updated test case in JSON format only.\n"
     "4. Do not include any additional text, explanations, or comments in the response.\n\n"
     "5. While updating new feature steps or expected result stat with 'u3:' to identify we steps and results"
     "Feature Update Information:\n"
     "{feature_update_info}\n\n"
     "Original Test Case JSON:\n"
     "{test_case_json}\n\n"
     "Updated Test Case JSON:\n"
     "")
    ]
)
    chain = prompt_template | llm | StrOutputParser()
    response = chain.invoke({
    "feature_update_info": newfeatures_comment,
    "test_case_json": single_test_case
    })
    
    return response
