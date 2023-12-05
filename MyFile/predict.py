from MyFile.library import *
from MyFile.utils import *

class_names = ['Enjoyment', 'Disgust', 'Sadness', 'Anger', 'Surprise', 'Fear', 'Other']
# Initialize model and tokenizer
model = SentimentClassifier(n_classes=7)
with open("MyFile/tokennizer_data.pkl", "rb") as input_file:
    tokenizer = pickle.load(input_file)
    
model.load_state_dict(torch.load('MyFile/model_2.pth', map_location=torch.device('cuda')))

model.eval()  # Put the model into evaluation mode to disable dropout and batch normalization

def infer(text):
    text = clean_Sentence(text) 
    CHECK = emoji_pro(text)
    if CHECK == "STR":
        encoded_review = tokenizer.encode_plus(
            text,
            max_length=80,
            truncation=True,
            add_special_tokens=True,
            padding='max_length',
            return_attention_mask=True,
            return_token_type_ids=False,
            return_tensors='pt',
        )

        with torch.no_grad():
            output = model(**encoded_review)
        _, y_pred = torch.max(output, dim=1)
        predicted_sentiment = class_names[y_pred.item()]

        return predicted_sentiment

    else: 
        return CHECK

