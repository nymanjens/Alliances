# Definitions

* **Round:** A single iteration of the game flow.
* **Unit:** Military unit, either an infantry or an artillery
* **Regions:** Named region on the map bounded by lines
    * **Strategic region:** Region with a star
    * **Sea region:** Region that consists mostly of a water body (the inverse of land regions)
    * **Land region:** Region that consists mostly of land (the inverse of sea regions)
    * **Occupied region:** Land region occupied by at least one unit
    * **Unoccupied region:** Land region not occupied by any units
    * **Neutral region:** Land region occupied by neutral units
    * **Region owned by a player:** Land region occupied by units of that player
    * **Friendly region for a player:** Land region occupied by units of that player, or
      units of an ally of that player
    * **Enemy region for a player:** Land region occupied by neutral units, or units of an enemy
      of that player
    * **Conquered region:** Land region won after successful battle earlier during the current
      command. This excludes previously unoccupied regions now occupied by retreated units.

# Contents of the game

* **Per player:**
    * Units:
        * Infantry: 14
        * Artillery: 5
    * Command tokens:
        * Invest: 2
        * Dig trenches: 1
        * Move: 3
        * Train units: 3
* **General:**
    * Coins: infinite
    * Neutral infantry: infinite
    * Trenches: infinite

# Teams

There are 2 opposing teams:

* The Triple Entente:
    * The British Empire
    * The Russian Empire (Россійская Имперія)
    * The French Third Republic (La Troisième République)
* The Central Powers:
    * The German Empire (Das Deutsches Kaiserreich)
    * The Ottoman Empire (دولت عليه عثمانیه)
    * The Austro-Hungarian Empire (Die Österreichisch-Ungarische Monarchie / Az Osztrák–Magyar Monarchia)

# Goal of the game

Take control over strategic regions. On every turn the team with the most strategic regions gains
points equal to the number of surplus regions. Strategic regions where units are trained this turn,
temporarily don't count. In case of a tie, neither team gains a point.

First to 6 points wins. If after an exhaustingly long war, neither team manages to reach 6 points,
whichever side may call itself the victor. For in war, there are no winners, but all are losers.

# Playing a round

Every round is divided into parts that happen simultaneously (\*) unless stated otherwise. Parts in
brackets ([example]) need no player input and can be done quickly.

1. **Token assignment**
    * All players put command tokens face down on regions they own (\*).
1. **[Token revealing and roll for start player]**
    * **Token revealing:** All tokens are turned face up
    * **Roll for start player**: Roll a dice. The player corresponding to the number (see below)
       becomes the new start player. If that player is not in the game, roll again until it is.

       The number-player correspondence is indicated on the board:

        * 1 - British Empire (down)
        * 2 - German Empire (up)
        * 3 - Russian Empire (down)
        * 4 - Ottoman Empire (up)
        * 5 - French Republic (down)
        * 6 - Austro-Hungarian Empire (up)

       The board also indicates the direction of the player order. Note that the full circle of the
       player order should always be the same as that of the above player order.

       *Example: If the dice shows 4 eyes, the player order is Ottoman Empire, Russian Empire, German
       Empire, British Empire, Austro-Hungarian Empire, French Republic.*
1. **Resolve Invest and Dig trenches tokens** (\*)
1. **Resolve Move tokens** (in player order)
1. **[Point scoring]**
    * The team controlling the most strategic regions that don't contain a Train token gains points
      equal to those surplus regions. In case of a tie, both teams gain 1 point. Check the game end
      condition.
1. **Production, payment and mutiny** (\*)
    * **Production:** All players receive the total amount of coins invested in regions they own,
       with a *minimum of 3*.
    * **Payment:** All units in regions the player wants to keep, are paid 1 coin per
       infantry and 2 coins per artillery.
    * **Mutiny:** All units which were not paid this round, convert to neutral infantry units (i.e.
       artillery converts to neutral infantry). Neutral units in sea regions are removed from the
       board.
1. **Train units and revival** (\*)
    * **Resolve Train units tokens**
    * **Revival:** Any player with *a unit cost of less than 3 coins* gets free units of their
       choice. After revival, the total unit cost may not exceed 3 coins. New units must be placed
       on regions owned by the player. If that's impossible, the player may pick a *single
       unoccupied or sea region*.
       All added units must be paid immediately.

(\*) Decisions are made simultaneously if possible. In case of a conflict, e.g. when a number of
players repetitively alter their decision in reaction to another player's decision, all players
whisper the solution to a player not involved who then executes the commands. When there is no such
player available, all write down their action and execute that action.

# Command tokens

* **Invest**:<br>
  You may change the number of coins in this region.

  Coins are exchanged between the player's supply and the region on the board. The maximum number of
  coins that may be invested in the region is indicated on the board.

  This token is ignored in **sea regions**.

* **Dig trenches**:<br>
  Up to two new trenches may be placed in this region on trench placeholders that don't already have
  a trench.

  This token is ignored in **sea regions**.

* **Move**:<br>
  All units in this region can move. Units can move separately to multiple regions.

  First, the player shows the other players all planned moves by moving units to their desired
  destinations. If there are multiple battles, the player chooses the subsequent battle every time the
  previous one concluded.

* **Train units**:<br>
  You can add/upgrade units in this region up to an additional cost of 2 coins if it's a strategic
  region, or 1 coin if it's a normal land region. Having this token on a strategic region however
  prevents it from generating a point.

  This token is ignored in **sea regions**.

  *Example: A normal land region contains 1 infantry. You can upgrade that infantry to an artillery
  or add an additional infantry.*

## Moving units

Units can move to an adjacent region. If this adjacent region has at least one invested coin and
was already friendly prior to resolving the move token, the unit may move through it to a next region
adjacent to this invested region. Units cannot end in friendly regions owned by other players.

*Examples:*

* *My infantry in England can move through N-France (occupied by an ally) to Benelux because
  N-France has an invested coin.*
* *If I have 3 units in the Middle East and there are coins invested in unoccupied Egypt, I cannot
  go from the Middle East to Libya with a single move token. This is because Egypt is not a friendly
  region before resolving this move token.*

### Plundering

If a unit's move ends in a previously unoccupied region, invested coins may be (partly) stolen.

### Sea regions

Units of different players and even teams can reside in the same sea region simultaneously.

### Straits

The following land-land borders can also be crossed by sea-sea movement, as indicated on the map:

* **Sweden - Denmark** (the Sound)
* **England - North France** (Strait of Dover)
* **Spain - North Africa** (Strait of Gibraltar)
* **Bulgaria - Turkey** (Bosphorus Strait and Dardanelles Strait)

Sea-sea movement is not possible for a unit if any land region at the strait is an enemy region.

## Battles

When a move proceeds into an enemy region, a battle is initiated with all moved units.

### Battle mechanic

A battle has one or more rounds. Every round has following parts:

1. **Artillery strike:**
    * Every attacking artillery kills 1 unit (\*)
1. **Rolling dice:**
    * Attacker gets a dice for every attacking **infantry unit**
    * Defender gets a dice for every defending **unit** (infantry + artillery)
    * Every attacker roll of:
        * **3-4:** Forces an enemy unit to retreat
        * **5-6:** Kills an enemy unit
    * Every defender roll of:
        * **1-4:** Forces an enemy unit to retreat
        * **5-6:** Kills an enemy unit

   Kills are resolved before forced retreat.
1. **Attacker retreat:** The attacker chooses their forced retreating units plus any additional units
   they want to retreat. All these units move back to the region where the move started.

   If no attacking units are left, the battle is instantly over and any defending units that would
   have been forced to retreat, don't retreat but remain in the region.
1. **Defender retreat:** The defender chooses their forced retreating units plus any additional units
   they want to retreat. All these units move to a single adjacent land region that is either owned by
   the defender or unoccupied, but not the region where the attacker's move started. Retreating units
   in subsequent battle rounds need to retreat to this same area.

   If no such region is found, the units are killed. If there is a choice, the defender may choose
   the region.

   If no defending units are left, the battle is instantly over and the attacker moves all remaining
   attacking units into the region. The invested coins in the conquered region may be kept on the
   board or may be (partly) stolen. If a token is present, the attacker may use it in a next command
   round after which the token returns to the defender.

Clarifications for edge cases:

* If the attacker completely **vacated a region** to attack an adjacent region, defending units
  may *not* retreat to this region.
* If the attacker is attacking **multiple regions**, it is possible that units could retreat to
  another region under attack. Retreated units are allowed to participate in the
  following battle.
* If the attacker has **won the battle**, he can still choose to retreat with any number of his units.

### Trench warfare

When attacking a region that has a trench on the defender's side of the border that the attacker is
crossing, the defender has advantages:

* Defending units cannot be forced to retreat (only killed)
* The defender gets **2** dice for every defending unit

### Fighting neutral regions

Neutral units will never attack, but do defend. The same rules apply as for normal combat. Whenever
a defender has to make a choice (e.g. retreat), the enemy team of the attacker may make that
decision.

# Coin trading

At any point in the game, you may give up to 2 coins to another player when you remove an extra coin
from your supply.

*Examples:*

* *When an ally is struggling with paying their units*
* *When an ally wants to invest in a region but has no coins*

# Initial setup

## Initial supply

* Every player gets 3 coins in their supply

## Beginner

Choose a [scenario](Scenarios.md) for the desired number of players *at random*.

* Every player gets 2 coins in every region they own
* Remove one start unit from the non-strategic start region of every player.

## Advanced

Choose a [scenario](Scenarios.md) for the desired number of players *at random*.

* Every player gets 2 coins in every region they own
* For every unoccupied region, roll a dice. If its result is:
    * 1-3: Nothing happens
    * 4-6: Add 1 coin

## Expert

Every player chooses a team. The teams are sitting crossed-wise and in order.

For 4|6 players: give everyone 3|2 cards from the 12 strategic cards. Give everyone 6|4 cards of
the remaining 24 cards. Every player should now have a deck of 9|6 cards to draft from.

Every player drafts their starting regions by picking a card from his deck, and putting it face
down on the table. When all players did this, reveal the cards and everyone puts a unit on the region
they picked. Everyone gives the remaining cards to the player on their left, and repeats the procedure
with the cards they received from the player on their right. Continue until all the cards are drafted.

At the end of the draft, every player chooses at least 3|2 cards from their drafted deck of cards and
puts them face down on the table. When all players did this, reveal those cards and everyone removes
all their units from the region on their card. No player may have more than 1 strategic region at this
point.

Everyone puts an additional 2 coins and 1 unit on their strategic region (if any), to a total of 2
units and 2 coins. Everyone also puts an additional coin on every land region they own, to a total
of 1 coin and 1 unit. Everyone who owns a sea region should have a unit there without coins.

Every unused strategic region also gets an additional 2 coins and 2 neutral units.
