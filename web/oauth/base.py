import os, aiohttp
import urllib.parse

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
