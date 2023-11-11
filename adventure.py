class AdventureChoice:
    def __init__(self, text, next_node):
        self.text = text
        self.next_node = next_node


class AdventureNode:
    def __init__(self, img, description):
        self.img = img
        self.description = description
        self.choices = []
