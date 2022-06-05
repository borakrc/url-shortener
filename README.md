# url-shortener

## How to deploy

### 1- Setup a database for the app on Google Cloud
This project uses Google Firestore to keep all of its non-volatile data. This includes shortened links and user information.

#### 1.1. Select or create a Google Cloud Platform project.
By going to https://console.cloud.google.com/project

#### 1.2. Enable the Google Cloud Firestore API.`_
By going to https://console.cloud.google.com/firestore

#### 1.3. Create a service account and download Json Keyfile
Go to project settings, click on 'Service Account', create a new service account and give it 
permissions to the firestore project. Then create a new private key for that service account 
and download the JSON keyfile. This file contains the credentials for the database. We will 
need this file when giving our API access to a db.

### 2- Setup the project to your local

We're doing this on our local so that we can add the db credentials to the serverless envs easily. 
Alternatively, you can use Vercel console to do the following steps, but this is not expained here.

#### 2.1. Install python3 and npm if you don't have

#### 2.2. Clone the repo to your local
Go to the directory where you want to clone the repo and run the following command:
```bash
$ git clone https://github.com/borakrc/url-shortener.git
```

#### 2.3. (Optional) Install requirements
If you want to run this project on your local, run the following command on project directory. 
You might want to create a venv before installing them, so that the packages are not installed globally.
```bash
$ pip install -r requirements.txt
```

#### 2.4. Install Vercel CLI
Vercel is a serverless cloud. Install the CLI so that you can create an account, a project and upload secrets to the project envs.
```bash
$ npm i -g vercel
```


#### 2.5. Create an account and project
Run the command below and follow the steps on the CLI. After this is done, you'll have an account on Vercel and a new cloud project.
```bash
$ vercel
```

#### 2.6. Download the .env file from Vercel
Run the command below on the project root. This will create a file named `.env`:
```bash
$ vercel env pull
```


#### 2.7. Populate the .env file with Firestore credentials
Remember the JSON keyfile we downloaded from Google Cloud? Open it, copy the contents of it without the curly brackets. 
Then paste it into the .env file on your project root.

#### 2.8. Generate a random JWT secret and a random password salt
Since JWTs are not signed using asymmetric encryption you do not have to generate your secret key using ssh-keygen.
Go to the .env file at project root and assign `JWT_SECRET` field to a long, random string.
You can go to https://www.grc.com/passwords.htm and use the alpha-numeric one to generate a secure secret.
Generate and setup another for the `PASSWORD_HASH_SALT` field as well. This is for adding salt to the password before
hashing it. See https://en.wikipedia.org/wiki/Salt_(cryptography)

#### 2.9. Upload modified .env file to vercel
Just run `vercel`. This will upload the envs to the serverless project. 
One of the URIs on your console after it is uploaded is a functional deployment of this project,
the other one is a link to the serverless portal page of the project.

## Assumptions
- Url will not be deleted, modified or expire once created.
- User will not be deleted or modified once created.
- System gives a login token when user registers.
- System does not verify the validity of URLs.
- JWT tokens do not expire.
- Short URLs will not be owned by a user. 
If two users create a short version of the same URL, they will share the short URL.
- Once registered, users will not forget their passwords or change their emails.
- Users can not logout.
- Users do not need to provide a valid token to consume a short url.

## Further work
Analytics
Logging and error monitoring
Allow user to create custom short urls
By creating the JWT token with an asymmetric key, we can broadcast our public key and 
provide others verify the validation of our tokens. This will provide scalability.

