class Solution {
        public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<String, Integer> hashS = new HashMap<String, Integer>();
        HashMap<String, Integer> hashT = new HashMap<String, Integer>();
        for (int i = 0; i < s.length(); i++) {
            hashS.put(String.valueOf(s.charAt(i)), hashS.getOrDefault(String.valueOf(s.charAt(i)), 0) + 1);
            hashT.put(String.valueOf(t.charAt(i)), hashT.getOrDefault(String.valueOf(t.charAt(i)), 0) + 1);
        }

        return hashS.equals(hashT);
    }
}
