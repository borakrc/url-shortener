# url-shortener

## Solution description
This project is a url shortener. It supports user signup, login and redirection from short urls to their target.
It is deployed to a serverless cloud called Vercel, which communicates with Google Firestore.

## Endpoints
### /api/v1/signup
Methods: [POST]
- Example url: https://url-shortener-borakrc.vercel.app/api/v1/signup
- Headers: {}
- Body: {email: string, password: string}
- Returns: {success: 'true'}, 200 or 409

### /api/v1/login
- Methods: [POST]
- Example url: https://url-shortener-borakrc.vercel.app/api/v1/login
- Headers: {}
- Body: {email: string, password: string}
- Returns: {jwtToken: string}, 200 or 401

### /api/v1/shortenUrl
- Methods: [PUT]
- Example url: https://url-shortener-borakrc.vercel.app/api/v1/shortenUrl
- Headers: {x-access-tokens: jwtToken}
- Body: {longUrl: string}
- Returns: {shortUrl: string}, 200 or 401

### /\<shortUrl>
- Methods: [GET]
- Example url: https://url-shortener-borakrc.vercel.app/zOog
- Headers: {}
- Returns: 302 or 404

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

#### 2.6. Create an .env file
You can rename `.env.example` to `.env`.

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

#### 2.10. (Optional) Run tests
To run all tests, use
```bash
$ python -m unittest discover ./Tests
```

## Technical choices and architecture, Trade-offs
This app consists a user registration, user login, url shortener and short url redirector.
It uses Google Firestore as the database. 
The recommended deployment is to a serverless cloud called Vercel.
The app deployed to Vercel is stateless. 
User sends http requests to this API and gets either a Json response or a 302 redirect response.
During user registration, passwords are hashed with bcrypt. 
To give users a login token, JWT is used.

To shorten the urls, it generates a hash of length 4 based on the url.
If it is a duplicate hash that already exists in the database, it retries longer string lengths.
The hash consists characters in the range within [a-z][A-Z][0-9].

### Deployment
This app is deployed to Vercel, a serverless cloud. 
Vercel is built by the creators of next.js, which is a modern js backend framework.
It is very scalable, easy to use and compatible with many backend frameworks.
I believe it's useful when the developer is given limited time, and it was hardly the bottleneck in this project.

### Database
Google Firestore is used to store non-volatile state of the data.
It is a very scalable, self maintaining, fun and easy to use document database. 
This db also gave me the opportunity to build the entire app without a single WHERE statement, which is quite a peace of mind.

Some assumptions below limits some potential features, such as users owning a short url or removing one.
Adding these features in the future will require changes to the db model 
and Firestore is one of the easiest databases to do that.

### Generation of short url
There are many ways to generate a short url. I generated them using first 4 characters of a hash based on the long url.
The app is checking if that 4-character hash already exists in the db. 
If it does, it tries a 5-character hash, and so on.

The downside of this approach is that when two clients make request for two different urls at the same time,
there's a chance they will have the same hash. When that happens, one of them will be overwritten.

The system, by default, hands out 4 character keys consisting a character within [A-Z, a-z, 0-9]. 
This is 64^4 combinations before it runs out of all the 4 character short urls. 
Assuming the hash function and urls are ideally distributed, the probability of two keys conflicting is 1 in 16.8 million.
To a key to be overwritten by another, that has to happen within the same second. There are 31540000 seconds in a year.

- If the app takes 2 requests per second for a year, we expect 1.88 conflicts. (((2-1)!)*(1/(64^4))*31540000)
- If the app takes 8 requests per second for a year, we would need 7 character hashes for similar number of conflicts. 
(((8-1)!)*(1/(64^7))*31540000)
- If the app takes 20 requests per second for a year, we would need 14 character hashes for similar number of conflicts.
(((20-1)!)*(1/(64^14))*31540000)
- If the app takes 50 requests per second for a year, we would need 39 character hashes for similar number of conflicts.
(((50-1)!)*(1/(64^39))*31540000)
- If the app takes 100 requests per second for a year, we would need 91 character hashes for similar number of conflicts
(((100-1)!)*(1/(64^91))*31540000)

Hence, current method does not scale well.

A solution I can think of is to have a single instance key handler that gives this serverless cluster a short hash 
every time a short url is generated. But this is not very scalable either, that key handler becomes the bottleneck.
A better solution would be writing stateful services and 
the key handler allocating each of them a huge set of random hashes.
Then, each service would hand out a random short url from that pool, without communicating with that key handler every 
time. Before the service assigns all of its short urls, it can go request a new pool of keys from the key handler.
In this case, the key handler would be the only instance that has write access to the db.

Also, some databases support incremental values, including firebase. But I'm out of time!
In Firestore, this is called batched writes. It increments a value between each write, and we'd use that integer value to 
generate a 1-to-1 conversion to a string of [A-Z, a-z, 0-9].

## Assumptions
- Url will not be deleted, modified or expire once created.
- User will not be deleted or modified once created.
- System does not return a login token when user registers successfully.
- System does not verify the validity or protocol of the URLs. 
Users are free to use custom protocols or private domains/IPs. (samba, IPv6, etc...)
- Login tokens do not expire and users do not logout.
- Short URLs will not be owned by a user. 
- Once registered, user will not forget their password or change their email.
- Users do not need to provide a valid token to consume a short url.

## Further work
- Database-incremented key generation
- Architectural diagrams
- Analytics
- Logging and error monitoring
- Allow user to create custom short urls
- For scalability, providing RSA signed JWT tokens with a published public key, 
so that other systems can verify user has a valid token from this system.
- Let others verify the validation of our tokens. This will improve scalability.
- Add cache
- Integration, adaptor and domain model tests
