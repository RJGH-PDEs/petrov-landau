import pickle

# Open the file
with open('results.pkl', 'rb') as file:
    # load the data
    data = pickle.load(file)

# print lenght of data
print(len(data))

# print it
for d in data:
    print(d)
    print()

