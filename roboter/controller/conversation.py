"""Controller for speaking with robot"""
from roboter.models import robot


def talk_about_restaurant():
    """Function to speak with robot"""
    restaurant_robot = robot.RestaurantRobot()
    restaurant_robot.hello()
    restaurant_robot.recommend_restaurant()
    restaurant_robot.ask_user_favorite()
    restaurant_robot.thank_you()

def talk_about_travel():
    """Function to speak with robot about travel"""
    travel_robot = robot.TravelRobot()
    travel_robot.hello()
    travel_robot.recommend_travel_place()
    travel_robot.ask_user_favorite_place()
    travel_robot.thank_you()