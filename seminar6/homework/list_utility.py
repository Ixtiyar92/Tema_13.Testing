class Utility:

    def __init__(self, list1: list, list2: list):
        self.list1 = list1
        self.list1_average = self.get_average(list1)
        self.list2 = list2
        self.list2_average = self.get_average(list2)

    @staticmethod
    def get_average(list_number):
        if len(list_number) > 0:
            return sum(list_number) / len(list_number)
        else:
            return 0

    def compare_lists(self):
        if self.list1_average > self.list2_average:
            return "Первый список имеет большее среднее значение"
        elif self.list1_average < self.list2_average:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"
