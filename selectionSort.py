class SelectionSort(object):

    def __init__(self, myarray):
        self.myarray = myarray

    def swap(self, myarray, index_a, index_b):
        print 'swap before:', self.myarray
        tmp = self.myarray[index_a]
        self.myarray[index_a] = self.myarray[index_b]
        self.myarray[index_b] = tmp
        print 'swap after:', self.myarray

    def find_min_index(self, myarray, start_index):
        print 'in first find_min_index:', self.myarray
        print start_index
        min_value = self.myarray[start_index]
        min_index = start_index

        for i in range(start_index + 1, len(myarray)):
            if myarray[i] < min_value:
                min_value = myarray[i]
                min_index = i

        print 'i think this is the end of the array so here is lowest index: ' , min_index
        return min_index

    def selection_sort(self):

        print 'in first selection_sort', self.myarray
        for index, item in enumerate(self.myarray):
            min_index = self.find_min_index(self.myarray, index)
            print 'here my min_index:', min_index
            if min_index:
                self.swap(self.myarray, index, min_index)

        print 'i think end of array for selection_sort', self.myarray

ary = [5,3,1,3,2,6]
doit = SelectionSort(ary)
doit.selection_sort()
# doit.swap(ary, 1, 2)
# doit.find_min_index(ary, 1)