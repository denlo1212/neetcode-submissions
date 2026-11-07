class Solution:
    def groupAnagrams(self, strings: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for string in strings:
            count = [0] * 26  # a ... z

            for character in string:
                count[ord(character) - ord("a")] += 1

            result[tuple(count)].append(string)
        return list(result.values())