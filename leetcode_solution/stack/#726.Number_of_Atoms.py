#  726. Number of Atoms (hard)
#  https://leetcode.com/problems/number-of-atoms/ 
#
class Solution:
    '''    
    trick: using stack, and when letters + number, generate a dict and insert into stack.
    
    e.g. formula = "K4(ON(SO3)2)2"
      i s[i] stack
      0  'K'  ['K']
      1  '4'  [{'K': 4}]
      2  '('  [{'K': 4}, '(']
      3  'O'  [{'K': 4}, '(', 'O']
      4  'N'  [{'K': 4}, '(', 'O', 'N']
      5  '('  [{'K': 4}, '(', 'O', 'N', '(']
      6  'S'  [{'K': 4}, '(', 'O', 'N', '(', 'S']
      7  'O'  [{'K': 4}, '(', 'O', 'N', '(', 'S', 'O']
      8  '3'  [{'K': 4}, '(', 'O', 'N', '(', 'S', {'O': 3}]
      9  ')2' [{'K': 4}, '(', 'O', 'N', {'O': 6, 'S': 2}]
     11  ')2' [{'K': 4}, {'O': 14, 'S': 4, 'N': 2}]

     => sorted by name: {'K':4, 'N': 2, 'O': 14, 'S': 4} => "K4N2O14S4"

    NOTE  corner cases: "(H)"", "Mg(H2O)N", where number after ")" = 1.
    '''
    def __init__(self):
        self.nums = set([str(i) for i in range(10)])
        
    def countOfAtoms(self, formula: str) -> str:
        
        stack = []
        i = 0
        while i <= len(formula) - 1:
            if formula[i] not in self.nums and formula[i] not in ("(", ")"):  # mean letters
                if formula[i].lower() != formula[i]: # [.., "O"] + "H" -> [.., "O", "H"]
                    stack.append(formula[i])
                else:
                    stack[-1] = stack[-1] + formula[i]  # [.., "B"] + "e" -> [.., "Be"]
                i += 1
            elif formula[i] in self.nums:
                j = self.get_number(i, formula)  # [.., "O"] + "3" + "2" -> [.., {"O": 32}]
                x = stack.pop()
                stack.append({x: int(formula[i:j])})
                i = j
            elif formula[i] == ")":
                               
                if i < len(formula)-1:           # get num after ")", e.g. num=2 for ")2" or num=1 for ")" 
                    j = self.get_number(i+1, formula)
                    num = int(formula[i+1:j]) if i+1 != j else 1
                    i = j
                else:
                    i += 1
                    num = 1
                
                counts = {}
                while len(stack) > 0 and stack[-1] != "(":
                    x = stack.pop()  # pop until meeting "(", and counts as {x: num}
                    if type(x) == str:
                        counts[x] = counts.get(x, 0) + 1
                    elif type(x) == dict:
                        for y in x:
                            counts[y] = counts.get(y, 0) + x[y]
                
                stack.pop()
                stack.append({x: counts[x]*num for x in counts}) 
            else:
                stack.append(formula[i])  # "("
                i += 1
        
        counts = {}
        while len(stack) > 0:
            x = stack.pop()
            if type(x) == str:
                counts[x] = counts.get(x, 0) + 1
            elif type(x) == dict:
                for y in x:
                    counts[y] = counts.get(y, 0) + x[y]
        
        ans = []
        for x in sorted(counts.keys()):
            if counts[x] == 1:
                ans.append(x)
            else:
                ans += [x+str(counts[x])]
        
        return "".join(ans)
    
    def get_number(self, j, formula):
        while j <= len(formula)-1 and formula[j] in self.nums:
            j += 1
        return j
