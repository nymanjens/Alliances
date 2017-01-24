# Definitions

* **Turn:** A single iteration of the game flow. There are a maximum of 10 turns in a game.
* **Unit:** Military unit, either an infantry or an artillery
    * **Healthy unit:** The default state of a unit. Able to move and participate in combat
    * **Wounded unit:** Acts like a normal unit, except that it has zero defence/attack and can't
      move (but it can retreat).
* **Strategic city:** Star on the map
* **Regions:** Region on the map bounded by white lines
    * **Sea region:** Region that consists mostly of a water body (the inverse of land regions)
    * **Land region:** Region that consists mostly of land (the inverse of sea regions)
    * **Occupied region:** Land region occupied by at least one military unit
    * **Unoccupied region:** Land region not occupied by any military units
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
        * Dig trench: 1
        * Move: 3
        * Train units: 2
* **General:**
    * Coins: infinite
    * Neutral infantry: infinite

# Teams

There are 2 teams:

* The Triple Entente:
    * UK
    * Russia
    * France
* Central players:
    * Germany
    * Ottoman Empire
    * Austro-Hungarian Empire

# Goal of the game

One of:

1. At the end of a turn `n` (`n in {1..10}`), have at least an `11 - n` point advantage over the
   other team (ends the game)
1. If there is no winner after turn 10, the team with the most strategic cities wins. If these
   match, whichever side may call itself the victor. For in war, there are no winners, but all are
   losers.

# Playing a turn

All decisions below happen simultaneously (&#42;) unless stated otherwise.

1. **Prepare phase:**
    1. **Token assignment:** All players simultaneously put command tokens face down on regions
       they own.
    1. **Token revealing:** All tokens are turned face up
    1. **Roll for start player**: Roll a dice. The player corresponding to the number (see below)
       becomes the new start player. If that player is not in the game, roll again until it is.

       The number-player correspondence is indicated on the board:

        * 1 - UK (down)
        * 2 - Germany (up)
        * 3 - Russia (down)
        * 4 - Ottoman Empire (up)
        * 5 - France (down)
        * 6 - Austro-Hungarian Empire (up)

       The board also indicates the direction of the player order. Note that the full circle of the
       player order should always be the same as that of the above player order.

       *Example: If the dice shows 4 eyes, the player order is Ottoman Empire, Russia, Germany, UK,
       Austro-Hungarians, France.*
    1. **Invest and Dig trench**: Resolve tokens (&#42;)
1. **Assault phase:**
    1. **Move**: Resolve tokens in player order
1. **Economic phase:**
    1. **Production:** All players receive the total amount of coins invested in regions they own,
       with a *minimum of 3*.
    1. **Payment:** All units in regions the player wants to keep, are paid 1 coins per
       infantry and 2 coins per artillery.
    1. **Mutiny:** All units which were not paid this turn, convert to neutral infantry units (i.e.
       artillery converts to neutral infantry). Neutral units in sea regions are removed from the
       board.
    1. **Point scoring:** Every team scores 1 point per strategic city they own
    1. **Advance turn counter** by one and check the game end condition
1. **Reorganise phase**
    1. **Revival:** Any player with *a unit cost of less than 3 coins* gets free units of their
       choice. After revival, the total unit cost may not exceed 3 coins. New units must be placed
       on regions owned by the player. If that's impossible, the player may pick a *single
       unoccupied or sea region*.
       All added units must be paid immediately.
    1. **Unit healing:** All wounded units are healed
    1. **Train units**: Resolve tokens simultaneously (&#42;)

(&#42;) Decisions are made simultaneously if possible. In case of a conflict, e.g. when a number of
players repetitively alter their decision in reaction to another player's decision, all players
whisper the solution to a player not involved who then executes the commands. When there is no such
player available, all write down their action and execute that action.

# Command tokens

* **Invest**:<br>
  You may change the number of coins in this region.

  Coins are exchanged between the player's supply and the region on the board. The maximum number of
  coins that may be invested in the region is indicated on the board.

  This token is ignored in **sea regions**.

* **Dig trench**:<br>
  A single trench may be placed at a border with another land region that has a trench placeholder
  on the map.

  This token is ignored in **sea regions**.

* **Move**:<br>
  All healthy units in this region can move. Units can move separately to multiple regions.

  First, the player shows the other players all planned moves by moving units to their desired
  destinations. If there are multiple battles, the player chooses the subsequent battle every time the
  previous one concluded.

* **Train units**:<br>
  You can add/upgrade units in this region up to an additional cost of 2 coins if it's a strategic
  city, or 1 coin if it's a normal land region.

  This token is ignored in **sea regions**.

  *Example: A normal land region contains 1 infantry. You can upgrade that infantry to an artillery
  or add an additional infantry.*

## Moving units

Units can move to any adjacent region, except for friendly regions owned by other players.

### Roads

Moves can hop over a single friendly region if a road exists (before resolving the move token) between
the starting region and that friendly region. A road exists between adjacent regions if both have at
least one invested coin.

*Examples:*

* *My infantry in England can move through N-France (occupied by an ally) to Benelux because both
  England and N-France have an invested coin.*
* *If I have 3 units in the Middle East and there are coins invested in unoccupied Egypt and the
  Middle East, I cannot go from the Middle East to N-Africa with a single move token. This is because
  Egypt is not a friendly region before resolving this move token.*

### Plundering

If a unit's move ends in a previously unoccupied region, invested coins may be (partly) stolen.

### Sea regions

Units of different teams can reside in the same sea region simultaneously.

### Ambiguous crossings

The following points on the map can be crossed both by land-land and sea-sea movement:

* **Denmark islands**
* **English Channel**
* **Gibraltar**
* **Istanbul**
* **North Channel (between Ireland and Scotland)**

Sea-sea movement is not possible for a unit if both land regions at the crossing are enemy regions.

## Battles

When a move proceeds into an enemy region, a battle is initiated with all moved units.

### Battle mechanic

A battle has one or more rounds. Every round has following parts:

1. **Artillery strike:**
    * Every healthy attacking artillery kills 1 unit (*)
1. **Rolling dice:**
    * Attacker gets a dice for every healthy attacking **infantry unit**
    * Defender gets a dice for every healthy defending **unit** (infantry + artillery)
    * Every attacker roll of:
        * **3-4:** Wounds an enemy unit (*)
        * **5-6:** Kills an enemy unit (*)
    * Every defender roll of:
        * **1-4:** Wounds an enemy unit (*)
        * **5-6:** Kills an enemy unit (*)

    Kills are resolved before wounds.
1. **Attacker decides to retreat or has no healthy units left:** All units move back to the region
   where to move started.

   Edge case: If the attacker has no healthy units left and the defender has no units left, the
   attacker has to retreat. Any command tokens on the attacked region are returned to the defender's
   supply.
1. **Defender decides to retreat or has no healthy units left:** All units (including wounded units)
   move to a single adjacent land region that is either unoccupied or owned by the defender.
   Exception: units can't retreat to the region where the attacker's move started.

  If no such region is found, the units are killed. If there is a choice, the defender may choose
  the region.

  Clarifications for edge cases:

    * If the attacker completely **vacated a region** to attack an adjacent region, defending units
      may *not* retreat to this region.
    * If the attacker is attacking **multiple regions**, it is possible that units could retreat to
      another region under attack. Healthy retreated units are allowed to participate in the
      following battle.

  The attacker moves all attacking units into the region. The invested coins in the conquered region
  may be kept on the board or may be (partly) stolen. If a token is present, the attacker may use it
  in a next command round after which the token returns to the defender.

(&#42;) When an enemy kills/wounds your unit, the choice of unit is determined by following
priorities:

* Healthy infantry
* Healthy artillery
* Wounded infantry
* Wounded artillery

### Trenches

When attacking a region that has a trench at the border the attacker is crossing, the defender has
advantages:

* Defending units cannot be wounded (only killed)
* The defender gets **2** dice for every healthy defending unit

### Fighting neutral regions

Neutral units will never attack, but do defend. The same rules apply as for normal combat. Whenever
a defender has to make a choice (e.g. retreat), the enemy team of the attacker may make that
decision.

# Coin trading

At any point in the game, you are allowed to give coins to another player.

*Examples:*

* *When an ally is struggling with paying their units*
* *When an ally wants to invest in a region but has no coins*

# Initial setup

## Apply scenario

Choose a [scenario](Scenarios.md) for the desired number of players *at random* and apply it.

## Coins

* Every player gets 2 coins in every region they own
* Every player gets 3 coins in their supply
* Every player gets command tokens:
    * Invest x 2
    * Dig trench x 1
    * Move x 3
    * Train units x 2

## Initial seeding

For every unoccupied region, roll a dice. If its result is:

* 1-3: Nothing happens
* 4-6: Add 1 coin
