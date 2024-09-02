model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
prompt = "Generate a physics problem related to thermodynamics."
inputs = tokenizer(prompt, return_tensors='pt')
outputs = model.generate(**inputs, max_length=100)
question = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(question)
