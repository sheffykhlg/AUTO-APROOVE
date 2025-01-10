from os import getenv
from dotenv import load_dotenv

#Necessary Variables 
API_ID = int(getenv("API_ID", 20589413))
API_HASH = getenv("API_HASH", "654d559a9a91daeecd9e760fc73e6766")
BOT_TOKEN = getenv("BOT_TOKEN", "8041789409:AAFYu0Y1-08-BG9536ZZevLPhQDcgK4VtpM") #Put your bot token here
CHANNEL = getenv("CHANNEL", "moviescrownvip1") #Your public channel username without @ for force subscription.
MONGO = getenv("MONGO", "mongodb+srv://mongodb7575:mkCNT8b2LZJX5ekf@cluster0.bcuh8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") #Put mongo db url here
#Optional Variables
OWNER_ID = int(getenv("OWNER_ID", 6514361814)) #Go to @ThunderrXbot and type /id and put that value here. 
FSUB = bool(getenv("FSUB", True)) #Set this True if you want to enable force subscription from users else set to False.
PICS = getenv('PICS', 'https://i.ibb.co/JHd49Yb/file-629.jpg').split()
SESSION = environ.get("SESSION", "BQE6K2UAHvTKH1_6wr5tovh2AgrIEblRJTkreBFZyvxaow5WX_yf0LwcSRpbzC4WPcqRlAfnl4U1WZiV6IBtH20xlh1WLGFxWBEnIkyt1HrDA17ZAD--hl--ffqDNJsVgwkqics8OXrtiS1pIYk7HIUaJNbJyO16zPiGJnMoF5_3bN-MqjF45NoniSnxLQZ9NJqGNqainQ8bSyG0eszeooBeXBq2fzhwTGQlcltFvQWvePgBnuRPiLytbeeuDWHK2QZzp8aYU-goDoxn549Xx291l6etWfQHNJE41Vw3WOaOxX9crQPTUHBNp91-i_bG8TIzUrWtLuyY667alSzIrVQZ4E8RUQAAAAGESUXWAA") #pyrogram v2 user session ⚠️ v2 required ⚠️ & User must joined in your channel
