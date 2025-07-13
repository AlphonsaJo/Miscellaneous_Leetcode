class Solution {
    public boolean isIsomorphic(String s, String t) {
        HashMap<Character, Character> forwardMap = new HashMap<>();
        HashMap<Character, Character> reverseMap = new HashMap<>();

        if(s.length() != t.length()){
            return false;
        }

        for(int i = 0; i<s.length(); i++){
            char chS = s.charAt(i);
            char chT = t.charAt(i);

            if(forwardMap.containsKey(chS)){
                if(forwardMap.get(chS) != chT){
                return false;
                } 
            }
            else {
                if(reverseMap.containsKey(chT)){
                    return false;
                }
                forwardMap.put(chS, chT);
                reverseMap.put(chT, chS);
            }
        }
        return true;
    }
}