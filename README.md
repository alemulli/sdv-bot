# StardewSavant

StardewSavant is an extended version of StardewSavvy, a Stardew Valley Discord bot that helps you quickly access info while you play.

[Invite the bot to your server here](https://discord.com/oauth2/authorize?client_id=1404203614347464805&permissions=117760&integration_type=0&scope=bot)

## Commands

### Gift Command

Use `!gift [villager name]` (i.e. `!gift Leah`) to get a list of that villager’s loved and liked gifts.

### Character Command

Use `!char [villager name]` (i.e. `!char Leah`) to get a villager’s profile, including their birthday and a picture, and a link to the Stardew Valley Wiki for their schedule.

### Build Command

Use `!build [farm building]` (i.e. `!build Big Barn`) to see the cost and materials needed to build that farm building.

### Upgrade Command

Use `!upgrade [tool]` (i.e. `!upgrade Iridium Pickaxe`) to see the cost and materials needed to upgrade a tool.

### Events Command

Use `!events [spring|summer|fall|winter]` (i.e. `!events winter`) to see the events and birthdays for the season.
Use `!events [spring|summer|fall|winter] [Day]` (i.e. `!events winter 3`) to get a list of events and birthdays occurring on a specific day.

### Bundle Command

Use `!bundle` to show a list of all items needed for the Community Center.
Use `!bundle incomplete` to show a list of only the incompleted Community Center bundles for your server.
Use `!bundle find [item]` (i.e. `!bundle find Daffodil`) to check if an item belongs to a bundle in the Community Center and which bundle(s) use that item.
Use `!bundle [bundle room]` (i.e. `!bundle Pantry`) to show a list of all items needed for the bundles in a specific room in the Community Center.
Use `!bundle [bundle name]` (i.e. `!bundle Chef's Bundle`) to show a list of all items needed for a specific bundle in the Community Center.
Use `!bundle check "[bundle name]" [item]` to mark an item as completed in a bundle (i.e. `!bundle check "Chef's Bundle" Poppy`).
Use `!bundle uncheck "[bundle name]" [itme]` to similarly unmark an item as completed in a bundle if it was marked by mistake.
Use `!bundle reset all` to reset all bundle progress for the server.

Progress is **server-based** for use in multiplayer campaigns of Stardew Valley and persists in `bundles_state.json`.

A bundle is considered completed when the number of checked items reaches the amount of items that is needed to complete the bundle, for example, the Artisan Bundle lists 12 items that can be turned in but only requires 6 items. When 6 items are marked as checked the bundle will be marked as complete.

### Season Commands

Use `!season [spring|summer|fall|winter]` (i.e. `!season summer`) to show a list of the crops, trees, and fish that are unique to the season.
Use `!season [spring|summer|fall|winter] bundle` (i.e. `!season summer bundle`) to list out specifically the items that appear in bundles that are unique to the season.
Use `!season [spring|summer|fall|winter] [crops|fish|foraging|trees]` (i.e. `!season summer fish`) to show a list of items specific to that season and that category.
Use `!season [spring|summer|fall|winter] [crops|fish|foraging|trees] bundle` to similarly show a list of items specific to that season and that category, but filters to show just the items that appear in bundles.

### Fish Commands

Use `!fish [fish]` to show information about a specific fish, such as location, weather, time of day, and season required to catch.

### Crop Commands

Use `!crop [crop]` to show the season and grow time for a specific crop.

### Junimo Command

`!junimo` - Suprise!
Use `!junimo help` to show a brief list of all the available commands that this bot can handle.

## Setup

1. Create a Discord application & bot in the [Discord Developer Portal](https://discord.com/developers/applications), invite it to your server.
2. Create a `.env` file alongside `main.py` with `BOT_TOKEN = YOUR_DISCORD_BOT_TOKEN`.
3. Install requirements (discord.py, python-dotenv).
4. Run `python main.py`.

## Credits

StardewSavant is built as an extended version of [StardewSavvy](https://github.com/alysshah/sdv-bot).

Original implementation: [alysshah](https://github.com/alysshah)

Extended/Altered version built by Lex Mullin ([alemulli](https://github.com/alemulli)).

Information and images sourced from the [Stardew Valley Wiki](stardewvalleywiki.com).
