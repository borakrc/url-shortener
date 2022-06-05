from src.Models.UserModel import UserModel
from src.Models.UserModelFactory import UserModelFactory


def generate(config) -> UserModel:
    return UserModelFactory(config).fromDict({'email': 'mockEmail', 'password': 'MockPassword'})
