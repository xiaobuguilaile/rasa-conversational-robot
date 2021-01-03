# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class MakeupForm(FormAction):

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "makeup_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["brand", "category", "product"]

    def submit(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ):
        """Define what the form has to do after all required slots are filled"""
        brand = tracker.get_slot('brand')
        category = tracker.get_slot('category')
        product = tracker.get_slot('product')

        brand_product_map = get_product_brand_map()
        brand_category_map = get_product_category_map()

        pass


def get_product_brand_map():
    """ 获取 brand 和 product 的 映射 dict"""

    pass


def get_product_category_map():
    """ 获取 brand 和 category 的 映射 dict"""

    pass


