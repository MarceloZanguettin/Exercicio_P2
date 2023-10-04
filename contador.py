with open("center_earth.txt", "r") as arquivo:
	wordstring = arquivo.read()
wordstring = wordstring.lower()

with open("gutenberg.txt", "r") as arquivo2:
      wordstring2 = arquivo2.read()
wordstring2 = wordstring2.lower()

wordstring += wordstring2

wordlist = wordstring.split()
wordfreq = []
wordquantidade = 0
for w in wordlist:
    wordfreq.append(wordlist.count(w))
    wordquantidade = wordquantidade + wordlist.count(w)

print("A quantidade total de palavras nos dois arquivos é de: " + str(wordquantidade) + " palavras.")
print("Pares\n" + str(list(zip(wordlist, wordfreq))))