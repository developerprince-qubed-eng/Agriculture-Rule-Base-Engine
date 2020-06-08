from random import choice
from pyknow import *


class Season(Fact):
    """Info about the Season patterns ."""
    pass


class FarmSeason(KnowledgeEngine):
    @Rule(Season(color='dry'))
    def dry_season(self):
        print("Rear Cattle or Livestock")

    @Rule(Season(color='wet'))
    def wet_season(self):
        print("Plant Wet Crops")

    @Rule(AS.season << Season(con=L('dry') | L('region5') | L('drought')))
    def cautious(self, season):
        if(season["con"] == 'region5'):
            print("Be cautious the we are now in", season["con"])
        if(season["con"] == 'drought'):
            print("Be cautious there is now", season["con"])
        else:
            print("Rear Cattle or Livestock")

    @Rule(AS.season << Season(con=L('wet') | L('rainy') | L('region1')))
    def cautious1(self, season):
        if(season["con"] == 'region1'):
            print("Be cautious we are now in", season["con"])
        if(season["con"] == 'wet'):
            print("Be cautious its now", season["con"])
        else:
            print("Plant Wet Crops")

def main():
    engine = FarmSeason()
    engine.reset()
    engine.declare(Season(con=choice(['wet', 'rainy', 'dry', 'region1'])))
    engine.run()

if __name__ == "__main__":
    main()