import numpy as np
import matplotlib.pyplot as plt
file_path = '/content/marksheet_one.xlsx'

Marks = ['Physics' , 'Maths' , 'Biology' , 'Chemistry' , 'English']
scores=[40,60,75,80,93]

scores_np = np.array(scores)

plt.figure(figsize=(7,5))
plt.bar(Marks, scores_np, color='lightgreen')
plt.xlabel('Subjects')
plt.ylabel('Scores')
plt.title('Student Scores Bar Graph')
plt.show()