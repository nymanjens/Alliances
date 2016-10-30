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
* **Unit:** Military unit, either a soldier or an artillery
    * **Wounded unit:** Acts like a normal unit, except that it has zero defence/attack and can't
      move.
    * **MP:** move point
    * **Troop:** Group of units
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
        * Artillery: 6
    * Command tokens:
        * Invest: 2
        * Dig trench: 1
        * Move: 3
        * Train troops: 2
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
    * Austro-Hungarian Empire (&#42;&#42;)

(&#42;) Neutral when playing with 4 players<br />
(&#42;&#42;) Neutral when playing with 4 or 5 players

# Goal of the game
One of:

1. At the end of a turn, have at least a 10 point advantage over the other team (ends the game)
1. Get your team to score the most points at the end of turn 10

# Playing a turn

All decisions below happen simultaneously (&#42;) unless stated otherwise.

1. **Command phase:**
    1. **Token assignment:** All players simultaneously put command tokens face down on regions
       they own.
    1. **Token revealing:** All tokens are turned face up
    1. **Commands:** Resolve token types in following order:
        * **Invest and Dig trench**: Resolved simultaneously (&#42;)
        * **Move**: Resolved in move command round order
        * **Train troops**: Resolved simultaneously (&#42;)
1. **Economic phase:**
    1. **Production:** All players receive the total amount of coins invested in regions they own,
       with a *minimum of 3*.
    1. **Payment:** All units in regions the player wants to keep, are paid one coin per unit.
        * After paying the units, coins can be given to allied players, which they can use to pay
          for their units.
1. **Cleanup phase**
    1. **Mutiny:** All units which were not paid this turn, convert to neutral infantry units (i.e.
       artillery converts to neutral infantry).
    1. **Unit healing:** All wounded units are healed
    1. **Point scoring:** Every team scores 1 point per strategic city they own (check game end
       condition)
    1. **Revival:** Any player with *less than 3 units* on the board gets free units of their choice
       until they have a total of 3 units on the board. New units must be placed at regions owned by
       the player. If that's impossible, the player may pick a *single unoccupied or sea region*.
    1. **Advance turn counter** by one

(&#42;) Decisions are made simultaneously if possible. In case of a conflict, e.g. when a number of
players repetitively alter their decision in reaction to another player's decision, all players
whisper the solution to a player not involved who then executes the commands. When there is no such
player available, all write down their action and execute that action.

# Command tokens
Token types:
* **Invest**:<br>
  Invest any amount (0-inf) in this region.

  Investing means that coins go from the player's supply on to the board. The maximum number of
  coins that may be invested in the region is indicated on the map.

  This token is ignored in **sea regions**.

* **Dig trench**:<br>
  A single trench may be placed at a border with another land region that has a trench placeholder
  on the map.

  This token is ignored in **sea regions**.

* **Move**:<br>
  All troops in this region get 2 MP. Units can move separately to multiple regions.

  First, the player shows the other players all planned moves by moving units to their desired
  destinations in the desired order. Where necessary, battles are resolved in that order.

* **Train troops**:<br>
  * +2 units in regions with a strategic city<br>
  * +1 unit in other land regions<br>
  * Does nothing in sea regions

  The player may choose the type of units, which are added to this region.

  Note: The unit has to be paid later that turn.

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
Troops can end their move in sea regions, unoccupied regions, enemy regions, neutral regions or
regions owned by the same player. Troops can't end in friendly regions owned by other players.

If a unit's move ends in a previously unoccupied region, invested coins may be (partly) stolen.

### Sea regions
Troops of different teams can reside in the same sea region simultaneously.

**Artillery** units are not allowed to move to sea regions.

### Ambiguous crossings
The following points on the map can be crossed both by land-land and sea-sea movement:

* **Denmark islands**
* **English Channel**
* **Gibraltar**
* **Istanbul**

Sea-sea movement is not possible for a unit if both land regions at the crossing are enemy regions.

## Battles
When a move proceeds into an enemy region, the move ends and a battle is initiated with all moved
units.

### Battle mechanic
A battle has one or more rounds. Every round has following parts:

1. **Rolling dice:**
    * Attacker gets a dice for every healthy attacking **unit** (infantry + artillery)
    * Defender gets a dice for every healthy defending **infantry unit**
    * Every roll of:
        * **3 or 4:** Wounds an enemy infanthy
        * **5 or 6:** Kills an enemy infanthy
1. **Attacker decides to retreat or has no healthy infantry left:** All units move back to the last
   touched unoccupied, sea or owned region.
1. **Defender decides to retreat or has no healthy infantry left:** All defender artillery is
   killed, all infantry moves to (in mandatory order of possibility):
    * An adjacent region owned by the defender
    * An adjacent unoccupied region
    * The above, but moving through as few as possible friendly regions

  If none of the above are found, the unit is killed. If there is choice, the defender may choose
  the region.

  The attacker moves all attacking units into the region (including artillery). The invested coins
  may be kept on the board or may be (partly) stolen.

*Example: If the attacker engages with only artillery, the attacker will get a chance of wounding or
killing enemy infantry without risk of losing their own units. The battle ends automatically **in
part 2** and the artillery retreats.*

### Trenches
When attacking a region that has a trench at the border the attacker is crossing, the defender has
advantages:
* Attacking **infantry** need 2 rolls >= 3 for wounded, 2 rolls >= 5 for kill
* Defender gets twice the amount of dice per defending infantry

*Clarification: This means attacking artillery follow normal combat rules (1 roll for
wounding/killing). Artillery and infantry dice should thus be rolled separately.*

### Fighting neutral regions
Neutral units will never attack, but do defend. The same rules apply as for normal combat. Whenever
a defender has to make a choice (e.g. retreat), the enemy team of the attacker may make that
decision.

# Special abilities of players
* **UK**: Owns the seas
    * UK units get 3 MP from the move token if the move starts in the England, Scotland or Ireland
      region
* **Germany**: Autobahn
    * German units get 3 MP from the move token if the regions touched by the move except for the
      last are friendly.
* **Russia**: Burning retreat
    * When losing a region, choose to destroy all or some coins
* **Ottoman Empire**: Cosmopolitans
    * When moving into neutral or conquered region without coins, a free coin is invested
* **France**: Diggers
    * May build 2 trenches per resolved command token
* **Austro-Hungarian Empire**: Bankers
    * Gains 1 coin when resolving invest token on a land region

# Initial setup
## 6 players
**Coins:**
* Every player gets 2 coins in every region they own
* Every player gets 3 coins in their supply

**Trenches:**
* Between N-France and W-Germany on both sides

**Troops**
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
    * 2 infantry in S-France
    * 1 infantry in N-France
* **Austro-Hungarian Empire**
    * 2 infantry in Hungary
    * 1 infantry in Austria

## 5 players
Note: This game has to be played with the uncertain allegiance extension, except only for the allied
players and with half the USA reinforcements.

Same setup as  6 players, except:

**Troops and other trenches:**
* **Austro-Hungarian Empire** (neutral):
<table>
  <tr>
    <th>Region</th>
    <th>Infantry</th>
    <th>Coins</th>
    <th>Trenches</th>
  </tr>
  <tr>
    <td>Austria</td>
    <td>3</td>
    <td>3</td>
    <td>with border W-Germany</td>
  </tr>
  <tr>
    <td>Hungary</td>
    <td>3</td>
    <td>3</td>
    <td></td>
  </tr>
  <tr>
    <td>Romania</td>
    <td>4</td>
    <td>3</td>
    <td>with border Ukraine</td>
  </tr>
  <tr>
    <td>Yugoslavia</td>
    <td>1</td>
    <td>1</td>
    <td></td>
  </tr>
  <tr>
    <td>Bulgaria</td>
    <td>4</td>
    <td>3</td>
    <td>with border Turkey</td>
  </tr>
</table>

## 4 players
Same setup as  5 players, except:

**Troops and other trenches:**
* **France** (neutral):
<table>
  <tr>
    <th>Region</th>
    <th>Infantry</th>
    <th>Coins</th>
    <th>Trenches</th>
  </tr>
  <tr>
    <td>N-France</td>
    <td>4</td>
    <td>4</td>
    <td>with border W-Germany</td>
  </tr>
  <tr>
    <td>S-France</td>
    <td>3</td>
    <td>3</td>
    <td></td>
  </tr>
  <tr>
    <td>Spain</td>
    <td>3</td>
    <td>3</td>
    <td>with border Ukraine</td>
  </tr>
  <tr>
    <td>Portugal</td>
    <td>2</td>
    <td>2</td>
    <td></td>
  </tr>
  <tr>
    <td>Morocco</td>
    <td>2</td>
    <td>2</td>
    <td>with border Turkey</td>
  </tr>
</table>

# Uncertain allegiance extension
At the beginning of the game, every player gets a card. One card symbolizes the "mole". This player
can only win if the opposing side wins.

## Discovery
**At the end of every turn** (after the cleanup phase), both teams get the opportunity (first
allies, then central) to call out a single team member to show their card. From the next turn
onwards, the mole will become a member of the opposing team and USA will send reinforcements to the
leftover members.

The mole may also **attack an ally**, which immediately changes their official allegiance and causes
the USA to enter the war immediately. The mole shows their card.

Note: After discovery, scored points for the strategic cities of the mole are scored for the mole's
new team.

## USA
**Troops:** At the start of every turn (before the command phase), each supported player gets a
number of units (see table below). The recipient may choose the type of unit and may pick a
region owned by the recipient for the units to appear in. If the recipient owns no regions,
the units appear in the North Sea or Atlantic Ocean.

**Coins:** At the start of the economic phase, each supported player receives  a number of coins
(see table below).
<table>
  <tr>
    <td></td>
    <th>1 shown card</th>
    <th>2+ shown cards</th>
  </tr>
  <tr>
    <th>Units</th>
    <td>4</td>
    <td>3</td>
  </tr>
  <tr>
    <th>Coins</th>
    <td>12</td>
    <td>7</td>
  </tr>
</table>
