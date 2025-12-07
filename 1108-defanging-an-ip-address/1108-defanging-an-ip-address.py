class Solution:
    def defangIPaddr(self, address: str) -> str:
        newAdd = ""
        for i in address:
            if i == ".":
                newAdd += "[.]"
            else:
                newAdd += i
        return newAdd