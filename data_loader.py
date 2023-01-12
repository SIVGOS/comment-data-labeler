import random
import pandas as pd
from labeler.helper import format_label_name
from labeler.models import Comment, Labels

def load_data():
    df = pd.read_csv('data/all_comments.csv')

    data = df.to_dict(orient='records')
    random.shuffle(data)
    N = len(data)

    if not Comment.objects.first():
        for i, z in enumerate(data):
            Comment.objects.create(**z)
            print(f'Completed {i} of {N}', end='\r' if i<N-1 else '\n')
    else:
        print('Nothing to load')


def make_labels():
    labels = ["timestamp", "thanks", "greetings", "question", "doubt", "suggestion", "future-question", "disagree", "other", "non-english"]
    for label in labels:
        label_text, display_name = format_label_name(label)
        Labels.objects.create(label_text=label_text, display_text=display_name)

'''
from data_loader import make_labels, load_data
make_labels()
load_data()
'''