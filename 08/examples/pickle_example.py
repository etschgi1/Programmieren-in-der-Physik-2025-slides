import pickle

# Create a dictionary
dic_ = {'a': 1, 'b': 2, 'c': 3}
with open('slides/08/examples/dic_.pkl', 'wb') as f:
    pickle.dump(dic_, f)
with open('slides/08/examples/dic_.pkl', 'rb') as f:
    data = pickle.load(f)
    print(f"Original data: {data}")
