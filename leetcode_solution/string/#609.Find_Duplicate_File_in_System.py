# [#609] Find Duplicate File in System
#
#   dropbox
#
class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        
        content_dict = {}
        
        for item in paths:
            item = item.split(" ")
            
            path = item[0]
            for file in item[1:]:
                file = file.split("(")
                fileName, content = file[0], file[1][:-1]
                if content not in content_dict:
                    content_dict[content] = [path+"/"+fileName]
                else:
                    content_dict[content].append(path+"/"+fileName)
                
        return [content_dict[x] for x in content_dict if len(content_dict[x]) > 1]
            