class MergeSort(object):

    def __init__(self, array):
        self.array = array

    def sort(self):
        print('Splitting', self.array)
        if len(self.array) > 1:
            m = len(self.array)//2
            left = self.array[:m]
            right = self.array[m:]

            leftSorter  = MergeSort(left)
            leftSorter.sort()
            rightSorter = MergeSort(right)
            rightSorter.sort()

            # sort(right)

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    self.array[k] = left[i]
                    i += 1
                else:
                    self.array[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                self.array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                self.array[k] = right[j]
                j += 1
                k += 1
        print('Merging', self.array)

x = MergeSort([1,6,5,2,10,8,7,4,3,9])
x.sort()