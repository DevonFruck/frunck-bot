from random import randint
import re

cmd_pattern = '^/roll\s\d+[d]\d+(\s[d]\d+)?$'

async def displayRolls(sendMsg, author, rolls, total):
  #await sendMsg("@{}".format(author) + str(rolls).replace("'", "") + " = " + "**{}**".format(str(total)))
  await sendMsg("`@%s` %s = **%s**" % (author, str(rolls).replace("'", ""), str(total)))

async def findLowestInt(list, numOfDrops):
  for x in range(0, numOfDrops):
    lowestIndex = None

    for index in range(0, len(list)):
      if not isinstance(list[index], int):
        continue

      if lowestIndex == None:
        lowestIndex = index
        continue
      
      if list[lowestIndex] > list[index]:
        lowestIndex = index

    list[lowestIndex] = "||{}||".format(list[lowestIndex])
  
  total = 0
  for elem in list:
    if isinstance(elem, int):
      total += elem

  return list, total

async def roll_cmd(input, author, sendMsg):
  if not re.search(cmd_pattern, input):
    await sendMsg('Improper use of command. /roll [# of die]d[# of faces]')
    return
  
  # Getting data from command arguments
  parsedText = input.split()
  rollParse = parsedText[1].split('d')
  numOfDropRolls = 0
  if len(parsedText) >= 3:
    numOfDropRolls = int(parsedText[2].replace('d', ''))
  
  rolls = []
  for num in range(0, int(rollParse[0])):
    rolls.append(randint(1, int(rollParse[1])))
  
  #Determine lowest dice to drop (if applicable)
  rolls, total = await findLowestInt(rolls, numOfDropRolls)

  await displayRolls(sendMsg, author, rolls, total)
