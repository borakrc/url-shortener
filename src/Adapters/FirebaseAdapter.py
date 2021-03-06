from google.cloud.firestore_v1 import DocumentReference, Client
from src.Adapters.IDbAdapter import IDbAdapter
from src.Exceptions.EmptyUserInformationError import EmptyUserInformationError
from src.Exceptions.UrlNotFoundError import UrlNotFoundError
from src.Models.EmailModel import EmailModel
from src.Models.UrlKeyModel import UrlKeyModel
from src.Models.UrlModel import UrlModel
from src.Models.UserModel import UserModel
from src.Models.UserModelFactory import UserModelFactory

class FirebaseAdapter(IDbAdapter):
    passwordSalt: str = None
    dbClient: Client = None

    def __init__(self, dbClient: Client, passwordSalt: str):
        self.passwordSalt: str = passwordSalt
        self.db = dbClient

    def getUser(self, email: EmailModel) -> UserModel:
        userDict: dict = self.db.collection('users').document(email.toString()).get().to_dict()
        if not userDict:
            raise EmptyUserInformationError

        user = UserModelFactory(self.passwordSalt).fromDict(userDict)

        return user

    def resolveShortUrl(self, shortUrl: UrlKeyModel) -> UrlModel:
        urlDict: dict = self.db.collection('urls').document(shortUrl.toString()).get().to_dict()
        if not urlDict:
            raise UrlNotFoundError

        url = UrlModel(urlDict['target'])

        return url

    def putShortUrl(self, shortUrl: UrlKeyModel) -> None:
        doc_ref: DocumentReference = self.db.collection('urls').document(shortUrl.toString())
        doc_ref.set({'target': shortUrl.targetUrl.toString()})
        return

    def putUser(self, user: UserModel) -> None:
        doc_ref: DocumentReference = self.db.collection('users').document(user.email.toString())
        doc_ref.set(user.toJson())
        return

    def authorizeUser(self, loginAttemptCredentials: UserModel) -> bool:
        user = self.getUser(loginAttemptCredentials.email)

        success: bool = user.compareCredentials(loginAttemptCredentials)
        return success

    def ifUserExists(self, email: EmailModel) -> bool:
        try:
            user = self.getUser(email)
        except EmptyUserInformationError as e:
            return False
        if user:
            return True
        return False
