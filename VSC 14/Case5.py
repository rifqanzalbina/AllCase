import openai
openai.api_key = "Bearer"

model_engine = "text-davinci-002"

def generate_text(prompt):
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = completions.choices[0].text.strip()
    return message

# Contoh penggunaan
prompt = "Halo, apa kabar?"
response = generate_text(prompt)
print(response)
