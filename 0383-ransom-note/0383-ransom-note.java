class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {

        HashMap<Character, Integer> letterCount = new HashMap<>();

        for(int i = 0; i<magazine.length(); i++){
            char ch = magazine.charAt(i);

            if(letterCount.containsKey(ch)){
                int count = letterCount.get(ch);
                letterCount.put(ch, count+1);
            }
            else{
                letterCount.put(ch, 1);
            }
        }

        for(int i = 0; i<ransomNote.length(); i++){

            char ch = ransomNote.charAt(i);

            if(!letterCount.containsKey(ch) || letterCount.get(ch) == 0){
                return false;
            }

            int count = letterCount.get(ch);
            letterCount.put(ch, count-1);
        }
        return true;

    }
}