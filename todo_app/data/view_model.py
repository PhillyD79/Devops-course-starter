class ViewModel:
    def __init__(self, items: list[item]):
        self._items = items
 
    @property
    def items(self):
        return self._items

    @property
    def todo_items(self):
        output = []

        for item in self._items:
            if item.status == "To Do"
                output.append(item)

    @property
    def doing_items(self):
        output = []

        for item in self._items:
            if item.status == "Doing"
                output.append(item)

    @property
    def done_items(self): -> list[Item]:
        output = []

        for item in self._items:
            if item.status == "Done"
                output.append(item)