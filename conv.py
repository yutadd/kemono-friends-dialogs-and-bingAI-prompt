import markdown

with open('all.md', 'r') as f:
    text = f.read()

html = markdown.markdown(text)

with open('yourfile.html', 'w') as f:
    f.write(html)