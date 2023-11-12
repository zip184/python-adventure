class AdventureChoice:
    def __init__(self, text, next_node):
        self.text = text
        self.next_node = next_node


class AdventureNode:
    def __init__(self, img, description):
        self.img = img
        self.description = description
        self.choices = []

    def set_on_arrive(self, on_arrive):
        self.on_arrive = on_arrive

    def fire_on_arrive(self):
        if hasattr(self, 'on_arrive'):
            self.on_arrive()
