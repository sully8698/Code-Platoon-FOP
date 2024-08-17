# time complexity is linear, O(n), due to the function growing based on list length and window size (ie. num)

# Space complexity is constant, O(1), as there just an integer being held in variable "answer"

def maxSubListSum(pos_num_list, num):
  answer = 0
  for i in range(len(pos_num_list)):
    window = pos_num_list[slice(i, i+num)]
    
    if sum(window) > answer:
      answer = sum(window)
  
  if answer == 0:
    return "None"
  
  return answer

print(maxSubListSum([4, 2, 1, 6], 1))