import random
import pandas as pd
from labeler.models import Comment

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
