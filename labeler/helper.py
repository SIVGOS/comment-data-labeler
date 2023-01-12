def format_label_name(name):
    label_text = '_'.join(name.lower().split())
    if '_' in name:
        name = name.replace('_', ' ')
    display_name = ' '.join([z[0].upper() + z[1::].lower() for z in name.split()])
    return label_text, display_name
