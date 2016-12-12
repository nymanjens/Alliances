# Definitions

* **Time:**
    * **Turn:** A single iteration of the game flow. There are a maximum of 10 turns in a game.
    * **Move command round order:** Player order: Starts with the order below and shifts every turn
      (first player becomes last player every turn):
        * UK
        * Germany
        * Russia
        * Ottoman Empire
        * France
        * Austro-Hungarian Empire
* **Unit:** Military unit, either an infantry or an artillery
    * **Wounded unit:** Acts like a normal unit, except that it has zero defence/attack and can't
      move (but it can retreat).
    * **MP:** move point
* **Strategic city:** Star on the map
* **Players**
    * **Nominal ally:** Other player in the same team
    * **Nominal enemy:** Any player in a different team
    * **Enemy player:** Any player that is either:
        1. A nominal enemy
        1. A nominal ally that has explicitly indicated to be a (temporary) enemy (this can be done
           at any time)
        1. A nominal ally that you have explicitly indicated to be a (temporary) enemy of (this can
           be done at any time)
    * **Actual ally:** A nominal ally that is not an enemy
* **Regions:** Region on the map bounded by white lines
    * **Sea region:** Region that consists mostly of a water body (the inverse of land regions)
    * **Land region:** Region that consists mostly of land (the inverse of sea regions)
    * **Occupied region:** Land region occupied by at least one military unit
    * **Unoccupied region:** Land region not occupied by any military units
    * **Neutral region:** Land region occupied by neutral units
    * **Region owned by a player:** Land region occupied by units of that player
    * **Friendly region for a player:** Land region occupied by units of that player, or
      units of an actual ally of that player
    * **Enemy region for a player:** Land region occupied by neutral units, or units of an enemy
      of that player
    * **Conquered region:** Land region won after successful battle earlier during the current
      command. This excludes previously unoccupied regions now occupied by retreated units.

# Contents of the game

* **Per player:**
    * Units:
        * Infantry: 14
        * Artillery: 5
* **Per team:**
    * Command tokens:
        * Invest: 2 x *number of players in team*
        * Dig trench: 1 x *number of players in team*
        * Move: 3 x *number of players in team*
        * Train units: 2 x *number of players in team*
* **General:**
    * Coins: infinite
    * Neutral infantry: infinite

# Teams

There are 2 teams:

* Allied players:
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

1. At the end of a turn, have at least a 7 point advantage over the other team (ends the game)
1. Get your team to score the most points at the end of turn 10
1. Have 5 (6 players) or 7 (4 players) strategic cities at any point in the game to win individually

   **In case of a tie:** The team with the most coins on board wins. If these match, the team
   with the highest unit cost, wins. If these match, everybody loses.

# Playing a turn

All decisions below happen simultaneously (&#42;) unless stated otherwise.

1. **Command phase:**
    1. **Token assignment:** All players simultaneously put command tokens face down on regions
       they own.
    1. **Token and coin trading:** All players can trade unused command tokens and coins among each
       other
    1. **Token revealing:** All tokens are turned face up
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
  All healthy units in this region get 2 MP. Units can move separately to multiple regions.

  First, the player shows the other players all planned moves by moving units to their desired
  destinations in the desired order. Where necessary, battles are resolved in that order.

* **Train units**:<br>
    * In regions with a strategic city: +2 infantry or +1 artillery or upgrade 2 infantry to artillery
    * In other land regions: +1 infantry or upgrade 1 infantry to artillery
    * In sea regions: Nothing happens

## Moving units

Units can move through unoccupied, friendly and sea regions. Moving to an enemy region consumes all
Move Points and initiates a battle.

### Move Points (MP)

Moves between regions normally cost 2 MP.<br>
Moves starting in a friendly region with at least one coin invested cost 1 MP.<br>
The total amount of MP consumed may never exceed the given amount (typically 2).

*Example: My infantry gets 2 MP. When entering sea from my region with 2 coins, 1 MP is consumed,
but the sea isn't a friendly region so I can't move any further. The remaining 1 MP gets lost.*

### Ending move

Units can end their move in sea regions, unoccupied regions, enemy regions, neutral regions or
regions owned by the same player. Units can't end in friendly regions owned by other players.

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

Sea-sea movement is not possible for a unit if both land regions at the crossing are neutral regions
or regions of a nominal enemy.

### Friendly fire

Nominal allies can become enemies at any moment, leading to edge cases:

* **Battle nominal ally:** Ending a move in the territory of a nominal ally triggers a battle. This
  move may not have relied on the same player being an ally (e.g. no moving through the soon-to-be
  enemy's territory).
* **Moving through territory:** When units move through your territory, you can stop them from
  passing through. This automatically starts a fight between the units passing through and the units
  in your territory.
* **Retreating through territory:** (Following existing rules) Nominal allies can prevent a retreat
  from going through their territory.
* **Moving through ambiguous crossing:** You cannot block allies from crossing ambiguous crossing
  via the sea.

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
1. **Attacker decides to retreat or has no healthy units left:** All units move back to the last
   touched unoccupied, sea or owned region.
1. **Defender decides to retreat or has no healthy units left:** All units (including wounded units)
   move to (in mandatory order of possibility):
    * An adjacent region owned by the defender
    * An adjacent unoccupied region
    * The above, but moving through as few as possible friendly regions

  If none of the above are found, the units are killed. If there is choice, the defender may choose
  the region.

  Note that if the attacker completely vacated a region to perform this attack, it could happen
  that the defending units retreat to this region.

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
* Attacking infantry need 2 rolls >= 5 for kill

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
