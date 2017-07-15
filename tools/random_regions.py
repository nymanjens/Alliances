import random

NUM_NON_STRATEGIC_REGIONS = 4
ALLOWED_NUM_PLAYERS = {2, 4, 6}
DEFAULT_NUM_PLAYERS = 4

REGION_TO_PLAYER = {
  "England": "UK",
  "Russia": "Russia",
  "N-France": "France",
  "E-Germany": "Germany",
  "Turkey": "Ottoman Empire",
  "Hungary": "Austro-Hungary",
}
STRATEGIC_REGIONS_PER_TEAM = {
  "The Triple Entente": [
    "England",
    "N-France",
    "Russia",
  ],
  "Central players": [
    "E-Germany",
    "Turkey",
    "Hungary",
  ]
}
NON_STRATEGIC_REGIONS = [
  "Ireland",
  "Scotland",
  "Norway",
  "Denmark",
  "Finland",
  "Baltic States",
  "Ukraine",
  "Caucasus",
  "Middle East",
  "Egypt",
  "N-Africa",
  "Portugal",
  "Spain",
  "S-France",
  "Switzerland",
  "W-Germany",
  "Austria",
  "Bosnia",
  "Serbia",
  "Greece",
  "Bulgaria",
  "Romania",
  "Czechoslovakia",
]

class RegionGenerator:
  _already_chosen = set()

  def random_region(self, regions):
    region = random.choice([r for r in regions if r not in self._already_chosen])
    self._already_chosen.add(region)
    return region

def main():
  # num_players = raw_input("How many players are playing? [{}] ".format(DEFAULT_NUM_PLAYERS))
  # if not num_players:
  #   num_players = DEFAULT_NUM_PLAYERS
  # else:
  #   assert num_players.isdigit(), "{} is not a number".format(num_players)
  #   num_players = int(num_players)
  num_players = 4
  assert num_players in ALLOWED_NUM_PLAYERS

  region_generator = RegionGenerator()
  for team_name, strategic_regions in STRATEGIC_REGIONS_PER_TEAM.items():
    print "== {} ==".format(team_name)
    for _ in range(num_players // 2):
      strategic_region = region_generator.random_region(strategic_regions)
      non_strategic_regions = [
        region_generator.random_region(NON_STRATEGIC_REGIONS)
        for _ in range(NUM_NON_STRATEGIC_REGIONS)]
      player = REGION_TO_PLAYER[strategic_region]

      print "  Regions for {}:".format(player)
      print "    - {}*".format(strategic_region)
      for region in non_strategic_regions:
        print "    - {}".format(region)

    print

  print "(* strategic region)"
  print

if __name__ == '__main__':
  main()

