"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Club": {
        "description": "Practice soccer skills and play team matches",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 22,
        "participants": []
    },
    "Basketball Club": {
        "description": "Practice basketball skills and play team matches",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": []
    },
    "Art Club": {
        "description": "Explore drawing, painting, and other visual arts",
        "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
        "max_participants": 15,
        "participants": []
    },
    "Drama Club": {
        "description": "Practice acting and prepare theatrical performances",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": []
    },
    "Debate Club": {
        "description": "Develop public speaking and argumentation skills",
        "schedule": "Mondays, 3:30 PM - 4:30 PM",
        "max_participants": 16,
        "participants": []
    },
    "Science Club": {
        "description": "Explore scientific concepts through experiments and projects",
        "schedule": "Wednesdays, 3:30 PM - 4:30 PM",
        "max_participants": 18,
        "participants": []
    },
    "Swimming Club": {
        "description": "Train swimming techniques and compete in meets",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": []
    },
    "Tennis Club": {
        "description": "Practice tennis skills and play singles and doubles matches",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 14,
        "participants": []
    },
    "Music Club": {
        "description": "Learn instruments, rehearse, and perform music together",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": []
    },
    "Photography Club": {
        "description": "Explore photography techniques and create visual projects",
        "schedule": "Wednesdays, 3:30 PM - 4:30 PM",
        "max_participants": 12,
        "participants": []
    },
    "Math Club": {
        "description": "Solve challenging problems and prepare for math competitions",
        "schedule": "Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 16,
        "participants": []
    },
    "Robotics Club": {
        "description": "Design, build, and program robots for competitions",
        "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": []
    },
    "Volleyball Club": {
        "description": "Practice volleyball skills and play team matches",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": []
    },
    "Track and Field": {
        "description": "Train running, jumping, and throwing events for competitions",
        "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 25,
        "participants": []
    },
    "Dance Club": {
        "description": "Learn dance styles and prepare performances",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": []
    },
    "Film Club": {
        "description": "Watch films, discuss cinema, and create short videos",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": []
    },
    "Astronomy Club": {
        "description": "Study stars, planets, and the night sky through observation and projects",
        "schedule": "Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 14,
        "participants": []
    },
    "Philosophy Club": {
        "description": "Discuss ideas, ethics, and critical thinking through readings and debate",
        "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
        "max_participants": 16,
        "participants": []
    },
    "Badminton Club": {
        "description": "Practice badminton skills and play matches",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": []
    },
    "Baseball Club": {
        "description": "Practice baseball skills and play team matches",
        "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": []
    },
    "Ceramics Club": {
        "description": "Create pottery and explore ceramic techniques",
        "schedule": "Wednesdays, 3:30 PM - 4:30 PM",
        "max_participants": 12,
        "participants": []
    },
    "Choir Club": {
        "description": "Practice singing and prepare group performances",
        "schedule": "Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": []
    },
    "Literature Club": {
        "description": "Read and discuss literature together",
        "schedule": "Fridays, 3:30 PM - 4:30 PM",
        "max_participants": 15,
        "participants": []
    },
    "History Club": {
        "description": "Explore historical events through discussion and projects",
        "schedule": "Mondays, 3:30 PM - 4:30 PM",
        "max_participants": 16,
        "participants": []
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up for this activity")

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}


@app.delete("/activities/{activity_name}/participants")
def unregister_from_activity(activity_name: str, email: str):
    """Unregister a student from an activity"""
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    activity = activities[activity_name]

    if email not in activity["participants"]:
        raise HTTPException(status_code=404, detail="Participant not found in this activity")

    activity["participants"].remove(email)
    return {"message": f"Unregistered {email} from {activity_name}"}
