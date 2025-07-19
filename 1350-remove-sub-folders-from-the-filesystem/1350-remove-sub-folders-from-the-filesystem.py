class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        l=list()
        se=set()
        folder.sort(key=lambda x :len(x))
        for i in folder:
            s=""
            flag=True
            temp = (i.split('/'))
            for j in temp[1:]:
                s+=j+'.'
                if s in se:
                    flag=False
                    break
            if flag:
                l.append(i)
                se.add(s)
            # print(se)
        return l