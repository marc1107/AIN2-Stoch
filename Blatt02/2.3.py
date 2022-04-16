allCombos = 10*10*10*10
noZeroBegin = allCombos-(1*10*10*10)

print("2.3.1:")
print("a)", allCombos)
print("b)", noZeroBegin)
print("\n2.3.2")
print("a)", (1/allCombos) + ((allCombos-1)/allCombos) * (1/allCombos) + ((allCombos-1)/allCombos)
      * ((allCombos-1)/allCombos) * (1/allCombos))
print("b)", (1/noZeroBegin) + ((noZeroBegin-1)/noZeroBegin) * (1/noZeroBegin) + ((noZeroBegin-1)/noZeroBegin)
      * ((noZeroBegin-1)/noZeroBegin) * (1/noZeroBegin))