from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from app.config import SLACK_BOT_TOKEN, SLACK_APP_TOKEN, SLACK_CHANNEL_ID
from app.utils import extract_domain
from app.pitchbook_api import search_company, search_investors, get_company_bio

app = App(token=SLACK_BOT_TOKEN)

def generate_company_description(bio, investors):
    company_name = bio["companyName"]["formalName"]
    description = bio["description"]
    year_founded = bio["yearFounded"]
    hq_location = f"{bio['hqLocation']['city']}, {bio['hqLocation']['stateProvince']}, {bio['hqLocation']['country']}"
    employees = bio["employees"]
    total_money_raised = bio["totalMoneyRaised"]["amount"]
    
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
"""

@app.event("message")
def handle_message_events(body, logger):
    event = body["event"]
    channel_id = event["channel"]
    
    if channel_id != SLACK_CHANNEL_ID:
        return
    user = event["user"]
    text = event.get("text", "")
    
    if event.get("bot_id") and event.get("username") != "Top of Funnel Bot":
        return

    domain = extract_domain(text)
    if not domain:
        return

    company_id = search_company(domain)
    if not company_id:
        app.client.chat_postMessage(
            channel=channel_id,
            thread_ts=event["ts"],
            text="No PitchBook data available for this company."
        )
        return

    bio = get_company_bio(company_id)
    investors = search_investors(company_id)

    if not bio:
        app.client.chat_postMessage(
            channel=channel_id,
            thread_ts=event["ts"],
            text="Unable to retrieve company information from PitchBook."
        )
        return

    description = generate_company_description(bio, investors)

    app.client.chat_postMessage(
        channel=channel_id,
        thread_ts=event["ts"],
        text=description
    )
