#Function to go through the scraped webpages and remove just the table and location
def callMe(data):
  idx1 = 0
  idx2 = 0
  idx3 = 0
  idx4 = 0
  output = open('output.txt', 'w')
  input = open(data, 'r')
  str = input.read()
  output.write('<!DOCTYPE HTML>')
  output.write('<html>')
  while(True):
    idx1 = str.find("<title>", idx4)
    idx2 = str.find("</title>", idx1)
    idx3 = str.find("<table", idx2)
    idx4 = str.find("</table>", idx3)
    if(idx1 < 0 or idx2 < 0 or idx3 < 0 or idx4 < 0):
      return
    output.write('<h2>')
    output.write(str[idx1+7:idx2-34].strip())
    output.write('</h2>')
    output.write('\n')
    output.write(str[idx3-2:idx4+8].strip())
    output.write('\n')
    output.write('\n')
    print idx1
    print idx2
    print idx3
    print idx4
    print ""
  output.write('</html>')
  output.close()
  input.close()
