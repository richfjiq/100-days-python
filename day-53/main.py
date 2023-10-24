from scrapping_page import Scrapping
from fill_form import FillForm


form = FillForm()
scrapping = Scrapping()

for n in range(len(links)):
    url = f"{BASE_URL}{scrapping.links[n]}"
    form.fill(address=scrapping.addresses[n], price=scrapping.prices[n], link=url)

print("Finish")
