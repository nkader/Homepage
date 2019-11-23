# First, get the template files
top_template = open('templates_top.html').read()
bottom_template = open('templates_bottom.html').read()

# Read in index HTML code
content = open('content_index.html').read()

# Combine template HTML code with content HTML code
index_html = top_template + content + bottom_template
open('index.html', 'w+').write(index_html)

content = open('contact_content.html').read()
about_html = top_template + content + bottom_template
