class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
     HashMap<String, List<String>> hashMap = new HashMap<>();
        for (String word : strs) {
            char[] charList = word.toCharArray();
            Arrays.sort(charList);
            String sortedWord = new String(charList);
            hashMap.computeIfAbsent(sortedWord, k -> new ArrayList<>()).add(word);
        }
        
        return new ArrayList<>(hashMap.values());
    }
}
