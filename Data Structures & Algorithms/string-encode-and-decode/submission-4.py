class Solution:

    def encode(self, strs: List[str]) -> str:
        if not len(strs):
            return ""

        lens = [str(len(s)) for s in strs]
        return "\n".join([",".join(lens), "".join(strs)])

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        offset = s.find("\n")
        lens = list(map(int, s[:offset].split(",")))

        result = []
        start = offset + len('\n')
        for l in lens:
            result.append(s[start: start+l])
            start = start+l
        
        return result

