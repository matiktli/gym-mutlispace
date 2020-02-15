from gym_multispace.scenario import BaseScenario
from gym_multispace.core.entity import Agent, SpecialObject
from gym_multispace.core.world import World
import numpy as np


# Test scenario
class Scenario(BaseScenario):

    def generate_world(self):
        world = World()
        world.is_reward_shared = False
        world.is_discrete = True
        world.agents = [Agent()]
        world.special_objects = [SpecialObject()]

        for i, agent in enumerate(world.agents):
            agent.can_collide = False
            agent.can_grab = False
            agent.uuid = f'a_{i}'
            agent.view_range = np.inf

        for i, special_obj in enumerate(world.special_objects):
            special_obj.uuid = f'o_{i}'
            special_obj.can_collide = False

        return world

    def reset_world(self):
        raise NotImplementedError()

    def get_reward(self, agent, world):
        raise NotImplementedError()

    def get_observation(self, agent, world):
        raise NotImplementedError()