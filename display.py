class DisplayMessage():
    def __init__(self, items, width, filler, endfiller, endline):
        self.display(items, width, filler, endfiller, endline)

    def display(self, items, width, filler, endfiller, endline):
        for s in items:
            print(s.center(width, filler))
        
        if endline:
            print(endfiller.center(width, filler))
        print()

class PrettyDisplay(DisplayMessage):
    def __init__(self, *args):
        super().__init__(args, 70, '=', '**********', True)
    

class AlertMessage(DisplayMessage):
    def __init__(self, message):
        items = ["", message]
        super().__init__(items, 70, '=', '!!!!!!!!!!', True)

