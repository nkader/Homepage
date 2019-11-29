# First, get the template files

top = open('templates/templates_top.html').read()
bottom = open('templates/templates_bottom.html').read()

# Read in index HTML code
indexcontent = open('content/index_content.html').read()

# Combine template HTML code with content HTML code
index_html = top + indexcontent + bottom
open('docs/index.html', 'w+').write(index_html)

contactcontent = open('cotent/contact_content.html').read()
contact_html = top + contactcontent + bottom
open('docs/contact.html', 'w+').write(index_html)

projectcontent = open('content/project_content').read()
projects_html = top + projectcontent + bottom
open('docs/projects.html', 'w+').write(index_html)


