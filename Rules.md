# Definitions

* **Time:**
    * **Turn:** A single iteration of the game flow. There are a maximum of 10 turns in a game.
    * **Initial move command round order:** Player order: The game starts with the order below:
        * UK
        * Germany
        * Russia
        * Ottoman Empire
        * France
        * Austro-Hungarian Empire
* **Unit:** Military unit, either an infantry or an artillery
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
    * France (&#42;)
* Central players:
    * Germany
    * Ottoman Empire
    * Austro-Hungarian Empire (&#42;)

(&#42;) Neutral when playing with 4 players

# Goal of the game

One of:

1. At the end of a turn `n` (`n in {1..10}`), have at least a `11 - n` point advantage over the
   other team (ends the game)
1. If there is no winner after turn 10, the team with the most strategic cities wins. If these
   match, whichever side may call itself the victor. For in war, there are no winners, but all are
   losers.

# Playing a turn

All decisions below happen simultaneously (&#42;) unless stated otherwise.

1. **Command phase:**
    1. **Token assignment:** All players simultaneously put command tokens face down on regions
       they own.
    1. **Token revealing:** All tokens are turned face up
    1. **Bid for start player**: All players put a number of coins in their hand and reveal their
       bid simultaneously. The player bidding the most wins. In case of a tie, the tied player that
       came first in the last command round order wins. If this is the first turn, skip this step.

       The winner pays the bidded coins to the supply, becomes start player and chooses the
       direction of the move command round order. The full circle of the move command round order
       should always be the same as that of the initial move command round order.
    1. **Commands:** Resolve token types in following order:
        * **Invest and Dig trench**: Resolved simultaneously (&#42;)
        * **Move**: Resolved in move command round order
        * **Train units**: Resolved simultaneously (&#42;)
1. **Economic phase:**
    1. **Production:** All players receive the total amount of coins invested in regions they own,
       with a *minimum of 3*.
    1. **Payment:** All units in regions the player wants to keep, are paid 1/2 coins per
       infantry/artillery.
1. **Cleanup phase**
    1. **Mutiny:** All units which were not paid this turn, convert to neutral infantry units (i.e.
       artillery converts to neutral infantry). Neutral units in sea regions are removed from the
       board.
    1. **Unit healing:** All wounded units are healed
    1. **Point scoring:** Every team scores 1 point per strategic city they own (check game end
       condition)
    1. **Revival:** Any player with *a unit cost of less than 3 coins* gets free units of their
       choice. After revival, the total unit cost may not exceed 3 coins. New units must be placed
       at regions owned by the player. If that's impossible, the player may pick a *single
       unoccupied or sea region*.

       All added units must be payed immediately.
    1. **Advance turn counter** by one

(&#42;) Decisions are made simultaneously if possible. In case of a conflict, e.g. when a number of
players repetitively alter their decision in reaction to another player's decision, all players
whisper the solution to a player not involved who then executes the commands. When there is no such
player available, all write down their action and execute that action.

# Command tokens

Token types:

* **Invest**:<br>
  You may change the number of coins in this region.

  Coins are exchanged between the player's supply and the region on the board. The maximum number of
  coins that may be invested in the region is indicated on the map.

  This token is ignored in **sea regions**.

* **Dig trench**:<br>
  A single trench may be placed at a border with another land region that has a trench placeholder
  on the map.

  This token is ignored in **sea regions**.

* **Move**:<br>
  All healthy units in this region can move. Units can move separately to multiple regions.

  First, the player shows the other players all planned moves by moving units to their desired
  destinations in the desired order. Where necessary, battles are resolved in that order.

* **Train units**:<br>
    * In regions with a strategic city: +2 infantry or +1 artillery or upgrade 2 infantry to artillery
    * In other land regions: +1 infantry or upgrade 1 infantry to artillery
    * In sea regions: Nothing happens

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

### Raiding

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

When a move proceeds into an enemy region, the move ends and a battle is initiated with all moved
units.

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
1. **Attacker decides to retreat or has no healthy units left:** All units move back to the last
   touched unoccupied, sea or owned region.
1. **Defender decides to retreat or has no healthy units left:** All units (including wounded units)
   move to an adjacent land region that is unoccupied or owned by the defender.

  If no such regions are found, the units are killed. If there is choice, the defender may choose
  the region.

  Clarifications for edge cases:

    * If the attacker completely **vacated a region** to perform this attack, it could happen that
      the defending units retreat to this region.
    * If the attacker is attacking **multiple regions**, it is possible that units could retreat to
      another region under attack. Healthy retreated units are allowed to participate in the
      following battle.

  The attacker moves all attacking units into the region. The invested coins in the conquered region
  may be kept on the board or may be (partly) stolen. If a token is present, the attacker may use it
  in a next command round but the token returns to the defender at the end of the turn.

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

## General setup

### Coins

* Every player gets 2 coins in every region they own
* Every player gets 3 coins in their supply
* Every player gets command tokens:
    * Invest x 2
    * Dig trench x 1
    * Move x 3
    * Train units x 2

### Units per player

*(ignore the players that are not in the game)*

* **UK**
    * 2 infantry in England
    * 1 infantry in Scotland
* **Germany**
    * 2 infantry in E-Germany
    * 1 infantry in W-Germany
* **Russia**
    * 2 infantry in Russia
    * 1 infantry in Ukraine
* **Ottoman Empire**
    * 2 infantry in Turkey
    * 1 infantry in Middle East
* **France**
    * 2 infantry in N-France
    * 1 infantry in S-France
* **Austro-Hungarian Empire**
    * 2 infantry in Austria
    * 1 infantry in Hungary

### Initial seeding

For every unoccupied region, roll a dice. If its result is:

* 1-2: Nothing happens
* 3-4: Add 1 coin
* 5-6: Add 2 coins + neutral infantry

## 6 players

Add the following to the map:
<table>
  <tr>
    <th>Region</th>
    <th>Trenches</th>
  </tr>
  <tr>
    <td>N-France</td>
    <td>with border W-Germany</td>
  </tr>
  <tr>
    <td>W-Germany</td>
    <td>with border France</td>
  </tr>
</table>

## 4 players

This game is without the Austro-Hungarian Empire and France.

Add the following to the map:
<table>
  <tr>
    <th>Region</th>
    <th>Neutral infantry</th>
    <th>Coins</th>
    <th>Trenches</th>
  </tr>
  <tr>
    <td>N-France</td>
    <td>2</td>
    <td>3</td>
    <td>with border W-Germany</td>
  </tr>
  <tr>
    <td>Austria</td>
    <td>2</td>
    <td>3</td>
    <td>with border W-Germany</td>
  </tr>
  <tr>
    <td>Italy</td>
    <td>2</td>
    <td>2</td>
    <td></td>
  </tr>
  <tr>
    <td>N-Africa</td>
    <td>1</td>
    <td>2</td>
    <td></td>
  </tr>
</table>
