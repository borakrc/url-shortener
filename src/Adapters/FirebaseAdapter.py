import os
from google.cloud import firestore
from google.cloud.firestore_v1 import DocumentReference
from src.Adapters.IDbAdapter import IDbAdapter
from src.Exceptions.EmptyUserInformationError import EmptyUserInformationError
from src.Models.EmailModel import EmailModel
from src.Models.UserModel import UserModel
from src.Models.UserModelFactory import UserModelFactory

class FirebaseAdapter(IDbAdapter):
    config = None

    def __init__(self, config):
        self.config = config
        self.db = firestore.Client.from_service_account_info({
            "project_id": os.getenv('project_id'),
            "private_key": os.getenv('private_key'),
            "client_email": os.getenv('client_email'),
            "token_uri": os.getenv('token_uri'),
        })

    def getUser(self, email: EmailModel) -> UserModel:
        userDict: dict = self.db.collection('users').document(email.toString()).get().to_dict()
        if not userDict:
            raise EmptyUserInformationError

        user = UserModelFactory(self.config).fromDict(userDict)

        return user

    def putUser(self, user: UserModel) -> None:
        doc_ref: DocumentReference = self.db.collection('users').document(user.email.toString())
        doc_ref.set(user.toJson())
        return

    def ifUserExists(self, email: EmailModel) -> bool:
        try:
            user = self.getUser(email)
        except EmptyUserInformationError as e:
            return False
        if user:
            return True
        return False
