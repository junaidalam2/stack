
###

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.



Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]


Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

###

temperatures = [73,74,75,71,69,72,76,73]
temperatures = [30,40,50,60]
temperatures = [30,60,90]

def dailyTemperature(temperatures):

  output_array = []
  
  for i in range(1, len(temperatures)):
    if(i - 1 < i):
      output_array.append(1)
    else:
      output_array.append(0)

  return output_array

print(dailyTemperature(temperatures))



# solution

class Solution(object):
  def dailyTemperatures(self, temperatures):
    n = len(temperatures)
    ans = [0 for _ in range(n)]
    st = []
    for i in range(0, n):
        while (len(st)>0) and temperatures[i]> temperatures[st[len(st)-1]]:
            index = st[len(st)-1]
            st.pop()
            ans[index] = i-index
        st.append(i)
    return list(ans)