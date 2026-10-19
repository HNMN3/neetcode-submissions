class Solution:
    

    def encode(self, strs: List[str]) -> str:
        final = ""
        for s in strs:
            s_len = len(s)
            final += f"{len(str(s_len))}{s_len}{s}"
        return final

    def decode(self, s: str) -> List[str]:
        strs = []
        while s:
            n, s = int(s[0]), s[1:]
            s_len, s = int(s[:n]), s[n:]
            actual_str, s = s[:s_len], s[s_len:]
            strs.append(actual_str)
        return strs
