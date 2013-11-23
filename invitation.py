#!/shrini/nithya/marriage

"""
.. module:: invitation.shy
    :synopsis: We fell in love on each other by pushed by our parents
    :aim:: Get married
    :purpose:: Invite all of our friends

.. module authors:: Shrinivasan.T & Nithya.D
.. target date:: 31.10.2011

"""

from god import blessings
from friends import wishes, greetings, gifts, kindals, joyful, help, etc
from family.parents import Thanigachalam_Karpagam, Duraisamy_Indirany as appa_amma
from family.brothers import Arulalan_Suresh as rubber_thoppai
from family.sister import Nalini
from family.relations import *

class Love(love):

    def __init__(self, partner):
        self.__romance__(partner)
        self.__duet__(partner)
        self.__fight__(partner)

    def __romance__(self, partner):
        # Do romance for infinity times without any break
        while True:        
            # Make self to love partner
            self = do_love(partner)
            # Exchange our loves 
            self, partner = partner, self

    def __duet__(self, partner):
        self.songs_60s_to_90s(partner)

    def __fight__(self, partner):
        pass

class Marriage(Love, friends, parents, siblings, relativies):

    def __init__(self):
        self.time = " 6.00 am to 7.00 am "
        self.date = " 31-10-2011 "
        self.place = " Mohana Mahal, Little Kanchipuram "
        self.place += " Near by Tollgate "
        Love.do_marriage(arranged_by = parents, with_supports = siblings,
                          manage_by = relativies, with_love_of = friends)


class Reception(Love, friends):

    def __init__(self):        
        place = self.place
        self.party(You)

    def party(self, friends):
        # Celebrate happiness with you
        you = friends.best

        print " Reception Date ", " 30-10-2011 "
        print " Party Time ", " 6.30 pm to 9.30 pm "

        if you in Marriage:
            treat_to(you)
            photo_clips_with_us()

        elif you in Reception:
            party_to(you)
            photo_clips_with_us()

        else:
            fight_with(you)


def welcome(you):

    print " With Blessings of ", Love.love.angel

    print " We 'Shrinivasan Nithya' invite ", you, """ to our marriage and
                        reception with immense pleasure.
                      Your presence is most important to us.
            We are waiting for the moment to join with our life partner
               in front of our parents, brothers, relativies and most
                        importantly friends (you)... """

    print " We thank ", love.angel, " to tighed us together in this brith too "

    print " Once again welcome you to ", Marriage()
    print " and ", Reception(you), " too..."

    if you:
        print ":) :-) :P :D :} :-] :D :P :-) :) " * 10000000000000000000000000
    else:
        print ":( :-( :( :-( :=( :-{ :-[ :{ :(  " * 10000000000000000000000000


if __name__ == 'main':
    
    # Invitation begins here
    import love
    from mylife.partner import shyness, smile, love, happy, friendship, *
    from myself import shyness, smile
    from future import children
    
    welcome(invitation.cover.your_name)
