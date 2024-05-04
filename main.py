import google.generativeai as genai


genai.configure(api_key="AIzaSyCo9olXYyXneNhjrznfT5ZsflaRFnKI7fI")

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What is the meaning of life?")

print(response.candidates[0].content.parts[0].text)