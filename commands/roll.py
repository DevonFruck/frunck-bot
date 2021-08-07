from random import randint
import re

cmd_pattern = '/roll+\s+[\d]+d[\d]'

async def roll_cmd(input, sendMsg):
  if not re.search(cmd_pattern, input):
    await sendMsg('Improper use of command. /roll [# of die]d[# of faces]')
    return
          
  parsedText = input.split()
  rollParse = parsedText[1].split('d')
  
  rolls = []
  for num in range(0, int(rollParse[0])):
    rolls.append(randint(1, int(rollParse[1])))

  await sendMsg(rolls)