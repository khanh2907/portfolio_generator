from yattag import Doc

doc, tag, text = Doc().tagtext()

with tag('h1'):
    text('Portfolio')

with tag('div', id='alveo', klass='project'):
    with tag('h2', klass='title'):
        text('Alveo')




print(doc.getvalue())