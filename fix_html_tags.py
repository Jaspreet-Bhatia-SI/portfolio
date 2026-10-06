with open('portfolio.html', 'r') as f:
    html = f.read()

bad_closing = """            </div>
        </div>
            </div>
        </div>
    <!-- Virtual Joystick -->"""

good_closing = """            </div>
        </div>
    </div>
    <!-- Virtual Joystick -->"""

html = html.replace(bad_closing, good_closing)

with open('portfolio.html', 'w') as f:
    f.write(html)
