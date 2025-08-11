from discord.ext import commands
import discord
import json
import os
from dotenv import load_dotenv
from typing import Optional
from discord.ext.commands import CommandNotFound, MissingRequiredArgument, BadArgument, UserInputError

STATE_PATH = Path("bundles_state.json")
CC_PATH = Path("communitycenter.json")

# Load environment variables from .env
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
BUNDLES_STATE_PATH = os.path.join(DATA_DIR, 'bundles_state.json')

########################
# Utility: JSON loading
########################

def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

townspeople_data = load_json('townspeople.json')
building_data = load_json('building.json')
events_data = load_json('events.json')
fish_data = load_json('fish.json')
seasons_data = load_json('seasons.json')
crops_data = load_json('crops.json')
community_data = load_json('communitycenter.json')
upgrades_data = load_json('upgrades.json')

########################
# Bot lifecycle
########################

@bot.event
async def on_ready():
    print("StardewSavant is ready!")

@bot.event
async def on_command_error(ctx, error):
    # Unknown command -> nudge toward help
    if isinstance(error, CommandNotFound):
        return await ctx.send("Unknown command. Try `!junimo help` for a list of commands.")

    # Missing pieces -> show per-command usage
    if isinstance(error, MissingRequiredArgument):
        cmd = ctx.command.qualified_name if ctx.command else ''
        if cmd == 'bundle check':
            return await ctx.send('I didn\'t understand your command, did you mean this?\nUsage: `!bundle check "Bundle Name" Item Name`\nExample: `!bundle check "Artisan Bundle" Cherry`')
        if cmd == 'bundle uncheck':
            return await ctx.send('I didn\'t understand your command, did you mean this?\nUsage: `!bundle uncheck "Bundle Name" Item Name`\nExample: `!bundle uncheck "Artisan Bundle" Cherry`')
        if cmd == 'gift':
            return await ctx.send('I didn\'t understand your command, did you mean this?\nUsage: `!gift <villager>`\nExample: `!gift Leah`')
        if cmd == 'char':
            return await ctx.send('I didn\'t understand your command, did you mean this?\nUsage: `!char <villager>`\nExample: `!char Leah`')
        if cmd == 'build':
            return await ctx.send('I didn\'t understand your command, did you mean this?\nUsage: `!build <building>`\nExample: `!build Big Barn`')
        if cmd == 'upgrade':
            return await ctx.send('I didn\'t understand your command, did you mean this?\nUsage: `!upgrade <tool>`\nExample: `!upgrade Iridium Pickaxe`')
        if cmd == 'fish':
            return await ctx.send('I didn\'t understand your command, did you mean this?\nUsage: `!fish <fish name>`\nExample: `!fish Midnight Carp`')
        if cmd == 'crop':
            return await ctx.send('I didn\'t understand your command, did you mean this?\nUsage: `!crop <crop name>`\nExample: `!crop Blueberry`')
        if cmd == 'events':
            return await ctx.send('I didn\'t understand your command, did you mean this?\nUsage: `!events <spring|summer|fall|winter> [day]`\nExample: `!events winter 3`')
        if cmd == 'season':
            return await ctx.send('I didn\'t understand your command, did you mean this?\nUsage: `!season <spring|summer|fall|winter> [crops|fish|foraging|trees] [bundle]`\nExample: `!season spring crops bundle`')
        return await ctx.send("That command was missing something. Try `!junimo help`.")

    # Other user input issues
    if isinstance(error, (BadArgument, UserInputError)):
        return await ctx.send(str(error))

    # Fallback (also logs to console)
    print("Unhandled command error:", repr(error))
    await ctx.send("Oops, I couldn't run that. Double-check the format or try `!junimo help`.")


########################
# Helpers for Embeds
########################

def make_embed(title: str, color: int = 0x1e31bd, thumb: str | None = None, fields: list[tuple[str, str, bool]] | None = None):
    embed = discord.Embed(title=title, color=color)
    if thumb:
        embed.set_thumbnail(url=thumb)
    if fields:
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
    return embed

########################
# GIFT COMMAND
########################

@bot.command(name='gift')
async def gift(ctx, townsperson: str):
    t = townsperson.capitalize()
    if t in townspeople_data:
        data = townspeople_data[t]
        loves_formatted = '\n'.join(f'- {item}' for item in data.get("loves", []))
        likes_formatted = '\n'.join(f'- {item}' for item in data.get("likes", []))
        embed = make_embed(
            title=f"Gift Preferences for {t}",
            color=0x1e31bd,
            thumb=data.get("image"),
            fields=[
                ("Loves", loves_formatted or '—', True),
                ("Likes", likes_formatted or '—', True),
            ]
        )
        button = discord.ui.Button(label="View All Gifts on Wiki", url="https://stardewvalleywiki.com/List_of_All_Gifts")
        view = discord.ui.View()
        view.add_item(button)
        await ctx.send(embed=embed, view=view)
    else:
        await ctx.send(f"No data available for {t}.")

########################
# CHARACTER COMMAND
########################

@bot.command(name='char')
async def char(ctx, townsperson: str):
    t = townsperson.capitalize()
    if t in townspeople_data:
        data = townspeople_data[t]
        embed = make_embed(
            title=f"Profile for {t}",
            color=0x0f700b,
            thumb=data.get("image"),
            fields=[("Birthday", data.get("birthday", '—'), False)]
        )
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"No data available for {t}.")

########################
# BUILD COMMAND
########################

@bot.command(name='build')
async def build(ctx, *building: str):
    b = " ".join(building).title()
    if b in building_data:
        data = building_data[b]
        cost_formatted = '\n'.join(f'- {item}' for item in data.get("cost", []))
        embed = make_embed(
            title=f"Cost for {b}",
            color=0xff0000,
            thumb=data.get("image"),
            fields=[("Materials", cost_formatted or '—', False)]
        )
        button = discord.ui.Button(label="View All Buildings on Wiki", url="https://stardewvalleywiki.com/Carpenter%27s_Shop#Farm_Buildings")
        view = discord.ui.View()
        view.add_item(button)
        await ctx.send(embed=embed, view=view)
    else:
        await ctx.send(f"No data available for {b}.")

########################
# EVENTS COMMAND
########################

@bot.command(name='events')
async def events(ctx, season, day: str | None = None):
    season = season.capitalize()
    if day is None:
        if season in events_data:
            embed = make_embed(title=f"Happening in {season}", color=0x5c15ad)
            data = events_data[season]
            events_formatted = ""
            for d in sorted(data, key=lambda x: int(x)):
                for event in data[d]:
                    events_formatted += f"- {d}: {event}\n"
            embed.add_field(name="Event(s)", value=events_formatted or 'No events', inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Please provide an existing season")
    else:
        if season in events_data:
            try:
                dnum = int(day)
            except ValueError:
                return await ctx.send("Day must be a number between 1 and 28.")
            if dnum > 28 or dnum < 1:
                await ctx.send("Not a valid date.")
            else:
                embed = make_embed(title=f"Happening on {season} {day}", color=0x5c15ad)
                data = events_data[season]
                if day in data:
                    events_formatted = '\n'.join(f'- {item}' for item in data[day])
                    embed.add_field(name="Event(s)", value=events_formatted, inline=False)
                else:
                    embed.add_field(name="Event(s)", value="No events", inline=False)
                await ctx.send(embed=embed)
        else:
            await ctx.send("No data available for this date.")

########################
# FISH COMMAND
########################

@bot.command(name='fish')
async def fish(ctx, *fish_name: str):
    name = " ".join(fish_name).strip()
    key = next((k for k in fish_data.keys() if k.lower() == name.lower()), None)
    if not key:
        return await ctx.send(f"I couldn't find fish named '{name}'.")
    data = fish_data[key]
    fields = [
        ("Location", data.get("Location", '—'), True),
        ("Season", data.get("Season", '—'), True),
        ("Time", data.get("Time", '—'), True),
        ("Weather", data.get("Weather", '—'), True),
        ("Base Sell Price", data.get("Base Sell Price", '—'), True),
        ("Bundle", 'Yes' if data.get("Bundle") else 'No', True),
    ]
    embed = make_embed(title=key, color=0x2aa198, thumb=data.get("image"), fields=fields)
    await ctx.send(embed=embed)

########################
# SEASON COMMAND (expanded)
########################

def _normalize_name(s: str) -> str:
    # Remove simple parentheticals like "Common Mushroom (Secret Woods)" -> "Common Mushroom"
    return s.split('(')[0].strip()

def _remaining_items_for_guild(guild_id: int) -> set[str]:
    """All item names still unchecked across incomplete bundles."""
    state = _init_bundles_state_for_guild(guild_id)
    gid = str(guild_id)
    remaining: set[str] = set()

    for room_name, room in community_data.items():
        for b_name, canonical in room.get('Bundles', {}).items():
            amount_needed = canonical.get('amount', 0)
            current = state[gid].get(room_name, {}).get(b_name, {}).get('items', {})
            count_true = sum(1 for v in current.values() if v)
            if count_true < amount_needed:
                for item in canonical['items'].keys():
                    if not current.get(item, False):
                        remaining.add(item)
    return remaining

def _season_category_lists(season_name: str):
    """Return dict with 'crops', 'fish', 'foraging', 'trees' lists for a season."""
    s = season_name.capitalize()
    data = seasons_data.get(s, {})
    crops = data.get('Crops', {})
    crops_names = list(crops.get('Single Harvest', {}).keys()) + list(crops.get('Multi Harvest', {}).keys())
    fish_names = list(data.get('Fish', {}).keys())
    foraging_names = [_normalize_name(x) for x in data.get('Foraging', [])]
    trees_names = list(data.get('Trees', {}).keys())
    return {
        'crops': crops_names,
        'fish': fish_names,
        'foraging': foraging_names,
        'trees': trees_names
    }

def _filter_to_remaining(names: list[str], remaining: set[str]) -> list[str]:
    rem_lower = {r.lower(): r for r in remaining}
    out = []
    for n in names:
        key = n.lower()
        if key in rem_lower:
            out.append(n)
        else:
            # some bundle items use variants like "5 Parsnip★" etc; do a loose contains check
            if any(key == r.lower() or key in r.lower() or r.lower() in key for r in remaining):
                out.append(n)
    # De-dup while preserving order
    seen = set()
    uniq = []
    for x in out:
        if x.lower() not in seen:
            seen.add(x.lower())
            uniq.append(x)
    return uniq

@bot.command(name='season')
async def season(ctx, season: str, *args: str):
    s = season.capitalize()
    if s not in seasons_data:
        return await ctx.send("Season must be Spring, Summer, Fall, or Winter.")
    args = [a.lower() for a in args]
    sub = args[0] if args else None
    want_bundle_filter = 'bundle' in args[1:] if len(args) > 1 else (args == ['bundle'])

    categories = _season_category_lists(s)

    # If user asked for a specific category
    if sub in ('crops', 'fish', 'foraging', 'trees'):
        items = categories[sub]
        if want_bundle_filter:
            remaining = _remaining_items_for_guild(ctx.guild.id)
            items = _filter_to_remaining(items, remaining)
        text = ', '.join(items) if items else '—'
        title = f"{s} {sub.capitalize()}" + (" (Needed for Incomplete Bundles)" if want_bundle_filter else "")
        embed = make_embed(title=title, color=0x859900, fields=[(sub.capitalize(), text[:1024], False)])
        return await ctx.send(embed=embed)

    # If user asked for overall "bundle" view for the season
    if sub == 'bundle' or want_bundle_filter:
        remaining = _remaining_items_for_guild(ctx.guild.id)
        out = {}
        for k in categories:
            out[k] = _filter_to_remaining(categories[k], remaining)
        fields = []
        fields.append(("Crops", (', '.join(out['crops']) or '—')[:1024], False))
        fields.append(("Fish", (', '.join(out['fish']) or '—')[:1024], False))
        fields.append(("Foraging", (', '.join(out['foraging']) or '—')[:1024], False))
        fields.append(("Trees", (', '.join(out['trees']) or '—')[:1024], False))
        embed = make_embed(title=f"{s} – Incomplete Bundle Targets", color=0x5f9ea0, fields=fields)
        return await ctx.send(embed=embed)

    # Default original summary view
    data = seasons_data[s]

    # Crops summary
    crops = data.get('Crops', {})
    single = list(crops.get('Single Harvest', {}).keys())
    multi = list(crops.get('Multi Harvest', {}).keys())
    crops_lines = []
    if single:
        crops_lines.append(f"Single: {', '.join(single)}")
    if multi:
        crops_lines.append(f"Multi: {', '.join(multi)}")
    crops_text = '\n'.join(crops_lines) or '—'

    # Foraging
    foraging = [_normalize_name(x) for x in data.get('Foraging', [])]
    foraging_text = ', '.join(foraging) or '—'

    # Fish (ALL fish for the season)
    fish_all = list(data.get('Fish', {}).keys())
    fish_text = ', '.join(fish_all) or '—'

    # Trees
    trees = list(data.get('Trees', {}).keys())
    trees_text = ', '.join(trees) or '—'

    embed = make_embed(
        title=f"Season: {s}",
        color=0x859900,
        fields=[
            ("Crops", crops_text[:1024], False),
            ("Foraging", foraging_text[:1024], False),
            ("Fish", fish_text[:1024], False),
            ("Trees", trees_text[:1024], False),
        ]
    )
    await ctx.send(embed=embed)

########################
# CROP COMMAND
########################

@bot.command(name='crop')
async def crop(ctx, *crop_name: str):
    name = " ".join(crop_name).strip()
    key = next((k for k in crops_data.keys() if k.lower() == name.lower()), None)
    if not key:
        return await ctx.send(f"I couldn't find crop named '{name}'.")
    data = crops_data[key]
    fields = [
        ("Season", data.get("Season", '—'), True),
        ("Type", data.get("Type", '—'), True),
        ("Growth Time", data.get("Growth Time", '—'), True),
        ("Max Harvests", data.get("Max Harvests", '—'), True),
        ("Seed Price", data.get("Seed Price", '—'), True),
        ("Base Sell Price", data.get("Base Sell Price", '—'), True),
        ("Bundle", 'Yes' if data.get("Bundle") else 'No', True),
    ]
    embed = make_embed(title=key, color=0xb58900, thumb=data.get("image"), fields=fields)
    await ctx.send(embed=embed)

########################
# UPGRADE COMMAND (tools/house)
########################

@bot.command(name='upgrade')
async def upgrade(ctx, *upgrade_name: str):
    name = " ".join(upgrade_name).strip().title()
    key = next((k for k in upgrades_data.keys() if k.lower() == name.lower()), None)
    if not key:
        return await ctx.send(f"I couldn't find an upgrade named '{name}'.")
    data = upgrades_data[key]
    cost_formatted = '\n'.join(f'- {item}' for item in data.get("cost", []))
    embed = make_embed(title=f"Upgrade: {key}", color=0xcb4b16, thumb=data.get("image"), fields=[("Cost", cost_formatted or '—', False)])
    await ctx.send(embed=embed)

#################################
# JUNIMO COMMAND GROUP (fun/help)
#################################

@bot.group(name='junimo', invoke_without_command=True)
async def junimo(ctx):
    # Return just the gif when called without subcommands
    await ctx.send("https://stardewvalleywiki.com/mediawiki/images/5/57/Junimo.gif")

@junimo.command(name='help')
async def junimo_help(ctx):
    desc = [
       "TBD"
    ]
    await ctx.send("\n".join(desc))

########################################
# BUNDLE COMMAND GROUP (with persistence)
########################################

@bot.group(name='bundle', invoke_without_command=True)
async def bundle(ctx, *query: str):
    """Default: show overview or search by item/room/bundle depending on args."""
    _init_bundles_state_for_guild(ctx.guild.id)
    q = " ".join(query).strip()
    if not q:
        return await _send_bundles_overview(ctx)

    # First try exact room match
    room_name = next((r for r in community_data.keys() if r.lower() == q.lower()), None)
    if room_name:
        return await _send_room_status(ctx, room_name)

    # Then try bundle name
    bkey = next((b for b in BUNDLE_NAME_TO_ROOM.keys() if b == q.lower()), None)
    if bkey:
        room, bundle = BUNDLE_NAME_TO_ROOM[bkey]
        return await _send_bundle_status(ctx, room, bundle)

    # Lastly treat as item search
    matches = ITEM_TO_BUNDLES.get(q.lower())
    if matches:
        lines = [f"**{q}** appears in:", *(f"- {room} → {bundle}" for room, bundle in matches)]
        return await ctx.send('\n'.join(lines))

    await ctx.send("No matching room, bundle, or item found. Try `!bundle`, `!bundle <room>`, `!bundle <bundle name>`, or `!bundle find <item>`.")

@bundle.command(name='find')
async def bundle_find(ctx, *item: str):
    _init_bundles_state_for_guild(ctx.guild.id)
    q = " ".join(item).strip()
    matches = ITEM_TO_BUNDLES.get(q.lower())
    if not matches:
        return await ctx.send(f"No bundles use '{q}'.")
    lines = [f"**{q}** appears in:"] + [f"- {room} → {bundle}" for room, bundle in matches]
    await ctx.send('\n'.join(lines))

@bundle.command(name='status')
async def bundle_status(ctx, *name: str):
    _init_bundles_state_for_guild(ctx.guild.id)
    q = " ".join(name).strip()
    if not q:
        return await _send_bundles_overview(ctx)
    # room or bundle
    room_name = next((r for r in community_data.keys() if r.lower() == q.lower()), None)
    if room_name:
        return await _send_room_status(ctx, room_name)
    bkey = next((b for b in BUNDLE_NAME_TO_ROOM.keys() if b == q.lower()), None)
    if bkey:
        room, bundle = BUNDLE_NAME_TO_ROOM[bkey]
        return await _send_bundle_status(ctx, room, bundle)
    await ctx.send("Not found. Use a room or bundle name.")

@bundle.command(name='check')
async def bundle_check(ctx, bundle_name: str, *, item_name: str):
    """Mark an item complete. Usage: !bundle check "<Bundle Name>" <Item Name>"""
    state = _init_bundles_state_for_guild(ctx.guild.id)
    gid = str(ctx.guild.id)
    bkey = bundle_name.lower()
    if bkey not in BUNDLE_NAME_TO_ROOM:
        return await ctx.send("Bundle not found. Tip: wrap bundle names with spaces in quotes.")
    room, bundle = BUNDLE_NAME_TO_ROOM[bkey]
    try:
        current = state[gid][room][bundle]['items']
    except KeyError:
        return await ctx.send("State not initialized correctly. Try again.")

    ikey = next((k for k in current.keys() if k.lower() == item_name.lower()), None)
    if not ikey:
        return await ctx.send(f"'{item_name}' is not part of {bundle}.")

    current[ikey] = True
    _save_bundles_state(state)
    await _send_bundle_status(ctx, room, bundle)

@bundle.command(name='uncheck')
async def bundle_uncheck(ctx, bundle_name: str, *, item_name: str):
    """Mark an item incomplete. Usage: !bundle uncheck "<Bundle Name>" <Item Name>"""
    state = _init_bundles_state_for_guild(ctx.guild.id)
    gid = str(ctx.guild.id)
    bkey = bundle_name.lower()
    if bkey not in BUNDLE_NAME_TO_ROOM:
        return await ctx.send("Bundle not found. Tip: wrap bundle names with spaces in quotes.")
    room, bundle = BUNDLE_NAME_TO_ROOM[bkey]
    try:
        current = state[gid][room][bundle]['items']
    except KeyError:
        return await ctx.send("State not initialized correctly. Try again.")

    ikey = next((k for k in current.keys() if k.lower() == item_name.lower()), None)
    if not ikey:
        return await ctx.send(f"'{item_name}' is not part of {bundle}.")

    current[ikey] = False
    _save_bundles_state(state)
    await _send_bundle_status(ctx, room, bundle)

@bundle.command(name='reset')
async def bundle_reset(ctx, scope: str = 'all'):
    """Reset bundle progress. Usage: !bundle reset [all]"""
    if scope.lower() != 'all':
        return await ctx.send("For now, only `!bundle reset all` is supported.")
    state = _load_bundles_state()
    if str(ctx.guild.id) in state:
        del state[str(ctx.guild.id)]
    _save_bundles_state(state)
    _init_bundles_state_for_guild(ctx.guild.id)
    await ctx.send("All bundle progress reset for this server.")

@bundle.command(name='incomplete')
async def bundle_incomplete(ctx):
    """List only incomplete bundles grouped by room."""
    state = _init_bundles_state_for_guild(ctx.guild.id)
    gid = str(ctx.guild.id)

    def room_incomplete(room_label: str, bundles_dict: dict):
        items = []
        for b_name, canonical in bundles_dict.items():
            amount = canonical.get('amount', 0)
            current = state[gid].get(room_label, {}).get(b_name, {}).get('items', {})
            count_true = sum(1 for v in current.values() if v)
            if count_true < amount:
                items.append((b_name, f"⬜ {count_true}/{amount}"))
        return items

    fields = []
    for room_name, room in community_data.items():
        items = room_incomplete(room_name, room.get('Bundles', {}))
        if items:
            fields.append((room_name, "\n".join(f"- {n}: {s}" for n, s in items)[:1024], False))

    if not fields:
        return await ctx.send("All bundles are complete. 🎉")
    embed = make_embed(title="Incomplete Bundles", color=0xd2691e, fields=fields)
    await ctx.send(embed=embed)

############################
# Bundle display helpers
############################

async def _send_bundles_overview(ctx):
    state = _init_bundles_state_for_guild(ctx.guild.id)
    gid = str(ctx.guild.id)
    fields = []
    for room_name, room in community_data.items():
        bundles = room.get('Bundles', {})
        completed, total = _room_completion_counts(state[gid], room_name, bundles)
        fields.append((room_name, f"{completed}/{total} bundles completed", False))

    embed = make_embed(title="Community Center Progress", color=0x34a853, fields=fields)
    await ctx.send(embed=embed)

def _room_completion_counts(guild_state: dict, room_name: str, bundles_dict: dict):
    completed = 0
    total = len(bundles_dict)
    for b_name, bundle in bundles_dict.items():
        amount_needed = bundle.get('amount', 0)
        current = guild_state.get(room_name, {}).get(b_name, {}).get('items', {})
        count_true = sum(1 for v in current.values() if v)
        if count_true >= amount_needed:
            completed += 1
    return completed, total

async def _send_room_status(ctx, room_name: str):
    state = _init_bundles_state_for_guild(ctx.guild.id)
    gid = str(ctx.guild.id)

    room = community_data.get(room_name, {})
    bundles = room.get('Bundles', {})

    fields = []
    for b_name, bundle in bundles.items():
        amount = bundle.get('amount', 0)
        current = state[gid].get(room_name, {}).get(b_name, {}).get('items', {})
        count_true = sum(1 for v in current.values() if v)
        status = "✅ Completed" if count_true >= amount else f"⬜ {count_true}/{amount}"
        fields.append((b_name, status, False))
    embed = make_embed(title=f"{room_name} – Bundles", color=0x34a853, fields=fields)
    await ctx.send(embed=embed)

async def _send_bundle_status(ctx, room_name: str, bundle_name: str):
    state = _init_bundles_state_for_guild(ctx.guild.id)
    gid = str(ctx.guild.id)

    canonical = community_data[room_name]['Bundles'][bundle_name]

    current = state[gid][room_name][bundle_name]['items']
    amount = canonical.get('amount', 0)
    reward = canonical.get('reward', '')
    image = canonical.get('image')

    lines = []
    count_true = 0
    for item_name in canonical['items'].keys():
        checked = current.get(item_name, False)
        lines.append(f"{'✅' if checked else '⬜'} {item_name}")
        if checked:
            count_true += 1

    footer = f"Progress: {count_true}/{amount} | Reward: {reward}" if reward else f"Progress: {count_true}/{amount}"
    embed = make_embed(title=f"{bundle_name} ({room_name})", color=0x34a853, thumb=image, fields=[("Items", '\n'.join(lines)[:1024], False), ("Status", footer, False)])
    await ctx.send(embed=embed)

########################
# Run the bot
########################

bot.run(os.getenv('BOT_TOKEN'))
