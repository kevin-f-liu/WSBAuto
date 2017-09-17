import numpy

# class Analyser():
#     def __init__(self, content):
#         self.page = content
#         self.words = []
#         self.wordCount = {}
#     def splitWords(self):
#         for p in self.page:
#             if type(p) is str:
#                 self.words.append(p.split())
#     def loadDictionary(self):
#         if len(self.wordCount > 0):
#             raise Exception("Dictionary not empty")
#         for word in words:
#             if word not in self.wordCount:
#                 self.wordCount[word] = 1
#             elif self.wordCount[word] > 1:
#                 self.wordCount[word] += 1
wordCount = {}
def loadDictionary(wwords):
    # if len(wordCount) > 0:
    #     raise Exception("Dictionary not empty")
    for word in wwords:
        if word not in wordCount:
            wordCount[word] = 1
        elif int(wordCount.get(word)) > 1:
            wordCount[word] += 1

# Main
with open('results_DATA.txt') as fin:
    data = fin.readlines()
    data = [d.strip() for d in data]
rawData = []
[rawData.append(d) for d in data if not d.startswith('http')]
rawData = [r[1:len(r)-1] for r in rawData]
# for r in rawData:
#     print(r)
messyWords = []
for rd in rawData:
    messyWords.append([s.split() for s in rd.split('\', \'')])
words = []
[words.append(w) for w in messyWords if len(w) > 0]
for a in words:
    for s in a:
        loadDictionary(s)


print(wordCount)