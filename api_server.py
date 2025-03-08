import jwt
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException, Depends, Form
from pydantic import BaseModel
from typing import Optional
from fastapi.security import OAuth2PasswordBearer
import requests
from database_create import Project, Permission, ContainerExpirationPolicy, Links
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

# Secret key to encode and decode JWT tokens (keep it secure in a production environment)
SECRET_KEY = "Sussh!!...This_is_a_secret!!"  # Never expose this publicly!
ALGORITHM = "HS256"  # HMAC algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiration time

app = FastAPI()

# Create OAuth2PasswordBearer instance for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Project(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

class Token(BaseModel):
    access_token: str
    token_type: str

def sendRequest(url_name, token):
    url = url_name
    headers = {
        "Accept": "application/json",
        "Private-Token": token }
    response = requests.get(url, headers=headers)
    return response
    

def getResponse(api_response):
    if api_response.status_code == 200:
        response_data = api_response.json()
        return(response_data)
    else:
        print(f"Failed to retrieve response with status code: {api_response.status_code}")

# Token creation function
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    """
    Function to create a JWT token with an expiration date.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Token validation function
def verify_token(token: str = Depends(oauth2_scheme)):
    """
    Function to verify the JWT token.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  # In a real application, you would return user info from the payload.
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/token", response_model=Token)
def login_for_access_token(username: str = Form(...), token: str = Form(...)):
    """
    The username and password should be sent as form data in the body.
    """
    # Simulating a user authentication. Replace this with actual logic.
    if username == "nandiya" and token == "personalY5x4w3Cme8yqUjMoxmyi":
        access_token = create_access_token(data={"sub": username})
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")


@app.get("/projects")
async def get_project(token: str = Depends(verify_token)):
    """
    Endpoint to fetch project details based on the token.
    """
    # After successful token validation, return a sample project.
    url = "https://gitlab.boon.com.au/api/v4/projects"
    private_token = "personalY5x4w3Cme8yqUjMoxmyi"

    response = sendRequest(url, private_token)

    result = getResponse(response)
    return result


@app.post("/insert_projects/")
async def insert_project(json_string: str, db: Session = Depends(get_db)):
    try:
        # Parse the JSON string into a dictionary
        project_data = json.loads(json_string)

        # Validate the parsed data
        project = ProjectBase(**project_data)

        # Create a new project instance
        new_project = Project(
            name=project.name,
            description=project.description,
            created_at=project.created_at,
            visibility=project.visibility,
            archived=project.archived
        )

        # Add the project to the session and commit
        db.add(new_project)
        db.commit()
        db.refresh(new_project)

        return {"message": "Project inserted successfully", "data": new_project.id}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid JSON format or data")
