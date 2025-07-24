class Solution {
    public boolean isAnagram(String s, String t) {
        s = s.replaceAll("\\s", "");
        t = t.replaceAll("\\s", "");

        if(s.length() != t.length()){
            return false;
        }

        char[] charS = s.toCharArray();
        char[] charT = t.toCharArray();

        Arrays.sort(charS);
        Arrays.sort(charT);

        return Arrays.equals(charS, charT);
    }
}