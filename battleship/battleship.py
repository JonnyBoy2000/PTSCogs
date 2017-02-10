import discord
from discord.ext import commands
import random
import asyncio

class Battleship:
    """Play the old game called Battleship!"""

    def __init__(self, bot):
        self.bot = bot
        self.positions = [
        'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 
        'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 
        'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 
        'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 
        'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10',
        'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10',
        'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10',
        'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10',
        'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10',
        'J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'J10'
        ]

    @commands.command(pass_context=True, aliases=["seabattle"])
    async def battleship(self, ctx):
        """Play Battleship with the bot. I swear I won't cheat ;)"""
        status = await self.bot.say("Generating my sea...")
        botsea = []
        for i in range(10):
            position = random.choice(self.positions)
            while position in botsea:
                position = random.choice(self.positions)
            botsea.append(position)
        print(str(botsea)) # DEBUGGER
        await asyncio.sleep(1) # so it looks a bit legit like it's actually doing something.
        await self.bot.edit_message(status, "Generating your sea...")
        usersea = []
        for i in range(10):
            position = random.choice(self.positions)
            while position in usersea:
                position = random.choice(self.positions)
            usersea.append(position)
        await asyncio.sleep(1) # again, just so it looks legit like it's actually doing something.
        await self.bot.edit_message(status, "Your ships are located at: **{}**.\nStarting battle now. You can always say 'stop' to stop or 'help' for help.".format("**, **".join(usersea)))
        first = random.choice([False, True])
        if first:
            await self.bot.say("I'll go first.")
            while len(usersea) >= 0:
                bomb = random.choice(self.positions)
                if bomb in usersea:
                    usersea.remove(bomb)
                    await self.bot.say("I've hit one of your ships! I hit {}, you have **{}** left ({} ships). Your turn.".format(bomb, "**, **".join(usersea), len(usersea)))
                else:
                    await self.bot.say("I missed, your turn.")
                bomb = await self.bot.wait_for_message(author=ctx.message.author, timeout=30)
                if (bomb == None) or (bomb.content.upper() == "STOP"):
                    await self.bot.say("K then, I'll stop.")
                    break
                elif (bomb.content.upper() not in self.positions) or (bomb.content.upper() == "HELP"):
                    example = random.choice(self.positions)
                    await self.bot.say("In this game you have to bomb the bot's ship, "
                    "you can do this by saying {0} for example, this will bomb {0}."
                    " If there's a ship there that ship will be destroyed, if there's no ship there the bomb will explode in the water."
                    " So when it's your turn you'll just have to say A1, B5, G9, it goes all the way up to J10."
                    " And just so I have to code less, it's now the bot's turn.".format(example))
                elif bomb.content.upper() in botsea:
                    botsea.remove(bomb.content.upper())
                    if len(botsea) > 0:
                        await self.bot.say("You've hit one of my ships! I have {} ships left.".format(len(botsea)))
                    else:
                        await self.bot.say("You've hit my last ship! You win!")
                        break
                else:
                    await self.bot.say("You missed, my turn.")
        else:
            await self.bot.say("You'll go first.")
            while len(usersea) >= 0:
                bomb = await self.bot.wait_for_message(author=ctx.message.author, timeout=30)
                if (bomb == None) or (bomb.content.upper() == "STOP"):
                    await self.bot.say("K then, I'll stop.")
                    break
                elif (bomb.content.upper() not in self.positions) or (bomb.content.upper() == "HELP"):
                    example = random.choice(self.positions)
                    await self.bot.say("In this game you have to bomb the bot's ship, "
                    "you can do this by saying {0} for example, this will bomb {0}."
                    " If there's a ship there that ship will be destroyed, if there's no ship there the bomb will explode in the water."
                    " So when it's your turn you'll just have to say A1, B5, G9, it goes all the way up to J10."
                    " And just so I have to code less, it's now the bot's turn.".format(example))
                elif bomb.content.upper() in botsea:
                    botsea.remove(bomb.content.upper())
                    if len(botsea) > 0:
                        await self.bot.say("You've hit one of my ships! I have {} ships left.".format(len(botsea)))
                    else:
                        await self.bot.say("You've hit my last ship! You win!")
                        break
                else:
                    await self.bot.say("You missed, my turn.")
                bomb = random.choice(self.positions)
                if bomb in usersea:
                    usersea.remove(bomb)
                    await self.bot.say("I've hit one of your ships! I hit {}, you have **{}** left ({} ships). Your turn.".format(bomb, "**, **".join(usersea), len(usersea)))
                else:
                    await self.bot.say("I missed, your turn.")
            
def setup(bot):
    bot.add_cog(Battleship(bot))