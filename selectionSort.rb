#!/usr/local/bin/ruby

class SelectionSort
	def initialize(myarray)
		@myarray = myarray

	end

	def swap(myarray, index_a, index_b)
		# given input of array, indexA and indexB swap value of indexA with indexB.
		# and swap index B with indexA
		temp = myarray[index_a]
		myarray[index_a] = myarray[index_b]
		myarray[index_b] = temp

	end

	def findminindex(myarray, start_index)
		# given array and startIndex, iterate through array starting with startindex+1
		# and find lowest number from entire subarray.
		# after iteration is done, return index of lowest number 
		# myarray.each do | x |
		(myarray[start_index+1]..myarray.length).each do | x |
			puts x
		end


	end

	def selectionsort

		# scan entire array

			# find lowest number and return its index
				# if its return swap current index with lowest number index
		@myarray.each do | x |
			puts x
		end

	end

arry = [3,2,5]
doit = SelectionSort.new(arry)
doit.selectionsort
doit.swap(arry, 0,1)
doit.selectionsort
doit.findminindex(arry, 0)



end