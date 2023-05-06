def pretty_display(items, width=70, filler='=', endfiller='*********', endline=True):
    for s in items:
        print(s.center(width, filler))
    
    if endline:
        print(endfiller.center(width, filler))
    print()
