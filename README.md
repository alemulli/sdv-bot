# StardewSavant

StardewSavant is an extended version of StardewSavvy, a Stardew Valley Discord bot that helps you quickly access info while you play.

[Invite the bot to your server here](https://discord.com/oauth2/authorize?client_id=1404203614347464805&permissions=117760&integration_type=0&scope=bot)

## Commands

### Gift Command

Use `!gift [villager name]` (i.e. `!gift Leah`) to get a list of that villager’s loved and liked gifts.

<img width="624" height="716" alt="image" src="https://github.com/user-attachments/assets/b340de8e-5b93-4461-ac2d-0ec5a35fb9a0" />

### Character Command

Use `!char [villager name]` (i.e. `!char Leah`) to get a villager’s profile, including their birthday and a picture, and a link to the Stardew Valley Wiki for their schedule.

<img width="324" height="159" alt="image" src="https://github.com/user-attachments/assets/7cd5fb17-c73b-417a-98c4-348260ee0499" />

### Build Command

Use `!build [farm building]` (i.e. `!build Big Barn`) to see the cost and materials needed to build that farm building.

<img width="341" height="214" alt="image" src="https://github.com/user-attachments/assets/d31c5e15-e61f-4dfc-9057-88d8de75ac18" />

### Upgrade Command

Use `!upgrade [tool]` (i.e. `!upgrade Iridium Pickaxe`) to see the cost and materials needed to upgrade a tool.

<img width="338" height="159" alt="image" src="https://github.com/user-attachments/assets/f67f20d8-945d-4de4-ba77-e4bea85e6498" />

### Events Command

Use `!events [spring|summer|fall|winter]` (i.e. `!events winter`) to see the events and birthdays for the season.

<img width="328" height="462" alt="image" src="https://github.com/user-attachments/assets/acd179c3-d24b-4eea-b4ed-2b9e31fbe2b4" />

Use `!events [spring|summer|fall|winter] [Day]` (i.e. `!events winter 3`) to get a list of events and birthdays occurring on a specific day.

<img width="300" height="133" alt="image" src="https://github.com/user-attachments/assets/882da788-553f-489c-961a-87a966ff063b" />

### Bundle Command

Use `!bundle` to show a list of all items needed for the Community Center.
Use `!bundle incomplete` to show a list of only the incompleted Community Center bundles for your server.
Use `!bundle find [item]` (i.e. `!bundle find Daffodil`) to check if an item belongs to a bundle in the Community Center and which bundle(s) use that item.

<img width="393" height="86" alt="image" src="https://github.com/user-attachments/assets/b8fcf89e-8b3c-4000-b0bc-4fdb26633eaa" />

Use `!bundle [bundle room]` (i.e. `!bundle Pantry`) to show a list of all items needed for the bundles in a specific room in the Community Center.

<img width="281" height="751" alt="image" src="https://github.com/user-attachments/assets/44ca88df-298d-48b1-b455-f65963b29aa6" />

Use `!bundle [bundle name]` (i.e. `!bundle Chef's Bundle`) to show a list of all items needed for a specific bundle in the Community Center.

<img width="438" height="372" alt="image" src="https://github.com/user-attachments/assets/23fe1945-0d07-42bc-82a4-8c58be92976f" />

Use `!bundle check "[bundle name]" [item]` to mark an item as completed in a bundle (i.e. `!bundle check "Chef's Bundle" Poppy`).
Use `!bundle uncheck "[bundle name]" [itme]` to similarly unmark an item as completed in a bundle if it was marked by mistake.
Use `!bundle reset all` to reset all bundle progress for the server.

Progress is **server-based** for use in multiplayer campaigns of Stardew Valley and persists in `bundles_state.json`.

A bundle is considered completed when the number of checked items reaches the amount of items that is needed to complete the bundle, for example, the Artisan Bundle lists 12 items that can be turned in but only requires 6 items. When 6 items are marked as checked the bundle will be marked as complete.

### Season Commands

Use `!season [spring|summer|fall|winter]` (i.e. `!season summer`) to show a list of the crops, trees, and fish that are unique to the season.

<img width="598" height="306" alt="image" src="https://github.com/user-attachments/assets/1055ab92-27e0-4f6e-835a-e5f0f19b7b37" />

Use `!season [spring|summer|fall|winter] bundle` (i.e. `!season summer bundle`) to list out specifically the items that appear in bundles that are unique to the season.

<img width="605" height="268" alt="image" src="https://github.com/user-attachments/assets/d6816c24-ce0f-47ba-acbd-3c5fd83e49bc" />

Use `!season [spring|summer|fall|winter] [crops|fish|foraging|trees]` (i.e. `!season summer fish`) to show a list of items specific to that season and that category.

<img width="604" height="164" alt="image" src="https://github.com/user-attachments/assets/fae6a39b-7eca-439d-bf7c-83c8d8358fe9" />

Use `!season [spring|summer|fall|winter] [crops|fish|foraging|trees] bundle` to similarly show a list of items specific to that season and that category, but filters to show just the items that appear in bundles.

<img width="604" height="138" alt="image" src="https://github.com/user-attachments/assets/b0e25649-bf09-4cac-901e-8bbbf86cf4b1" />

### Fish Commands

Use `!fish [fish]` to show information about a specific fish, such as location, weather, time of day, and season required to catch.

<img width="597" height="240" alt="image" src="https://github.com/user-attachments/assets/f4338f3d-f4c0-48d9-9c37-4df39b8cad74" />

### Crop Commands

Use `!crop [crop]` to show the season and grow time for a specific crop.

<img width="597" height="238" alt="image" src="https://github.com/user-attachments/assets/73bf5c16-ccb2-464e-9390-54fd900d5c8b" />

### Junimo Command

`!junimo` - Suprise!
Use `!junimo help` to show a brief list of all the available commands that this bot can handle.

## Setup

To host your own version of the discord bot. 

1. Create a Discord application & bot in the [Discord Developer Portal](https://discord.com/developers/applications), invite it to your server.
2. Create a `.env` file alongside `main.py` with `BOT_TOKEN = YOUR_DISCORD_BOT_TOKEN`.
3. Install requirements (discord.py, python-dotenv).
4. Run `python main.py`. If you want to run your own modified version, you can clone this repository, update/change what you want and run that version of `main.py`.

## Credits

StardewSavant is built as an extended version of [StardewSavvy](https://github.com/alysshah/sdv-bot).

Original implementation: [alysshah](https://github.com/alysshah)

Extended/Altered version built by Lex Mullin ([alemulli](https://github.com/alemulli)).

Information and images sourced from the [Stardew Valley Wiki](stardewvalleywiki.com).
