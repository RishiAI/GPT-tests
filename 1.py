from transformers import BertTokenizer, BertModel

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

text = "Explain the first law of thermodynamics."
inputs = tokenizer(text, return_tensors='pt')
outputs = model(**inputs)

