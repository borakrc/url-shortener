from flask_restful import Resource
from flask import make_response, jsonify

class FirestoreTestController(Resource):
    def __init__(self):
        pass

    def get(self):
        res = self.firestoreTestQuery()

        return make_response(jsonify(res), 200)

    def firestoreTestQuery(self):
        from google.cloud import firestore
        import os
        from dotenv import load_dotenv

        load_dotenv()
        os.getenv('MY_ENV_VAR')

        db = firestore.Client.from_service_account_info({
            "project_id": os.getenv('project_id'),
            "private_key": os.getenv('private_key'),
            "client_email": os.getenv('client_email'),
            "token_uri": os.getenv('token_uri'),
        })

        # Add a new document
        doc_ref = db.collection(u'users').document(u'johndoe')
        doc_ref.set({
            u'first': u'John',
            u'last': u'Doe',
        })

        # Then query for documents
        users_ref = db.collection(u'users')

        response = []
        for doc in users_ref.stream():
            response.append(u'{} => {}'.format(doc.id, doc.to_dict()))

        print(response)
        return response
