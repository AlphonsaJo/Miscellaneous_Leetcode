/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int isPick = guess(n);
        int left = 1;
        int right = n;
        int mid = 0;

        while(left<=right){
            mid = left + (right - left)/2;
            isPick = guess(mid);
            if(isPick == 0){
                // got the number
                break;
            } else if(isPick == -1){
                // guess is higher
                right = mid - 1;
            }else{
                // guess is lower
                left = mid + 1;
            }
        }

        return mid;
        
    }
}