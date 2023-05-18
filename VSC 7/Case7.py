# import openai
# import os

# # Masukkan API key OpenAI
# openai.api_key = os.environ["OPENAI_API_KEY"]

# # Fungsi untuk menghasilkan teks otomatis menggunakan GPT-3
# def generate_text(prompt):
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )

#     # Mengembalikan teks yang dihasilkan oleh GPT-3
#     return response.choices[0].text.strip()

# # Contoh penggunaan
# prompt = "Apa itu AI?"
# generated_text = generate_text(prompt)
# print(generated_text)

