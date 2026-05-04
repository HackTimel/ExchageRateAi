import os
from dotenv import load_dotenv
from tools import get_exchange_rate


load_dotenv()

print(get_exchange_rate(120,"eur", "usd"))
