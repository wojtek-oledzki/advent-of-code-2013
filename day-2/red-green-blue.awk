{
  b=g=r=1; 
  for (i = 2; i <= NF; i++) {
    split($i, a, " ")
    if (index($i, "red") != 0) {
      if (a[1] > r) {
        r = a[1]
      }
    } 
    if (index($i, "green") != 0) {
      if (a[1] > g) {
        g = a[1]
      }
    } 
    if (index($i, "blue") != 0) {
      if (a[1] > b) {
        b = a[1]
      }
    } 
  }
  print b*g*r
}
