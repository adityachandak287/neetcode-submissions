class Solution:

    def encode(self, strs: List[str]) -> str:
        import json
        return json.dumps(strs)

    def decode(self, s: str) -> List[str]:
        import json
        return json.loads(s)
