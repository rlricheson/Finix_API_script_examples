curl https://finix.sandbox-payments-api.com/identities \
    -H "Content-Type: application/vnd.json+api" \
    -u  US5yHgRAS7JyYzRYiigeYvZF:6b86f7a9-0fd1-42c9-af25-4faac06d088c \
    -d '
    {
        "tags": {
            "Studio Rating": "4.7"
        },
        "entity": {
            "last_name": "Richeson",
            "max_transaction_amount": 150000,
            "has_accepted_credit_cards_previously": true,
            "default_statement_descriptor": "Prestige World Wide",
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
            "email": "randy.richeson@gmail.com",
            "mcc": "0742",
            "phone": "3038773492",
            "business_name": "Self Employed",
            "tax_id": "123456789",
            "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP",
            "business_phone": "+1 (303) 877-3492",
            "dob": {
                "year": 1966,
                "day": 22,
                "month": 04
            },
            "url": "www.PrestigeWorldWide.com",
            "annual_card_volume": 12000000
        }
    }'

