from sys import argv

BACK_ROOT = argv[1]
DJANGO_APP = argv[2]

new_lines = [ '{% load static %}\n' ]
INDEX_HTML = f'{ BACK_ROOT }/{ DJANGO_APP }/templates/index.html'

with open(INDEX_HTML, 'r') as reader:
    for i, line in enumerate(reader.readlines()):
        if i == 10:
            new_lines.append('  {% csrf_token %}\n')

        new_lines.append(line)


MODULE_NAME = new_lines[8][51:68]
NEW_SCRIPT_LINE = (
    '    <script type="module" crossorigin src="{% static \'' +
    DJANGO_APP +
    '/' +
    MODULE_NAME +
    '\' %}"></script>\n'
)

new_lines[8] = NEW_SCRIPT_LINE

with open(INDEX_HTML, 'w') as writer:
    writer.writelines(new_lines)
