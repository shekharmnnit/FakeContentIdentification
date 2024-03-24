import pandas as pd
from fastapi import FastAPI, Form
from typing import Optional

from service.news_classifier_service import NewsClassifierService

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/api")
async def handle_request(url: Optional[str] = Form(None)):
    # You can now use the 'url' variable in your function
    return {"url": url}


@app.post("/postjson")
async def return_post_json(url: str = Form(...)):


    text = """
    "Others were more supportive: Good for you for going green! One car emits 4.6 metric tons of carbon dioxide each year, which is contributing to the global warming crisis, hurtling humanity toward imminent doom.

Or: So … do you guys need a lift?

Some interpreted the move as a personal attack: Oh, you think you’re better than me and that I’m polluting the environment with my 2013 Honda Pilot? Everyone can’t ditch their cars and bike around; I’ve got three kids with soccer practice, piano lessons and endless appointments!

People are also reading…
Charlottesville man found guilty of raping neighbor
Lorraine Williams, half of Charlottesville civil rights power couple, dies
Monticello scraps deal to purchase Michie Tavern
Charlottesville police investigating Belmont shooting
james and sadie aventon.jpeg
James and Sadie Van Vranken

For the Van Vrankens, the decision was a little more straightforward.


“We just like it,” James Van Vranken told The Daily Progress.

With both of their workplaces only a 10-minute ride from their house, the Van Vrankens said not having to worry about car maintenance, monthly insurance payments or even parking around Charlottesville is “a weight off of our shoulders.”

“Our life hasn’t changed as much as people might imagine that it would,” said Sadie Van Vranken. “There’s nowhere we went before that we can’t go to now on the bikes. It’s just a new calculus of deciding if it’s worth going out.”

The young couple was not avid cyclists prior to July, when they switched their primary mode of transportation, though James Van Vranken had some experience solely using a bicycle for a year while a graduate student in the U.K.

In fact, the Van Vrankens hadn’t given much consideration to e-bikes, thinking they were incredibly expensive and wouldn’t be suitable for their lifestyle.

Then, they went to the library — the Charlottesville E-Bike Lending Library based out of Josh Carp’s backyard shed in the city’s Fifeville neighborhood.


Q&A | Natalie Oschrin wants to put Charlottesville roads on a diet
POLITICS
Q&A | Natalie Oschrin wants to put Charlottesville roads on a diet
Jason Armesto
Carp launched the library in the spring of 2022 to provide people with a free opportunity to test out e-bikes for a week or two at a time, as well as counter some of the common misconceptions and mystery surrounding motorized bicycles.

“It’s hard to explain exactly what an e-bike is; it’s not a bike or moped,” Carp told The Daily Progress. “Something about actually trying one makes people say, ‘I actually really like this.’ I want to give people real-life experience on the bikes.”

Potential e-bikers can browse the library’s selection, read up on all things e-bike and schedule a joyride through the library’s website, ebikelibrarycville.org. Carp’s day job as a software engineer allows him to work from home, so those interested in borrowing a bike can drop by the library and test drive different styles along Carp’s street before deciding which bike they want to check out for a trial period.

EBikeCville'24-9.jpg
Josh Carp rides an electric bicycle outside the Charlottesville E-Bike Lending Library on Wednesday, March 13.

CAL CARY, THE DAILY PROGRESS
“Everybody who tries the bikes enjoys them,” said Carp. “The library allows people to test out their commute and find different safe routes around the city.”


The due date for most bikes is within a week or two, but the nonprofit service doesn’t charge late fees — or any fees for that matter. Carp’s mission is focused on giving people a chance to experiment with incorporating the bikes into their daily routine or finding the bike that best fits their specific needs, all free of charge.

“We thought the library was a scam at first because it was all free. We didn’t quite believe it,” said James Van Vranken. “But once we borrowed a bike, it showed us that we liked it and it fit with our lifestyle.”

Crozet park and ride promises to cut down on Charlottesville commutes
POLITICS
Crozet park and ride promises to cut down on Charlottesville commutes
Jason Armesto
The trial period can help a potential buyer overcome the sticker shock, which is understandable given an e-bike can range in price from $1,000 to $3,000. Though e-bikes are nowhere close to the price of a car, it is still a sizable investment for the average person and one that may be difficult to make without first testing out how an e-bike rides in the city. Carp said a number of individuals who have tapped the library’s services already had an idea of what bike they were looking to purchase either online or at a store, but wanted to get in a couple test rides beforehand.


Most of the library’s users tend to be commuters searching for a cheaper, more enjoyable ride to work in the mornings, Carp said. A portion of them includes the parents of young children who take pleasure in skipping the tedious drop-off and pick-up lanes at school. Instead of waiting behind lines of cars, they can pedal straight to the schoolhouse door with their children strapped onto the back of a “cargo bike,” which has space to hold two small children or bags of groceries on the back.

The bicycle’s motor compensates for the additional weight, and some models also sport throttles that provide an extra thrust. The rider can adjust the level to offset the amount of effort they need to exert with a gear shift on the handle bar, similar to a manually powered bicycle.

EBikeCville'24-5.jpg
Josh Carp points at the digital gauge on an electric bicycle at the Charlottesville E-Bike Lending Library outside his house on Wednesday, March 13, 2024.

CAL CARY, THE DAILY PROGRESS
“It makes you feel like you’re in much better shape than you actually are,” said Carp.

One individual who bought an e-bike after trying out one at the library was a travel nurse working night shifts at University of Virginia Medical Center. According to Carp, by the time she got off work at night, there was no bus running to take her back to the parking lot where she had parked her car more than a mile away from the hospital. So, she bought an e-bike."
"""

    #add scraping code
    service = NewsClassifierService()
    data = {'text': [text]}
    df = pd.DataFrame(data)
    classification_result = service.classify_news(df)
    print('Classification result:', classification_result)
    return {"Result": classification_result}