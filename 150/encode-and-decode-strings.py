class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""

        result = ""

        for s in strs:
            result += str(len(s)) + "$" + s

        return result

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""

        result = []

        i = 0

        while i < len(s):
            n = ""

            while s[i] != "$":
                n += s[i]
                i += 1
            i += 1
            n = int(n)
            result.append(s[i : i + n])
            i = i + n

        return result


c = Codec()

print(c.decode(c.encode(["same", "as", "all"])))
