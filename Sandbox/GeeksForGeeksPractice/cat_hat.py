def cat_hat(str):
  ##your code here##
  ##You need to write complete code this time 
  c=0
  h=0
  print(str)
  for s in range(len(str)):
      print(str[s:s+3])
      if str[s:s+3] == "cat":
          c += 1
          print(s)
      elif str[s:s+3] == "hat":
          h +=1
          print(s)
  if c == h:
      return("True")
  else:
      return("False")

print(cat_hat("czcckkhkhkkakzzkatkzzzkzatatzhztkzhzkcktczttzcchczkhkkcakakzkttcachchzthhckacakchkhathzzkhaacccczctc"))
