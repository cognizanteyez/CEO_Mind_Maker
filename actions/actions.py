from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionProvideCustomInfo(Action):
    def name(self) -> Text:
        return "action_provide_custom_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        metric = next(tracker.get_latest_entity_values("metric"), None)
        response = ""

        if metric:
            # Mock data retrieval based on the metric
            if metric == "sales":
                response = "Sales have increased by 15% this quarter."
            elif metric == "customer satisfaction":
                response = "Customer satisfaction has improved with a 90% satisfaction rate."
            elif metric == "revenue":
                response = "Revenue is up by 20% compared to last quarter."
            elif metric == "performance":
                response = "Overall performance metrics are showing positive trends in productivity."
            elif metric == "product launches":
                response = "We successfully launched three new products this month, all receiving positive feedback."
            elif metric == "market share":
                response = "Our market share has increased to 25% in the current industry segment."
            else:
                response = f"Currently, we do not have specific data on {metric}."

            dispatcher.utter_message(text=response)
        else:
            dispatcher.utter_message(text="I'm not sure which metric you're interested in. Please specify.")

        return []



class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="I'm not sure how to help with that. Can you clarify?")
        return []
