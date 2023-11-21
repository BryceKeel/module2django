from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from dataclasses import dataclass

# Create your views here.

@dataclass
class Team:
    Name: str
    Description: str
    Team_Members: list[str]

Teams = {
    "Management": Team(
        "Management",
        "Management team is in charge of keeping other students on track, Making and leading the teams for chores, and making sure we have all the cleaning supplies.",
        ["Owen", "Jeremiah", "Nick", "Ab", "Abigail", "Mathew"],
    ),
    "Community": Team(
        "Community",
        "Community team is in charge of coming up with events for the school, they contact places and work to bring the community together",
        ["Jordan", "Joby", "Aj", "Micah", "Caleb"],
    ),
    "Documentation": Team(
        "Documentation",
        "Documentation Team is in charge of taking pictures and posting online to show and advertise the school",
        ["Conner", "Kaleigh", "Blair", "Mina", "Jay", "Joshua", "Kayleah",],
    ),
    "Procurement": Team(
        "Procurement",
        "Procurement is in charge of going out and buying items, they are also in charge of preparing food for lunch.",
        ["Adrian", "Bryce", "Big John", "Blaine", "Wyatt"],
    ),
}

def homepage(request: HttpRequest) -> render:
    context = {
        "teams": Teams.keys
    }
    return render(request, "index.html", context)

def teampages(request: HttpRequest, team_name: str) -> render:
    team = Teams.get(team_name)
    if team:
        context = {
            "team_info": team
        }
        return render(request, "info.html", context)
    else:
        return HttpResponse("Team not found.")

def ilovethisguy(request: HttpRequest) -> render:
    return render(request, "ilovethisguy.html")
