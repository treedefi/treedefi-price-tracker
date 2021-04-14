import requests
import re
treeweb = requests.get("https://bscscan.com/token/0xf0fcd737fce18f95621cc7841ebe0ea6efccf77e")
seedweb = requests.get("https://bscscan.com/token/0x40B34cC972908060D6d527276e17c105d224559d")
p= re.compile("[$][0-9]{1,4}\.[0-9]{1,4}")
result1=p.search(treeweb.text)
result2=p.search(seedweb.text)
print(result1.group(0),result2.group(0))

