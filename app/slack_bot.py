from slack_bolt import App
from app.config import SLACK_BOT_TOKEN, SLACK_CHANNEL_ID
from app.utils import extract_domain
from app.pitchbook_api import search_company, search_investors, get_company_bio
from app.logger import logger

app = App(token=SLACK_BOT_TOKEN)

def generate_company_description(bio, investors):
    company_name = bio["companyName"]["formalName"]
    description = bio["description"]
    year_founded = bio["yearFounded"]
    hq_location = f"{bio['hqLocation']['city']}"
    employees = bio["employees"]
    total_money_raised = bio["totalMoneyRaised"]["amount"]
    financingStatusNote = bio["financingStatusNote"]["note"]
    financingAsOf = bio['financingStatusNote']["asOfDate"]
    
    investor_text = ", ".join(investors[:5])
    if len(investors) > 5:
        investor_text += f", and {len(investors) - 5} more"

    return f"""
{company_name} is a company founded in {year_founded} and headquartered in {hq_location}.
Description: {description}

Key Facts:
- Employees: {employees}
- Total Money Raised: ${total_money_raised:,.2f}
- Notable Investors: {investor_text}
- Financing (Updated {financingAsOf}): {financingStatusNote}
"""

@app.event("message")
def handle_message_events(body, say):
    event = body['event']
    channel_id = event['channel']
    
    logger.info(f"Received message event in channel {channel_id}")
    
    if channel_id != SLACK_CHANNEL_ID:
        logger.info(f"Ignoring message from channel {channel_id} - not the target channel")
        return

    user = event['user']
    text = event['text']
    
    logger.info(f"Processing message from user {user}: {text[:50]}...")  # Log first 50 chars of message

    if event.get("bot_id") and event.get("username") != "Top of Funnel Bot":
        logger.info(f"Ignoring message from bot: {event.get('username', 'Unknown bot')}")
        return

    domain = extract_domain(text)
    if not domain:
        logger.info("No valid domain found in message")
        return

    logger.info(f"Extracted domain: {domain}")

    company_id = search_company(domain)
    if not company_id:
        logger.info(f"No PitchBook data found for domain: {domain}")
        say(
            text=f"No PitchBook data available for the company with domain: {domain}",
            thread_ts=event["ts"]
        )
        return

    logger.info(f"Found company ID: {company_id}")

    bio = get_company_bio(company_id)
    investors = search_investors(company_id)

    if not bio:
        logger.warning(f"Unable to retrieve company bio for company ID: {company_id}")
        say(
            text="Unable to retrieve company information from PitchBook.",
            thread_ts=event["ts"]
        )
        return

    logger.info(f"Retrieved bio and {len(investors)} investors for company ID: {company_id}")

    description = generate_company_description(bio, investors)

    say(
        text=description,
        thread_ts=event["ts"]
    )
    logger.info(f"Posted company description for {bio['companyName']['formalName']}")

@app.error
def global_error_handler(error, body, logger):
    logger.exception(f"Error: {error}")
    logger.error(f"Request body: {body}")
