with open('portfolio.html', 'r') as f:
    html = f.read()

html = html.replace("window.open('https://curator-ai.foodzie.store', '_blank')", "window.open('https://curator.foodzie.store', '_blank')")

with open('portfolio.html', 'w') as f:
    f.write(html)
print("Link updated")
