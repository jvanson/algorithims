class SelectionSort(object):

    def __init__(self, myarray):
        self.myarray = myarray

    def swap(self, myarray, index_a, index_b):
        print myarray
        print index_a
        print index_b

    # def find_min_index():

    def selection_sort(self):
        print self.myarray
        print "hi"

ary = [5,3,1]
doit = SelectionSort(ary)
doit.selection_sort()
doit.swap(ary, 1, 2)