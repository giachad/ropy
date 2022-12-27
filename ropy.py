import requests

# Badge class stores information about badges, yup, crazy right?
class Badge:
    def __init__(self, badgeId) -> None:
        request = requests.get("https://badges.roblox.com/v1/badges/"+str(badgeId)).json()
        
        self.badgeId = badgeId
        self.name = request["name"]
        self.description = request["description"]
        self.displayName = request["displayName"]
        self.displayDescription = request["displayDescription"]
        self.displayIconImageId = request["displayIconImageId"]
        self.enabled = request["enabled"]
        self.iconImageId = request["iconImageId"]
        self.created = {"date": str(request["created"]).split("T")[0], "time": str(request["created"]).split("T")[1]}
        self.updated = {"date": str(request["updated"]).split("T")[0], "time": str(request["updated"]).split("T")[1]}
        self.statistics = request["statistics"]
        self.awardingUniverse = request["awardingUniverse"]

# Friend class is a dumbed-down version of the User class
class Friend:
    def __init__(self, userId, username, banned, verified, displayName, presence) -> None:
        self.userId = userId
        self.username = username
        self.banned = banned
        self.verified = verified
        self.displayName = displayName

# User class contains info such as userId, username and description
class User:
    def __init__(self, userId) -> None:
        self.userId = userId
        
        request = requests.get("https://users.roblox.com/v1/users/"+str(userId), headers={"accept": "application/json"}).json()
        
        self.description = request["description"]
        self.created = {"date": str(request["created"]).split("T")[0], "time": str(request["created"]).split("T")[1]}
        self.banned = request["isBanned"]
        self.verified = request["hasVerifiedBadge"]
        self.username = request["name"]
        self.displayName = request["displayName"]

        request2 = requests.get("https://friends.roblox.com/v1/users/"+str(userId)+"/friends?userSort=1", headers={"accept": "application/json"})

        self.friends = []
        self.friendCount = len(request2.json()["data"])

        for friend in request2.json()["data"]:
            friend_ = Friend(friend["id"], friend["name"], friend["isBanned"], friend["hasVerifiedBadge"], friend["displayName"], friend["presenceType"])
            self.friends.append(friend_)
