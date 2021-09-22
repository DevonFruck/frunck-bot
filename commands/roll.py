from random import randint
import re

cmd_pattern = '\d+[d]\d+(\s[d]\d+)?$'

async def displayRolls(ctx, author, rolls, total):
  await ctx.send("`@%s` %s = **%s**" % (author, str(rolls).replace("'", ""), str(total)))

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

async def roll_cmd(input, author, ctx):
  print(input)
  if not re.search(cmd_pattern, input):
    await ctx.send('Improper use of command. /roll [# of die]d[# of faces]')
    return
  
  # Getting data from command arguments
  parsedText = input.split()
  rollParse = parsedText[0].split('d')
  numOfDropRolls = 0

  # Checking if there is an aditional argument
  if len(parsedText) >= 2:
    numOfDropRolls = int(parsedText[1].replace('d', ''))
  
  rolls = []
  for num in range(0, int(rollParse[0])):
    rolls.append(randint(1, int(rollParse[1])))
  
  # Determine lowest dice to drop (if applicable)
  rolls, total = await findLowestInt(rolls, numOfDropRolls)

  await displayRolls(ctx, author, rolls, total)
