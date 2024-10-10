def sum_of_min_subarrays(arr):
    mod = 10**9 + 7  
    total_sum = 0  


    for i in range(len(arr)):
        current_min = arr[i] 
  
        for j in range(i, len(arr)):
 
            current_min = min(current_min, arr[j])
            
          
            total_sum = (total_sum + current_min) % mod

    return total_sum  
