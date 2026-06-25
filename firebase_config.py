import pyrebase

config = {
    "apiKey": "AIzaSyCb7vZz8iCFuK2iEJpoIMElERZkEdiE9eE",
    "authDomain": "anzzstroe.firebaseapp.com",
    "databaseURL": "https://anzzstroe-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "anzzstroe",
    "storageBucket": "anzzstroe.firebasestorage.app",
    "messagingSenderId": "7353814767",
    "appId": "1:7353814767:web:fb1d70c45e612f5eb3951a"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()