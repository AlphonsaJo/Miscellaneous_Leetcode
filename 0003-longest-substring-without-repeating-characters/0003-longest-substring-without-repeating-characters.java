import java.util.HashSet;

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int maxLen = 0;
        int left = 0, right = 0;

        HashSet<Character> set = new HashSet<>();

        while (right < n) {
            char ch = s.charAt(right);

            // If duplicate found, shrink window from the left
            while (set.contains(ch)) {
                set.remove(s.charAt(left));
                left++;
            }

            // Add current character and update max length
            set.add(ch);
            maxLen = Math.max(maxLen, right - left + 1);

            right++;
        }

        return maxLen;
    }
}
