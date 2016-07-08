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
		min_index = start_index
		min_value = myarray[start_index]

		for i in (start_index + 1)..(myarray.length - 1)
			# puts "index: #{i} value: #{myarray[i]}"
			if myarray[i] < min_value
				min_value = myarray[i]
				min_index = i
			end
		end

		return min_index


	end

	def selectionsort
		puts "Original array: #{@myarray}"

		# scan entire array

			# find lowest number and return its index
				# if its return swap current index with lowest number index
		@myarray.each_index do | i |
			min_index = findminindex(@myarray, i)
			if min_index
				swap(@myarray, i, min_index)

			end
		end

		puts "Sorted array: #{@myarray}"

	end

arry = [3,2,5,1,8]
doit = SelectionSort.new(arry)
doit.selectionsort
#doit.swap(arry, 0,1)
#doit.selectionsort
#doit.findminindex(arry, 0)



end