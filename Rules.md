# Definitions
* **Time:**
    * **Turn:** Contains among others multiple command token rounds. There are a maximum of 15 turns
      in a game.
    * **(Command token) round:** A single iteration in round order where all players can play a
      single command token
    * **Round order:** Player order: Starts with the order below and shifts every turn (first player
      becomes last player every turn):
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
    * **Sea region:** Region that contains mostly of a water body (the inverse of land regions)
    * **Occupied region:** Land region with at least one military unit
    * **Neutral region:** Either a region without any units or a sea region
    * **Conquered region:** Region won after successful battle earlier in the current round. This
      excludes neutral regions occupied by retreated units.
    * **Friendly region:** Region owned by you or your allies (the inverse of enemy regions)

# Teams
There are 2 teams:
* Allied powers:
    * UK
    * Russia
    * France (&#42;)
* Central powers:
    * Germany
    * Ottoman Empire
    * Austro-Hungarian Empire (&#42;&#42;)

(&#42;) Neutral power when playing with 4 players<br />
(&#42;&#42;) Neutral power when playing with 4 or 5 players

# Goal of the game
One of:

1. At the end of a turn, have at least a 15 point advantage over the other team (ends the game)
1. Get your team to score the most points at the end of turn 15

# Playing a turn
1. **Command phase:**
    1. **Token assignment:** All players simultaneously put command tokens face down on occupied
       regions
    1. **Token revealing:** All tokens are turned face up
    1. **Rounds:** For every token type: Until all command tokens of that type are removed from the
       board, every player plays a single command token in round order.<br>
       Command token types are resolved in this order:
        * Invest
        * Dig trench
        * Move
        * Train troops
1. **Economic phase:**
    1. **Production:** All occupied regions produce the amount of coins invested
    1. **Payment:** Units in regions the player wants to keep, are paid one coin per unit
        * After paying the units, money can be given to allies, which they can use to pay for their
        units.
    1. **Mutiny** Countries with units which were not paid this round, convert to neutral forces.
1. **Cleanup phase**
    1. **Point scoring:** Every team scores 1 point per occupied strategic city (check game end
       condition)
    1. **Unit healing:** All wounded units are healed
    1. **Advance turn counter** by one

# Command tokens
Token types:
* **Invest** (x 2):<br>
  Receive 2 coins and invest any amount (0-inf) in this region.

  Investing means that coins go from the player's supply on to the board. The maximum number of
  coins that may be invested in the region is indicated on the map.

  This token is ignored in **sea regions**, i.e. no coins can be received/invested in sea regions.

* **Dig trench** (x 1):<br>
  A single trench may be placed at a border with another land region that has a trench placeholder
  on the map.

* **Move** (x 3):<br>
  All troops in this region get 2 MP. Units can move separately to multiple regions, but only one
  region can be battled.

* **Train troops** (x 2):<br>
  * +2 units in regions with a strategic city<br>
  * +1 unit in other land regions<br>
  * Does nothing in sea regions

  The player may choose the type of units, which are added to this region.

  Note: The unit has to be paid later that turn.

## Moving units
Units can move through neutral, friendly and sea regions. Moving to an enemy region consumes all
Move Points and initiates a battle.

### Move Points (MP)
Moves between regions normally cost 2 MP.<br>
Moves starting in a friendly region with at least one coin invested cost 1 MP.<br>
The total amount of MP consumed may never exceed the given amount (typically 2).

*Example: My infantry gets 2 MP. When entering sea from my region with 2 coins, 1 MP is consumed,
but the sea isn't friendly region so I can't move any further. The remaining 1 MP gets lost.*

### Ending move
Troops can end their move in conquered, neutral or owned regions. Troops can't end in foreign
(friendly) regions.

### Sea regions
Sea regions are **always neutral** and troops of different teams can thus reside in the same region
simultaneously.

**Artillery** units are not allowed to move to sea regions.

### Ambiguous crossings
The following points on the map can be crossed both by land-land and sea-sea movement:

* **Denmark islands**
* **Gibraltar**
* **Istanbul**

Sea-sea movement is not possible if both land regions at the crossing are controlled by an enemy power.

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
   touched region not owned by a foreign power
1. **Attacker decides to retreat or has no healthy infantry left:** All defender artillery is
   killed, all infantry moves to (in mandatory order of possibility):
    * An adjacent owned region
    * An adjacent neutral land region
    * The above, but moving through as few as possible friendly regions
  
  If none of the above are found, the unit is killed. If there is choice, the defender may choose the
  region.

  The attacker moves all attacking units into the region (including artillery). The coins present
  may be kept on the board or may be removed.

*Example: If the attacker engages with only artillery, the attacker will get a chance of wounding or
killing enemy infantry without risk of losing their own units. The battle ends automatically **in
part 2 **and the artillery retreats.*

### Trenches
When attacking a region that has a trench at the border the attacker is crossing, the defender has
advantages:
* Attacker needs 2 rolls >= 3 for wounded, 2 rolls >= 5 for kill
* Defender gets twice the amount of dice per defending infantry

### Fighting neutral powers
Neutral powers don't attack, but do defend. The same rules apply as for normal combat. Whenever a
defender has to make a choice (e.g. retreat), the other team may make that decision.


# Special abilities of powers
* **UK**: Owns the seas
    * UK units get 3 MP from the move token if the move starts in the UK or Ireland region
* **Germany**: Autobahn
    * German units get 3 MP from the move token if the move only touches German regions
* **Russia**: Burning retreat
    * When losing a territory, choose to destroy all or some coins
* **Ottoman Empire**: Cosmopolitans
    * When moving into neutral or conquered territory without coins, a free coin is invested
* **France**: Diggers
    * May build 2 trenches per resolved command token
* **Austro-Hungarian Empire**: Bankers
    * Gains 3 coins when resolving invest token

# Initial setup
## 6 players
**Money:**
* Every player gets 2 coins in every owned region
* Every player gets 3 coins in their supply

**Trenches:**
* Between N-France and W-Germany on both sides
* At coast of W-Germany

**Troops**
* **UK**
    * 2 infantry in UK
    * 1 infantry in Ireland
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
powers and with half the USA reinforcements.

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
number of units (see table below). The recipient may choose the type of unit and may pick an owned
region for the units to appear in. If the recipient owns no territories, the units appear in the
North Sea or Atlantic Ocean.

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
