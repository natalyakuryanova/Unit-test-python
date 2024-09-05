class List:
    def __init__(self, newlist):
        self.newlist = newlist

    # Find average
    def find_average(self):
        if not self.newlist:
            return 0
        return sum(self.newlist) / len(self.newlist)


class Comparator:
    def __init__(self, newobjlist1, newobjlist2):
        self.newobjlist1 = List(newobjlist1)
        self.newobjlist2 = List(newobjlist2)

    def compare(self):
        print(self.newobjlist1.newlist)
        print(self.newobjlist2.newlist)

        avg1 = self.newobjlist1.find_average()
        avg2 = self.newobjlist2.find_average()
        print(avg1)
        print(avg2)

        if avg1 > avg2:
            return "Первый список имеет большее среднее значение"
        elif avg2 > avg1:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"

# Main code
# test = Comparator([1, 2, 6], [1, 2, 6, 7])
# res = test.compare()
# print(res)
