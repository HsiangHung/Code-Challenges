# [#648] Replace Words
#
# Uber
#
class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        sentence = sentence.split(" ")
        min_dict = min([len(word) for word in dict])
        
        sent_dict = {}
        for word in set(sentence):
            if len(word) >= min_dict:
                for root in dict:
                    if root == word[:len(root)]:
                        if (word not in sent_dict) or (word in sent_dict and len(root) < len(sent_dict[word])):
                            sent_dict[word] = root
                        
        for i in range(len(sentence)):
            if sentence[i] in sent_dict:
                sentence[i] = sent_dict[sentence[i]]
        
        return ' '.join(sentence)
                        