from pymongo import MongoClient
from fastapi import FastAPI
import validators



client = MongoClient('localhost', 27017)
db = client.xlab
collection = db.users


#validators ("user_phone")
def phone_validator(cls, phone):
        if not re.match("^(7+([0-9]){10})$", phone):
            raise HTTPException(
                detail=["Некорректное поле 'телефон'"],
                status_code=status.HTTP_400_BAD_REQUEST,
            )

app = FastAPI()


async def add_user(user_id: int, data: 'UserModel'):
    users_collection = database.get_collection("test_user_collection")
    user = await users_collection.find_one({"user_id":  user_id})

    if not user:
        data_to_mongo = {
            "user_id": user_id,
            "user_name": data.user_name,
            "user_phone": data.user_phone
        }
        users_collection.insert_one(data_to_mongo)
        return True

    else:
        result = users_collection.update_one(
            {"_id": user["_id"]},
            {"$set": {
                "user_name": data.user_phone,
                "user_phone": data.user_name
            }},
        )
        if result.modified_count < 0:
            return False
        return True


app.post("users/create_user")
async def create_user(
        user_id: int,
        data: 'UserModel',
):
    result = add_user(user_id, data)
    if result:
        return JSONResponse(
            "Данные успешно сохранены/изменены",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    else:
        return JSONResponse(
            {"detail": ["Ошибка создания/изменения"]},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
