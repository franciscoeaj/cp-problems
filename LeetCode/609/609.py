class Solution:
  def findDuplicate(self, paths: list[str]) -> list[list[str]]:
    contentsMap = {}

    for path in paths:
      splitPath = path.split()
      rootDir, paths = splitPath[0], splitPath[1:]

      for filePath in paths:
        splitFile = filePath.split("(")
        fileContent = splitFile[1][:-1]

        fullPath = "%s/%s" % (rootDir, splitFile[0])
        if fileContent not in contentsMap:
          contentsMap[fileContent] = [fullPath]
        else:
          contentsMap[fileContent].append(fullPath)
        
    ans = []
    for files in contentsMap.values():
      if len(files) > 1:
        ans.append(files)

    return ans

paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
sol = Solution()
print(sol.findDuplicate(paths))