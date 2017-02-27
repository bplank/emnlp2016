from bllipparser import Tree
from collections import defaultdict
import gzip, sys

if __name__ == '__main__':
  if len(sys.argv) != 3:
    print('usage: python create_vocab.py train.gz count')
    sys.exit(0)

  threshold = int(sys.argv[2])
  counts = defaultdict(int)
  for line in gzip.open(sys.argv[1], 'rb'):
    line=line.strip().decode("utf-8")
    #print(">>{}<<".format(line))
    for word in Tree(line).tokens():
      counts[word.lower()] += 1

  for w, c in list(counts.items()):
    if c > threshold:
      print(w)
