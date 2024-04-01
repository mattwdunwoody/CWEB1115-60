# Inheritance

import MN_Chef
import WI_Chef
import TX_Chef
import NM_Chef

if __name__ == '__main__':

    MN_Chef = MN_Chef.MN_Chef()
    WI_Chef = WI_Chef.WI_Chef()
    TX_Chef = TX_Chef.TX_Chef()
    NM_Chef = NM_Chef.NM_Chef()

    chefs = [MN_Chef, WI_Chef, TX_Chef, NM_Chef]

    for chef in chefs:
        print(f'Step 1: {chef.make_hotdish()}\nStep 2: {chef.make_fried_spam()}\nThe result: {chef.make_spam_hotdish()}\n')