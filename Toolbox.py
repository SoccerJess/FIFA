# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 17:21:26 2017

@author: 3415756
"""

from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import settings
from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation
from soccersimulator.gui import SimuGUI,show_state,show_simu
import math

#Toolbox

class Position(object):
    def __init__(self, state, id_team, id_player):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player
        
    def mon_but(self):        
        return Vector2D(0, settings.GAME_HEIGHT/2)
    
    def but_adv(self):
        return Vector2D(settings.GAME_WIDTH, settings.GAME_HEIGHT/2)
    
    def my_position(self):
        return self.state.player_state(self.id_team, self.id_player).position
    
    def ball_position(self):
        return self.state.ball.position
    
    def zone_tir(self):
        return settings.PLAYER_RADIUS + settings.BALL_RADIUS
        
###############################################################################
        
class Deplacement(Position):
    def aller(self, p):
        return SoccerAction(p-self.my_position(), Vector2D())
    
#    def allervballe(self, p):
#        return SoccerAction(p-self.my_position(), Vector)
        
###############################################################################
        
class ActionOffensive(Deplacement):
        def shoot(self, p):
            return SoccerAction(Vector2D(), 0.1 * (p-self.my_position()))
            
        def dribbler(self):
            if (self.ball_position() - self.my_position()).norm <= self.zone_tir() and self.state.ball.position.x > settings.GAME_WIDTH - 30:
                return self.shoot(self.but_adv())
#                return SoccerAction(self.ball_position() - self.my_position(), Vector2D(1,-1))
            else:
              return self.aller(self.ball_position()) + self.shoot(self.my_position() + Vector2D(1, 0))