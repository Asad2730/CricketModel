import spacy
from spacy.tokens import Span


nlp = spacy.blank("en")

doc1 = nlp("The batsman hit a 6 over the boundary.")
doc1.ents = [
    Span(doc1, 1, 2, label="ROLE"),
    Span(doc1, 3, 4, label="SCORE"),
   
]


doc2 = nlp("The bowler delivered a yorker.")
doc2.ents = [
    Span(doc2, 1, 2, label="ROLE"),
    Span(doc2, 3, 4, label="DELIVERY_TYPE"),
]


doc3 = nlp("LBW is a common method of dismissal.")
doc3.ents = [
    Span(doc3, 0, 1, label="DISMISSAL_METHOD"),
]


doc4 = nlp("The umpire signaled a no-ball.")
doc4.ents = [
    Span(doc4, 1, 2, label="ROLE"),
    Span(doc4, 3, 4, label="SIGNAL"),
]


doc5 = nlp("Hit Wicket is a method of dismissal.")
doc5.ents = [
    Span(doc5, 0, 2, label="DISMISSAL_METHOD"),
]


doc6 = nlp("The batsman was bowled out.")
doc6.ents = [
    Span(doc6, 1, 2, label="ROLE"),
    Span(doc6, 3, 4, label="DISMISSAL_METHOD"),
]


doc7 = nlp("The batsman was caught behind by the wicketkeeper.")
doc7.ents = [
    Span(doc7, 1, 2, label="ROLE"),
    Span(doc7, 3, 5, label="DISMISSAL_METHOD"),
    Span(doc7, 8, 9, label="ROLE"),
]


doc8 = nlp("The batsman hit a 4 to the boundary.")
doc8.ents = [
    Span(doc8, 1, 2, label="ROLE"),
    Span(doc8, 3, 4, label="SCORE"),
    Span(doc8, 7, 8, label="LOCATION"),
]


doc9 = nlp("The batsman took 3 runs.")
doc9.ents = [
    Span(doc9, 1, 2, label="ROLE"),
    Span(doc9, 3, 5, label="SCORE"),
]


doc10 = nlp("The batsman took 2 runs.")
doc10.ents = [
    Span(doc10, 1, 2, label="ROLE"),
    Span(doc10, 3, 5, label="SCORE"),
]


doc11 = nlp("The batsman took a single run.")
doc11.ents = [
    Span(doc11, 1, 2, label="ROLE"),
    Span(doc11, 4, 6, label="SCORE"),
]

doc12 = nlp("The bowler bowled a dot ball.")
doc12.ents = [
    Span(doc12, 1, 2, label="ROLE"),
    Span(doc12, 4, 6, label="SCORE"),
]


doc13 = nlp("The bowler bowled a maiden over.")
doc13.ents = [
    Span(doc13, 1, 2, label="ROLE"),
    Span(doc13, 4, 6, label="SCORE"),
]


doc14 = nlp("The bowler bowled a wicket maiden.")
doc14.ents = [
    Span(doc14, 1, 2, label="ROLE"),
    Span(doc14, 4, 6, label="SCORE"),
]


doc15 = nlp("The batsman was run out.")
doc15.ents = [
    Span(doc15, 1, 2, label="ROLE"),
    Span(doc15, 3, 5, label="DISMISSAL_METHOD"),
]


for doc in [doc1, doc2, doc3, doc4, doc5, doc6, doc7, doc8, doc9, doc10, doc11, doc12, doc13, doc14, doc15]:
    print([(ent.text, ent.label_) for ent in doc.ents], f"-- {doc.text}")
