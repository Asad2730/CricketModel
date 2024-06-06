import spacy
from spacy.training import Example
from spacy.util import minibatch, compounding
import random
from train_data import TRAINING_DATA

nlp = spacy.blank("en")
ner = nlp.add_pipe("ner")

LABELS = ["RUNS", "BOWLER", "BATSMAN", "DELIVERY", "DISMISSAL"]

for label in LABELS:
    ner.add_label(label)

optimizer = nlp.begin_training()

for i in range(100): 
    random.shuffle(TRAINING_DATA)
    losses = {}
    for batch in minibatch(TRAINING_DATA, size=compounding(4.0, 32.0, 1.001)):
        examples = []
        for text, annotations in batch:
            doc = nlp.make_doc(text)
            biluo_tags = spacy.training.offsets_to_biluo_tags(doc, annotations['entities'])
            examples.append(Example.from_dict(doc, {"entities": annotations['entities'], "tags": biluo_tags}))
        nlp.update(examples, drop=0.5, losses=losses)
    print(f"Iteration {i}: Losses {losses}")

# Save the model
nlp.to_disk("cricket_ner_model")
print("Model trained and saved successfully!")
