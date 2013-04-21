#Function to turn regular text with line breaks and paragraphs
# into html filled text (with line breaks and paragraphs).
def htmlify(s):
  length = len(s)
  idx = 0
  output = '<p>'
  lastBr = False
  while(idx < length-1):
    #print idx
    if(lastBr and s[idx] == ' '):
      lastBr = False
    elif(s[idx] == '\n'):
      if(s[idx + 1] == '\n'):
        output += '</p>\n<p>'
        lastBr = True
        idx += 1
      else:
        output += '</br>'
        lastBr = True
    else:
      output += s[idx]
      lastBr = False
    idx += 1
    #print output
  output += '</p>'
  return output

#Call this function
def callMe(s):
  f = open(s, 'r')
  a = htmlify(f.read())
  g = open('output.txt', 'w')
  g.write(a)
