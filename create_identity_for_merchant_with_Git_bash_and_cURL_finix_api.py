Purpose = "This shows how to create a merchant id using a python with the Finix Payment APIs"
print (Purpose)

import finix

from finix.config import configure
configure(root_url="https://finix.sandbox-payments-api.com", auth=("US5yHgRAS7JyYzRYiigeYvZF", "6b86f7a9-0fd1-42c9-af25-4faac06d088c"))

from finix.resources import Identity

identity = Identity(**
    {
        "tags": {
            "Studio Rating": "4.7"
        },
        "entity": {
            "last_name": "Richeson",
            "max_transaction_amount": 200000,
            "has_accepted_credit_cards_previously": True,
            "default_statement_descriptor": "Self Employed",
            "personal_address": {
                "city": "Highlands Ranch",
                "country": "USA",
                "region": "CO",
                "line2": "Attn: Randy",
                "line1": "5006 Cresthill Place",
                "postal_code": "80130"
            },
            "incorporation_date": {
                "year": 1966,
                "day": 22,
                "month": 4
            },
            "business_address": {
                "city": "Highlands Ranch",
                "country": "USA",
                "region": "CO",
                "line2": "Attn: Randy",
                "line1": "5006 Cresthill Place",
                "postal_code": "80130"
            },
            "ownership_type": "PRIVATE",
            "first_name": "Randy",
            "title": "CEO",
            "business_tax_id": "123456789",
            "doing_business_as": "Self Employed",
            "principal_percentage_ownership": 100,
            "email": "user@example.org",
            "mcc": "0742",
            "phone": "3038773492",
            "business_name": "Self Employed",
            "tax_id": "123456789",
            "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP",
            "business_phone": "+1 (303) 877-3492",
            "dob": {
                "year": 1966,
                "day": 22,
                "month": 4
            },
            "url": "www.PrestigeWorldWide.com",
            "annual_card_volume": 12000000
        }
    }).save()

print(identity)

