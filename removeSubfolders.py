class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folderSet = set(folder)
        res = []
        for i in range(len(folder)):
            res.append(folder[i])
            for j in range(len(folder[i])):
                if folder[i][j] == "/" and folder[i][:j] in folderSet:
                    res.pop()
                    break
        return res

    def removeSubfoldersN2(self, folder: list[str]) -> list[str]:
        folder.sort()
        res = []
        for i in range(len(folder)):
            if folder[i] == "":
                continue
            res.append(folder[i])
            for j in range(i + 1, len(folder)):
                pass
                if (
                    folder[j].startswith(folder[i])
                    and folder[i] != folder[j]
                    and folder[j][len(folder[i])] == "/"
                ):
                    folder[j] = ""
        return res


print(Solution().removeSubfolders(folder=["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))
print(Solution().removeSubfolders(folder=["/a", "/a/b/c", "/a/b/d"]))
print(Solution().removeSubfolders(folder=["/a/b/c", "/a/b/ca", "/a/b/d"]))
