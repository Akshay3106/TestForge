import locallay
import langchain
# Load the Ollama model
ollama_model = locallay.load_model("C:\\Users\\AkshayPatil\\AppData\\Local\\Programs\\Ollama\\ollama.exe")

# Create a LangChain instance


# Prompt the user for the feature details
feature_details = input("Enter the feature details: ")

# Chain the feature details
chained_input = langchain.chain_input(feature_details)

# Set the role of the model
role = "tester"  # You can set the role based on your requirements
chained_input.set_role(role)

# Format the response
response_format = "json"  # You can choose the desired response format
chained_input.set_response_format(response_format)

# Increase efficiency by setting the max tokens and temperature
max_tokens = 100  # Set the maximum number of tokens for the generated test cases
temperature = 0.8  # Set the temperature for controlling randomness in generation

# Generate the test cases using LangChain
generated_test_cases = langchain.generate_test_cases(chained_input, model=ollama_model, max_tokens=max_tokens, temperature=temperature)

# Print the generated test cases
print("Generated test cases:")
for i, test_case in enumerate(generated_test_cases):
    print(f"Test ID: {i+1}")
    print("Summary:")
    print(test_case["summary"])
    print("Description:")
    print(test_case["description"])
    print("Expected Result:")
    print(test_case["expected_result"])
    print()
    print("------------------------------")
