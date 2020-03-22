import sys
import pywikibot
from pywikibot import pagegenerators
siteC = pywikibot.Site(u'commons', u'commons')
siteC.login()

def movepage(title, newtitle, summary, noredirect=True):
    page = pywikibot.Page(siteC, title)
    page = pywikibot.site.APISite.movepage(
        siteC,
        page=page,
        newtitle=newtitle,
        summary=summary,
        noredirect=noredirect
    )
    return page


category = pywikibot.Category(siteC, u'Vegetarian food in Ain')
print("this category is analysed...")

gen = pagegenerators.CategorizedPageGenerator(category)

for page in gen:
    title = str(page.title())
    if title.find("grattin"):
        titleTarget = title.replace("grattin", "gratin")
        try:
            movepage(title, titleTarget, "faute d'ortographe grattin => gratin")
        except:
            print("Petit souci")
