class ViewModel:
    def __init__(self, items: list[item]):
        self._items = items
 
    @property
    def items(self):
        return self._items