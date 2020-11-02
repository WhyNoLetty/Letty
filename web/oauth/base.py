import os, aiohttp
import urllib.parse
from bs4 import BeautifulSoup

class Api:
    def __init__(self, *, letty):
        self.letty = letty
        self.link = letty.data.link
    

    async def url(self, value=None, data=None):          
       if value == 'invite':
          code = {"client_id":str(self.letty.user.id), "permissions":data.get("perma", "8"), "scope":"bot", "guild_id":data.get("guild", "None")} 
       elif value == 'login':
          code = {"client_id":str(self.letty.user.id), "response_type":"code", "scope":"identify guilds guilds.join", "redirect_uri":f"{self.link.website}/callback"} 
       else:
          if value in ['youtube','github', 'suport', 'donate', "twitter"]:
             code = {"youtube":self.link.youtube, "github":self.link.github, "suport":self.link.suport, "donate":self.link.donate, "twitter":self.link.twitter}
             return code[value]
          return '/'
       return f"{self.link.endpoint}?{urllib.parse.urlencode(code)}"
    
    async def data(self, value=None, data=None):
       if value == 'oauth':
          code = {"client_id":str(self.letty.user.id), "code":data.get("code", "None"), "client_secret":os.environ['OAUTH_SECRET'], "grant_type":"authorization_code", "scope":"identify guilds guilds.join", "redirect_uri":f"{self.link.website}/callback"} 
       elif value == 'header':
           code = {"Content-Type": "application/x-www-form-urlencoded"}
       elif value == 'bearer':
           code = {"Authorization": f"Bearer {data.get('token', 'None')}"}
       return code
    
    async def callback(self, data):
       code = data.get("code", None)
       if code is None:
          return None
       data = await self.data(value='oauth', data=data)
       headers = await self.data(value='header')
       async with self.letty.session.post(f"https://discordapp.com/api/oauth2/token", data=data, headers=headers) as response:
            return await response.json()
    
    async def get_user(self, data, endpoint='@me'):
       headers = await self.data(value='bearer', data=data)
       async with self.letty.session.get(f"https://discordapp.com/api/users/{endpoint}", headers=headers) as response:
            return await response.json()
    
