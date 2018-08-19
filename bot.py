# This bot requires no permissions in order to work besides being able to read and write in whatever channel it's left in
import discord
from discord.ext import commands
import os
import asyncio
import requests
from bs4 import BeautifulSoup

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    game = discord.Game("Assisting the RHPD")
    await bot.change_presence(status=discord.Status.online, activity=game)

	
# Greet new users and provide helpful information	
@bot.event
async def on_member_join(member):
    print('User Joined')
    embed = discord.Embed(title="__Welcome to the Rockford Hills Police Department Discord!__", description="_Here are a few tips & tricks to get you started!_", color=0x3D59AB)
	
    embed.set_author(name="Rockford Hills Police Info Bot", icon_url="http://www.beverlyhills.org/cbhfiles/storage/files/filebank_images/images/Police%20Department/BHPDLogo2.jpg")
	
    embed.add_field(name="Signing In", value="Make sure you head over to the #headquarters-lobby channel in order to be granted your tags.", inline=False)
    embed.add_field(name="Questions?", value="If at any point you have any other questions please check our !faq or ask around, I am sure anyone would be willing to help!", inline=False)
    embed.add_field(name="Bot Help", value="Please contact brandon#9658 (Patrol Officer Johnson,) if you need any assistance with the bot and using !help, !faq and !cmds doesn't get you to where you need to be, thanks!", inline=False)
	
    
    await member.send(embed=embed)


@bot.command()
async def embe(ctx,ar,arg,arg2,arg3,arg4):
    user_inpt = arg  
    user_inpt2 = arg2
    user_inpt3 = arg3
    user_inpt4 = arg4
    embed = discord.Embed(title="".join(user_inpt), description="".join(user_inpt2), color=0x3D59AB)
	
    embed.set_author(name="{}".format(ar), icon_url="http://www.beverlyhills.org/cbhfiles/storage/files/filebank_images/images/Police%20Department/BHPDLogo2.jpg")
	
    embed.add_field(name="".join(user_inpt3), value="[Click Here]({})".format(user_inpt4), inline=False)
 
    await ctx.send(embed=embed)
    await asyncio.sleep(2) 
    await ctx.message.delete()

@bot.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)

@bot.command()
async def status(ctx):
    web = requests.get('http://status.highspeed-gaming.com/')
    soup = BeautifulSoup(web.content, 'html.parser')
    empserver = "No players currently online."
    players1 = []
    playerss2 = []
    for element in soup.find_all("dd", id="accordion1"):
      for stat in element.find_all("tr", attrs={"width":True}):
        for players in stat.find_all("td")[1]:
          players1.append(players)
    if not players1:
      players1.append(empserver)


    for element2 in soup.find_all("dd", id="accordion2"):
      for stat2 in element2.find_all("tr", attrs={"width":True}):
        for players2 in stat2.find_all("td")[1]:
          playerss2.append(players2)
    if not playerss2:
      playerss2.append(empserver)
    
    servers = []
    for p in soup.find_all('a'):
      servers.append(p.text)
    embed = discord.Embed(title="__Highspeed-Gaming Status__", description=("Current Status of HSG Servers"), color=0x3D59AB)
    embed.set_author(name="Rockford Hills Police Info Bot", icon_url="http://www.beverlyhills.org/cbhfiles/storage/files/filebank_images/images/Police%20Department/BHPDLogo2.jpg")
    embed.add_field(name="Server 1", value=servers[0], inline=False)
    embed.add_field(name="S1 - Players", value=', '.join(players1), inline=False)

    embed.add_field(name="Server 2", value=servers[1], inline=False)
    embed.add_field(name="S2 - Players", value=', '.join(playerss2), inline=False)

    embed.add_field(name="Disclaimer", value="If it shows both servers as empty, it's most likely wrong. Blame status.highspeed-gaming.com", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def searchpc(ctx, *, arg):
    temporary = """1.01 Inadmissible Defences	| 	N/A	| 	N/A
1.02 Admissible Defences	| 	N/A	| 	N/A
1.03 Persons Liable to Punishment	| 	N/A	| 	N/A	| 	
2.01 Principals and Accessories	| 	N/A	| 	N/A
2.02 Principles to a Crime	| 	N/A	| 	N/A
2.03 Accessories to a Crime	| 	N/A	| 	N/A	| 	
3.01 Bribery	| 	Misdemeanor	| 	Up to 3 Minutes
3.02 Felony Bribery	| 	Felony	| 	From 5 to 10 Minutes
3.03 Reception of a Bribe	| 	Misdemeanor	| 	Up to 3 Minutes
3.04 Felony Reception of a Bribe	| 	Felony	| 	From 5 to 10 Minutes
3.05 Obstruction of a Public Official	| 	Misdemeanor	| 	Up to 3 Minutes
3.06 Aggravated Obstruction of a Public Official	| 	Felony	| 	Up to 10 Minutes	| 	
4.01 Rescue	| 	Misdemeanor	| 	Up to 5 Minutes
4.02 Escape	| 	Felony	| 	From 5 to 10 Minutes
4.03 Aiding Escape	| 	Felony	| 	From 5 to 10 Minutes
4.04 Resisting Arrest	| 	Misdemeanor	| 	Up to 3 Minutes
4.05 Failure to Identify	| 	Misdemeanor	| 	10 Minutes
4.06 Obstruction of a Government Employee	| 	Misdemeanor	| 	Up to 3 Minutes
4.07 Misuse of a Government Hotline	| 	Infraction/Misdemeanor	| 	Up to 2 Minutes
4.08 Tampering With Evidence	| 	Misdemeanor	| 	Up to 5 Minutes
4.09 Forgery of Public Record	| 	Misdemeanor	| 	Up to 3 Minutes
4.10 Perjury	| 	Felony	| 	From 8 to 15 Minutes
4.11 Falsification of Evidence	| 	Felony	| 	From 5 to 10 Minutes
4.12 Dissuading a Witness	| 	Misdemeanor	| 	Up to 5 Minutes
4.13 Evading	| 	Misdemeanor	| 	Up to 5 Minutes
4.14 Felony Reckless Evading	| 	Felony	| 	From 8 to 15 Minutes
4.15 Refusal to Sign	| 	Misdemeanor	| 	From 5 to 15 Minutes
4.16 Failure to Pay Fine	| 	Misdemeanor	| 	From 5 to 15 Minutes
4.17 Contempt of Court	| 	Misdemeanor	| 	Up to 10 Minutes
4.18 Provision of False Information to A State Employee	| 	Misdemeanor	| 	Up to 5 Minutes
4.19 False Complaint	| 	Misdemeanor	| 	Up to 5 Minutes
4.20 Human Trafficking	| 	Felony	| 	From 8 to 15 Minutes
4.21 Violation of Parole or Probation	| 	Misdemeanor	| 	Up to 10 Minutes
4.22 False Personation	| 	Felony	| 	Up to 5 Minutes
4.23 Peace Officer Refusing to Arrest	| 	Felony	| 	Up to 5 Minutes
4.24 False Report of Crime or Emergency	| 	Felony	| 	Up to 10 Minutes
4.25 Street Gang Membership	| 	Felony	| 	From 8 to 15 Minutes	| 	
5.01 Intimidation	| 	Misdemeanor	| 	Up to 5 Minutes
5.02 Assault	| 	Misdemeanor	| 	Up to 5 Minutes
5.03 Assault With a Deadly Weapon	| 	Misdemeanor/Felony	| 	Up to 5 Minutes/From 5 to 10 Minutes
5.04 Mutual Combat	| 	Misdemeanor	| 	Up to 5 Minutes
5.05 Battery	| 	Misdemeanor	| 	Up to 5 Minutes
5.06 Aggravated Battery	| 	Misdemeanor	| 	Up to 10 Minutes
5.07 Attempted Murder	| 	Felony	| 	From 8 to 15 Minutes
5.08 Manslaughter	| 	Felony	| 	From 8 to 15 Minutes
5.09 Murder	| 	Felony	| 	From 8 to 15 Minutes
5.10 False Imprisonment	| 	Misdemeanor	| 	Up to 5 Minutes
5.11 Kidnapping	| 	Felony	| 	From 8 to 18 Minutes
5.12 Mayhem	| 	Felony	| 	From 8 to 15 Minutes
5.13 Hate Crime	| 	Felony	| 	From 8 to 15 Minutes
5.14 Hostage Taking	| 	Felony	| 	From 8 to 15 Minutes	| 		| 	
6.01 Indecent Exposure	| 	Misdemeanor	| 	Up to 5 Minutes
6.02 Obscene Exhibition	| 	Misdemeanor	| 	Up to 5 Minutes
6.03 Bawdy or Disorderly House	| 	Misdemeanor	| 	Up to 5 Minutes
6.04 Prostitution	| 	Misdemeanor	| 	Up to 5 Minutes
6.05 Solicitation	| 	Misdemeanor	| 	Up to 5 Minutes
6.06 Pandering	| 	Misdemeanor	| 	Up to 5 Minutes
6.07 Sexual Assault	| 	Misdemeanor	| 	Up to 5 Minutes
6.08 Sexual Battery	| 	Misdemeanor	| 	Up to 10 Minutes
6.09 Rape	| 	Felony	| 	From 8 to 15 Minutes
6.10 Stalking	| 	Misdemeanor	| 	Up to 5 Minutes
6.11 Disorderly Conduct	| 	Misdemeanor	| 	Up to 5 Minutes
7.01 Possession of a Controlled Substance	| 	Misdemeanor	| 	Up to 5 Minutes
7.02 Possession of a Controlled Substance with Intent to Distribute	| 	Felony	| 	From 5 to 10 Minutes
7.03 Possession of Drug Paraphernalia	| 	Misdemeanor	| 	Up to 3 Minutes
7.04 Maintaining a Place for Purpose of Distribution	| 	Felony	| 	From 5 to 10 Minutes
7.05 Manufacture of a Controlled Substance	| 	Felony	| 	From 5 to 15 Minutes
7.06 Sale of a Controlled Substance	| 	Felony	| 	From 5 to 10 Minutes
7.07 Possession of an Open Container	| 	Infraction	| 	N/A
7.08 Public Intoxication	| 	Misdemeanor	| 	Up to 5 Minutes
7.09 Public Influence of a Controlled Substance	| 	Misdemeanor	| 	Up to 5 Minutes
7.10 Possession in Excess	| 	Misdemeanor	| 	Up to 5 Minutes
7.11 Criminal Threats	| 	Misdemeanor	| 	Up to 5 Minutes
7.12 Reckless Endangerment	| 	Misdemeanor	| 	Up to 5 Minutes
7.13 Trafficking of a Controlled Substance	| 	Felony	| 	From 5 to 10 Minutes	| 	
8.01 Obstruction of Assembly	| 	Misdemeanor	| 	Up to 5 Minutes
8.02 Riot	| 	Misdemeanor	| 	Up to 10 Minutes
8.03 Incitement to Riot	| 	Misdemeanor	| 	Up to 5 Minutes
8.04 Unlawful Assembly	| 	Misdemeanor	| 	Up to 5 Minutes
8.05 Breach of the Peace	| 	Misdemeanor	| 	Up to 5 Minutes
8.06 Obstruction of Rightful Passage	| 	Misdemeanor	| 	Up to 5 Minutes
9.01 Arson	| 	Felony	| 	From 8 to 15 Minutes
9.02 Burglary	| 	Felony	| 	From 8 to 15 Minutes
9.03 Possession of Burglary Tools	| 	Misdemeanor	| 	Up to 5 Minutes
9.04 Forgery	| 	Misdemeanor/Felony	| 	Up to 5 Minutes/From 5 to 10 Minutes
9.05 Petty Theft	| 	Misdemeanor	| 	Up to 10 Minutes
9.06 Grand Theft	| 	Felony	| 	From 5 to 15 Minutes
9.07 Embezzlement	| 	Misdemeanor/Felony	| 	Up to 10 Minutes/From 5 to 15 Minutes
9.08 Trespassing	| 	Misdemeanor	| 	Up to 5 Minutes
9.09 Robbery	| 	Felony	| 	From 5 to 15 Minutes
9.10 Armed Robbery	| 	Felony	| 	From 8 to 15 Minutes
9.11 Receiving Stolen Property	| 	Misdemeanor/Felony	| 	Up to 5 Minutes/From 5 to 10 Minutes
9.12 Vandalism	| 	Misdemeanor	| 	Up to 5 Minutes
9.13 Criminal Damage	| 	Misdemeanor	| 	Up to 5 Minutes
9.14 Grand Larceny	| 	Felony	| 	From 5 to 15 Minutes	| 	
10.01 Hate Crime	| 	Misdemeanor/Felony	| 	Up to 10 Minutes	| 		| 	
11.01 Extortion	| 	Felony	| 	From 5 to 10 Minutes
11.02 Money Laundering	| 	Felony	| 	From 5 to 10 Minutes	| 	
12.01 Unlawful Possession of a Firearm	| 	Felony 	| 	From 5 to 10 Minutes
12.02 Unlawful Concealment of a Firearm	| 	Misdemeanor/Felony	| 	Up to 5 Minutes/From 5 to 10 Minutes
12.03 Unlawful Carry of a Firearm	| 	Misdemeanor/Felony	| 	Up to 5 Minutes/From 5 to 10 Minutes
12.04 Unlawful Display of a Firearm	| 	Misdemeanor/Felony	| 	Up to 5 Minutes/From 5 to 10 Minutes
12.05 Unlawful Discharge of a Firearm	| 	Misdemeanor/Felony	| 	Up to 5 Minutes/From 5 to 10 Minutes
12.06 Unlawful Possession of a Deadly Weapon	| 	Misdemeanor/Felony	| 	Up to 5 Minutes/From 5 to 10 Minutes
12.07 Unlawful Display of a Deadly Weapon	| 	Misdemeanor/Felony	| 	Up to 5 Minutes/From 5 to 10 Minutes
12.08 Unlawful Concealment of a Deadly Weapon	| 	Misdemeanor/Felony	| 	Up to 5 Minutes/From 5 to 10 Minutes
12.09 Unlawful Possession of An Explosive Device	| 	Felony	| 	From 5 to 15 Minutes
12.10 Manufacture of an Explosive Device	| 	Felony	| 	From 8 to 15 Minutes
12.11 Unlawful Distribution of a Firearm	| 	Misdemeanor/Felony	| 	Up to 10 Minutes/From 8 to 15 Minutes
12.12 Unlawful Possession of Firearms with Intent to Sell	| 	Felony	| 	From 5 to 15 Minutes.
12.13 Unlawful Modification of a Firearm	| 	Misdemeanor/Felony	| 	Up to 5 Minutes/From 5 to 10 Minutes"""
    us_inpt = arg  
    err = "Nothing has been found based on your input"
    found_list = []

	
    for line in temporary.splitlines():
      if us_inpt.lower() in line.lower():
        found_list.append(line)

    if len(found_list) == 0:
    	await ctx.send(err)

    embed = discord.Embed(title="__San Andreas Penal Code Lookup__", description=("It looks like you searched for "+us_inpt.title()), color=0x3D59AB)
    embed.set_author(name="Rockford Hills Police Info Bot", icon_url="http://www.beverlyhills.org/cbhfiles/storage/files/filebank_images/images/Police%20Department/BHPDLogo2.jpg")
    embed.add_field(name="Here's what we found based on your search:", value='\n'.join(found_list), inline=False)
    embed23 = await ctx.send(embed=embed)
    await asyncio.sleep(10) 
    await ctx.message.delete()

	
@bot.command()
async def searchvc(ctx, *, arg):
    temporary = """13.01 Reckless Driving  |   Misdemeanor/Infraction  |   Up to 3 Minutes / 150$ Fine / Both
13.01(b) Reckless Driving Causing Bodily Injury |   Felony  |   p to 5 Minutes / 150$ Fine / Both
13.02 Eluding / Evading a Peace Officer |   Misdemeanor/Infraction  |   Up to 3 Minutes / 150$ Fine / Both
13.03 Hit and Run   |   Misdemeanor/Infraction  |   Up to 3 Minutes / 150$ Fine
13.03(b) Hit and Run With Injury    |   Felony  |   Up to 6 Minutes / 150$ Fine / Both
13.04 Failure to Yield to a TCD |   Infraction  |   150$ Fine
13.05 Speeding  |   Infraction  |   150$ Fine
13.06 Driving Wrong Way |   Infraction  |   150$ Fine
13.07 Illegal Window Tint   |   Infraction  |   100$ Fine
13.08 Failure to Maintain Lane  |   Infraction  |   150$ Fine
13.09 Impeding Traffic  |   Infraction  |   150$ Fine
13.10 Open Alcohol Container    |   Infraction  |   150$ Fine
13.10(b) Open Alcohol Container Under 21    |   Misdemeanor/Infraction  |   Up to 5 Minutes / 150$ Fine / Both
13.10(c) Driving in Possession of Marijuana |   Infraction  |   100$ Fine
13.11 Exhibition of Speed   |   Infraction  |   150$ Fine
13.12 Illegal Vehicle Modifications |   Infraction  |   150$ Fine
13.13 Operating an Unroadworthy Vehicle |   Infraction  |   150$ Fine
13.14 Failure to display License Plate  |   Infraction  |   150$ Fine
13.15 Failure to Yield to Emergency Vehicle(s)  |   Misdemeanor/Infraction  |   Up to 5 Minutes / 150$ Fine / Both
13.16 Unsafe Vehicle Load   |   Infraction  |   150$ Fine
13.17 Driving on Sidewalk   |   Infraction  |   100$ Fine
13.18 Interfering with Driver's Control of Vehicle  |   Misdemeanor/Infraction  |   Up to 2 Minutes / 150$ Fine
13.19 Following too Closely |   Infraction  |   150$ Fine
13.20 Motorcycles: Lane Splitting   |   Infraction  |   150$ Fine
13.21 Illegal Passing   |   Infraction  |   150$ Fine
13.22 Unsafe Operation of Emergency Vehicle    
13.23 Driving Without Headlights at Night   |   Infraction  |   150$ Fine
13.24 Failure to Dim Lights |   Infraction  150$ Fine
13.25 Driving Without a Valid License   |   Misdemeanor/Infraction  |   Up to 5 Minutes / 150$ Fine / Both
13.26 Failure to Show a Driver's License    |   Infraction  |   150$ Fine
13.27 Illegal Parking      
13.28 Driving Under the Influence of Alcohol    |   Misdemeanor |   Up to 6 Minutes / 150$ Fine
13.28(b) Driving Under the Influence of Drugs   |   Misdemeanor |   Up to 6 Minutes / 150$ Fine
13.29 Broken Tail Light / Headlights    |   Infraction  |   100$ Fine
13.30 Jaywalking    |   Infraction  |   100$ Fine
13.31 Possession of Sirens & Emergency Lighting |   Infraction  |   150$ Fine
13.31(b) Possession of Sirens & Emergency Lighting With Intent to Impersonate   |   Misdemeanor |   Up to 6 Minutes / 150$ Fine
13.32 Failure to Wear Motorcycle Helmet |   Infraction  |   150$ Fine
13.33 Hitchhiking   |   Infraction  100$ Fine
13.34 Driving with a Suspended License  |   Misdemeanor |   Up to 5 Minutes / 150 Fine
13.35 Failure to Signal Lane Change |   Infraction  |   100$ Fine
13.36 Use of Hydraulics on Public Roads |   Infraction  |   100$ Fine
13.37 Intentionally Altering or Destroying a VIN    |   Misdemeanor/Infraction  |   Up to 5 Minutes / 150$ Fine / Both
13.38 Buying or Possessing a Vehicle with an Altered VIN    |   Misdemeanor/Infraction  |   Up to 5 Minutes / 150$ Fine / Both
13.39 Felony Speeding   |   Felony  |   Up to 5 Minutes"""
    us_inpt = arg  
    err = "Nothing has been found based on your input"
    found_list = []

    for line in temporary.splitlines():
      if us_inpt.lower() in line.lower():
        found_list.append(line)	 
	
    if len(found_list) == 0:
    	await ctx.send(err)

    embed = discord.Embed(title="__San Andreas Vehicle Code Lookup__", description=("It looks like you searched for "+us_inpt.title()), color=0x3D59AB)
    embed.set_author(name="Rockford Hills Police Info Bot", icon_url="http://www.beverlyhills.org/cbhfiles/storage/files/filebank_images/images/Police%20Department/BHPDLogo2.jpg")
    embed.add_field(name="Here's what we found based on your search:", value='\n'.join(found_list), inline=False)
    await ctx.send(embed=embed)
    await asyncio.sleep(10) 
    await ctx.message.delete()
   
	
	
	
	
# This command prints out info about the bot itself
@bot.command()
async def info(ctx):
    embed = discord.Embed(title="__Rockford Hills Police Information Bot__", description="_Used to convey information about HighSpeed-Gaming's Rockford Hills Police_", color=0x3D59AB)
	
    embed.set_author(name="Rockford Hills Police Info Bot", icon_url="http://www.beverlyhills.org/cbhfiles/storage/files/filebank_images/images/Police%20Department/BHPDLogo2.jpg")

    embed.add_field(name="Author", value="Patrol Officer David Johnson (brandon#9648)")
    embed.add_field(name="Suggestions", value ="DM brandon#9648 to make suggestions about the future of the bot.")
    embed.add_field(name="Disclaimer", value="If the bot stops working an update is being pushed to it or I broke something.")
    embed.set_footer(text="'neat, i made a bot to incentivize lazyness' - brandon")


    await ctx.send(embed=embed)

	
	
	
	
# This command removes the default help command
bot.remove_command('help')

# This command is the reworked help command once the default one is removed
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="__Help Box__", description="_You appear to need help, let me get you started._", color=0x3D59AB)
	
    embed.set_author(name="Rockford Hills Police Info Bot", icon_url="http://www.beverlyhills.org/cbhfiles/storage/files/filebank_images/images/Police%20Department/BHPDLogo2.jpg")
	
    embed.add_field(name="!cmds", value="Type this command in chat to get started, this should get you where you need to go.", inline=False)
	
    await ctx.send(embed=embed)

	
# This command lists the base of commands for users to utilize
@bot.command()
async def cmds(ctx):
    embed = discord.Embed(title="__Rockford Hills Police Information Bot__", description="_List of commands are:_", color=0x3D59AB)
	
    embed.set_author(name="Rockford Hills Police Info Bot", icon_url="http://www.beverlyhills.org/cbhfiles/storage/files/filebank_images/images/Police%20Department/BHPDLogo2.jpg")

    embed.add_field(name="!searchpc", value="Allows a user to search through the list of Penal Codes", inline=False)
    embed.add_field(name="!searchvc", value="Allows a user to search through the list of Vehicle Codes", inline=False)	
    embed.add_field(name="!divisions", value="Gives information about the various divisions of the Rockford Hills Police", inline=False)
    embed.add_field(name="!faq", value="Gives a list of info about Frequently Asked Questions", inline=False)
    embed.add_field(name="!status", value="Gives status of all HighSpeed-Gaming servers and their playercount", inline=False)
    embed.add_field(name="!info", value="Gives information about the bot", inline=False)
    embed.add_field(name="!cmds", value="Gives a message containing important commands for the bot", inline=False)

    await ctx.send(embed=embed)
	
# This command lists the base of commands for users to utilize
@bot.command()
async def divisions(ctx):
    embed = discord.Embed(title="__Rockford Hills Police Information Bot__", description="_List of commands are:_", color=0x3D59AB)
	
    embed.set_author(name="Rockford Hills Police Info Bot", icon_url="http://www.beverlyhills.org/cbhfiles/storage/files/filebank_images/images/Police%20Department/BHPDLogo2.jpg")

    embed.add_field(name="Field Services Division," value="Run by Commander Rocknik, containing the Patrol, Traffic, Emergency Services and Community Relations sections", inline=False)
    embed.add_field(name="Investigative Services Division," value="Run by N/A, containing the Detective, Identification, Crime Analysis, and Intelligence sections", inline=False)
    embed.add_field(name="Administrative Services Division," value="Run by N/A, containing the Records, Communications, Jail, Property & Evidence, Personnel Training, Special Projects, and Professional Standards sections", inline=False)

    await ctx.send(embed=embed)


	
	
	
# This command is to show answers to FAQ
@bot.command()
async def faq(ctx):
    embed = discord.Embed(title="__Frequently Asked Questions__", description="_Answers and links to FAQ:_", color=0x3D59AB)
	
    embed.set_author(name="Rockford Hills Police Info Bot", icon_url="http://www.beverlyhills.org/cbhfiles/storage/files/filebank_images/images/Police%20Department/BHPDLogo2.jpg")
	
    embed.add_field(name="I want to report someone", value="Contact your Shift Supervisor, if they can't help, go to one of the Sergeants or above", inline=False)
    embed.add_field(name="What is my Call Sign?/What is my Patrol Zone?", value="Contact your Shift/Division Supervisor and utilize the #radio-frequencies channel.", inline=False)
    embed.add_field(name="Who is my Supervisor?", value="Utilize the #radio-frequencies channel to learn the rank hierarchy and then search for the Supervisor with the corresponding call-signs", inline=False)
    embed.add_field(name="How do I communicate with other officers?", value="Utilize the #radio-frequencies to understand the communication channel hierarchy and utilize it for inter-department communication.", inline=False)	
	
    await ctx.send(embed=embed)
	

	
	
	

bot.run(os.environ.get('TOKEN'))
