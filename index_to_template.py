from sys import argv

# Command line arguments
BACK_ROOT = argv[1]
DJANGO_APP = argv[2]

# index.html file path
INDEX_HTML = f'{ BACK_ROOT }/{ DJANGO_APP }/templates/index.html'

new_lines = [ '{% load static %}\n' ]

with open(INDEX_HTML, 'r') as reader:
    for line in reader.readlines():
        if 'module' in line:
            MODULE_NAME = line[51:68]
            line = (
                '    <script type="module" crossorigin src="{% static \'' +
                DJANGO_APP +
                '/' +
                MODULE_NAME +
                '\' %}"></script>\n'
            )
        elif 'stylesheet' in line:
            STYLESHEET_NAME = line[53:71]
            line = (
                '    <link rel="stylesheet" crossorigin href="{% static \'' +
                DJANGO_APP +
                '/' +
                STYLESHEET_NAME +
                '\' %}">\n'
            )
        elif 'root' in line:
            new_lines.append('  {% csrf_token %}\n')
        
        new_lines.append(line)
    

with open(INDEX_HTML, 'w') as writer:
    writer.writelines(new_lines)
