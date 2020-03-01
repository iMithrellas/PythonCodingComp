a = []
for i in range(3):
  r = []
  for j in range(3):
    r.append(i+1)
  a.append(r)


  def printall(currentRow, currentColumn, nums):

    if ( currentRow == len(a) - 1):

        for i in range(currentColumn, len(a[0])):
            nums.append(a[currentRow][i])
        print nums
        return

    if (currentColumn == len(a[0]) - 1):

        for i in range(currentRow, len(a)):
            nums.append(a[i][currentColumn])
        print nums
        return

    nums.append(a[currentRow][currentColumn])
    printall(currentRow+1, currentColumn, nums[:])
    printall(currentRow, currentColumn+1, nums[:])

printall(0,0,[])
