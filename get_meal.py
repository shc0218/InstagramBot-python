import requests

class Meal:
    def __init__(self):
        return None
    def get_meal(self, key: str, city_code: str, school_code: str, date: str) -> dict:
        uri = (f"https://open.neis.go.kr/hub/mealServiceDietInfo"
               f"?KEY={key}"
               f"&Type=json"
               f"&ATPT_OFCDC_SC_CODE={city_code}"
               f"&SD_SCHUL_CODE={school_code}"
               f"&MMEAL_SC_CODE=2"
               f"&MLSV_YMD={date}")
        response = requests.get(uri)
        return self.__parser_meal(response.json())

    def __parser_meal(self, meal: dict) -> dict:
        res = {
            "meal_menu": [],
            "meal_allergy": []
        }
        allergy_list = ["난류", "우유", "메밀", "땅콩", "대두", "밀", "고등어", "게", "새우", "돼지고기", "복숭아", "토마토", "아황산류", "호두", "닭고기", "쇠고기", "오징어", "조개류(굴, 전복, 홍합 포함)", "잣"]
        if "mealServiceDietInfo" in meal.keys():
            meal_data = meal["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"]
            meal_data = meal_data.split("<br/>")
            for meal in meal_data:
                if len(meal.split(" ")) == 2:
                    meal_data_split = meal.split(" ")
                    meal_data_split[1] = str(meal_data_split[1]).replace("(","")
                    meal_data_split[1] = str(meal_data_split[1]).replace(")","")
                    for menu_allergy in meal_data_split[1].split("."):
                        if str(menu_allergy).isdecimal():
                            if allergy_list[int(menu_allergy) - 1] not in res["meal_allergy"]:
                                res["meal_allergy"].append(allergy_list[int(menu_allergy) - 1])
                res["meal_menu"].append(meal.split(" ")[0])

            return res