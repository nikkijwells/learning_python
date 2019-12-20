def order(sentence):
  n_list = sentence.split(" ")
  n_sentence = []
  finder = 1
  while finder < (len(n_list) - 1):
      for i in n_list:
          for x in i:
              if finder in i:
              n_sentence.append(i)
              finder = finder + 1
          #n_sentence = n_sentence + " " + i.find(finder)
          #return n_sentence

  #return n_list

print(order("is2 Thi1s T4est 3a"))
