##dict of response for each type of intent
import random


complaint_response_dict = {
    "national registration department":'promised to deliver MyKad in 2 months from the date of application but failed to do so and also failed to provide feedback on citizenship application',
    "immigration department":'failed to provide feedback about work permit application and replacement of missing passport',
    "inland revenue board":'did not pay back the credit balance of income tax in 2 months as promised earlier.',
    "police":'Delay or inaction by Police in investigating reports that were lodged by public burglary, accidents and drug addicts who occupied empty houses | did not pay back the credit balance of income tax in 2 months as promised earlier.',
    "epf":'Delay by Employee Provident Fund (EPF) in approving members applications to withdraw contribution money with purpose of purchasing new houses, financing child education and also because of the permanent disabilities',
    "faq_link":'You can check out the list of public services here <a href=\"http://www.pcb.gov.my/en/complaintinfo/type-of-complaint\">Public Complaint Bureau - Type of complaint</a>'
}


# startupinfo_response_dict = {
#     "investors":'Here are the top 5 investors: <UL><li>Undisclosed Investors</li><li>Kalaari Capital</li><li>Indian Angel Network</li><li>Info Edge (India) Ltd</li><li>Brand Capital</li></ul>For more info: <a href=\"http://www.github.com/lkamat\">Startups in India</a>',
#     "startups":'Top 5 startups based on funding.<UL><li>Paytm</li><li>Flipkart</li><li>Ola</li><li>Ola Cabs</li><li>Oyo Rooms</li></ul> For more info: <a href="http://www.github.com/lkamat">Startups in India</a>',
#     "industries":'Top 5 industries based on funding.<UL><li>Consumer Internet</li><li>Technology </li><li>ecommerce </li><li>Logistics </li><li>Education</li></ul>For more info: <a href="http://www.github.com/lkamat">Startups in India</a>',
#     "categories":'Top 5 categories based on funding.<UL><li>Food Delivery Platform</li><li>Online lending platform</li><li>eOnline Pharmacy</li><li>Online Learning Platform</li><li>ECommerce Marketplace</li></ul>For more info: <a href="http://www.github.com/lkamat">Startups in India</a>',
#     "city": 'Top 5 cities with the most startup funding:<UL><li>Bangalore</li><li>Mumbai</li><li>New Delhi</li><li>Gurgaon</li><li>Pune</li></ul>For more info: <a href="http://www.github.com/lkamat">Startups in India</a>',
#     "type": 'Startup funded by investment type:<UL><li>Private Equity</li><li>Seed Funding </li><li>Debt Funding </li></ul>Fo rmore info: <a href="http://www.github.com/lkamat">Startups in India</a>',
#     "faq_link":'You can check out the list of startups here <a href="http://www.github.com/lkamat">Startups in India</a>'
# }

BOT_INTRO_RESPONSES = ["Aku Bot Servis, apa yg saya boleh bantu? 1) Membuat Aduan 2) Dapat Info ", "I am Service Bot, what can i help? 1) File a complaint 2) Information"]
GREETING_RESPONSES = ["*selamat pagi tuan/puan","Good Morning"]
GOODBYE_RESPONSES = ["terima kasih", "good bye", "take care", "glad it help"]
AFFIRM_RESPONSES = ["indeed", "okay", "that's right", "great", "cool"]


def greeting():
    """If any of the words in the user's input was a greeting, return a greeting response"""
    return random.choice(GREETING_RESPONSES)

def bot_intro():
    """If any of the words in the user's input was a greeting, return a greeting response"""
    return random.choice(BOT_INTRO_RESPONSES)

def goodbye():
    """If any of the words in the user's input was a goodbye, return a goddbye response"""
    return random.choice(GOODBYE_RESPONSES)

def affirm():
    """If any of the words in the user's input was a goodbye, return a goddbye response"""
    return random.choice(AFFIRM_RESPONSES)

def file_complaint():
    return "please put down the details: Date & Time: ____ , Officer-in-charge: ____, Location: _____, Remark:_______,  and we will file a case and get back to you again "


def info_search(entities):
    if entities == []:
        return "For more information please refer to link below ..." +  complaint_response_dict["faq_link"]
    if len(entities) >= 1:
        return complaint_response_dict[entities[0] ]
    return "You can look for" + complaint_response_dict["faq_link"]

def complaint(entities):
    if entities == []:
        return "For more information please refer to link below ..." +  complaint_response_dict["faq_link"]
    if len(entities) >= 1:
        return complaint_response_dict[entities[0] ]
    return "You can look for" + complaint_response_dict["faq_link"]


