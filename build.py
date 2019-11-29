# First, get the template files
from pathlib import Path

templates_top = Path("templates/template_top.html")

top = open('templates_top.html').read()
bottom = open('templates_bottom.html').read()

# Read in index HTML code
indexcontent = open('index_content.html').read()

# Combine template HTML code with content HTML code
index_html = top + indexcontent + bottom
open('index.html', 'w+').write(index_html)

contactcontent = open('contact_content.html').read()
contact_html = top + contactcontent + bottom

projectcontent = open('project_content').read()
projects_html = top + projectcontent + bottom


