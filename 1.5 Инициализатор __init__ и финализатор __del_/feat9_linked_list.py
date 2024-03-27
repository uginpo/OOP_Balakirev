class ListObject():
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

    def push_back(self, object):
        self.next = object

    def length(self):

        if self.data is None:
            return 0

        temp = self
        count = 1
        while temp.next:
            temp = temp.next
            count += 1
        return count

    def __str__(self) -> str:
        return f'{self.data} -> {self.next}'


linked_list = list(range(6))
head = ListObject(linked_list[0])

temp = head
for i in range(1, len(linked_list)):
    obj = ListObject(linked_list[i])
    temp.push_back(obj)
    temp = obj

print(head)
