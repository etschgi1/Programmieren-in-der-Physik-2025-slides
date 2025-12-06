replacements = {'bad': 'good', 'ugly': 'beautiful', 'hate': 'love'}
s = 'I hate bad weather. It makes me feel ugly.'
for word in s.split():
    if word in replacements:
        s = s.replace(word, replacements[word])
print(s)  # I love good weather. It makes me feel beautiful.
