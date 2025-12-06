import numpy as np
text = np.loadtxt('example_text.txt')
print(text) # prints the contents of the file
newtext = "Hello world!"
np.savetxt('example_text.txt', newtext) 
text = np.loadtxt('example_text.txt')
print(text) # "Hello world!"
