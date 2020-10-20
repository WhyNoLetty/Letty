import os, aiohttp
import urllib.parse

class Filter:
    def __init__(self, *, app):
        self.app = app
        
        async def use(lang, cmd):
           usage = await lang(f'help|{cmd}')
           text = f' {usage["usage"]}' if usage != None else ''
           return f"lt.{cmd.qualified_name}{text}"

        async def sub(cmd):
           if hasattr(cmd, 'commands'):
             lista = []
             for sub_command in cmd.commands:
                 lista.append(sub_command.name)
             return lista
           else:
             return None
        
        async def perm(lang, cmd):
          if hasattr(cmd, 'commands'):
            for sub_command in cmd.commands:
                perm = await lang(f'help|{cmd}|{sub_command.name}|permission')
          else:
            perm = await lang(f'help|{cmd}|permission')
          
          text = [f'{await lang("permission|text|"+a["text"])} [{await lang("permission|user|"+a["user"])}]' for a in perm] or await lang('value|not_defined|f')
          return text


        async def example(lang, cmd):
          if hasattr(cmd, 'commands'):
            lista = []
            for sub_command in cmd.commands:
                example_ = await lang(f'help|{cmd}|{sub_command.name}')
                lista.append(f"lt.{cmd.qualified_name} {sub_command.name} {example_['example'][0]}")
            return lista
          else:
            example_ = await lang(f'help|{cmd}')
            invocation = f"lt.{cmd.full_parent_name + ' ' if cmd.parent else ''}"
            text = [f'{invocation}{cmd.aliases[i] if -1 < i < len(cmd.aliases) else cmd.name} {e}'for i, e in enumerate(example_["example"], -1) or 'gg']
            return text


        self.app.add_template_filter(sub)
        self.app.add_template_filter(example)
        self.app.add_template_filter(use)
        self.app.add_template_filter(perm)

