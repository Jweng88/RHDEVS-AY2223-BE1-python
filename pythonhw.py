# This program simualtes the backend of a ticket purchasing system

# Price per visitor is $5
# Price per member is $3.50

# You are to do the following
# 1. Identify all banned visitors with a filter call
# 2. Determine the memberships status of all applicants
# 3. Calculate the total price for all eligible visitors
# 4. For each valid visitor, return a corresponding ticket in Dictionary form
# 5. Return an error via thrown exception if applicants is empty
# Complete everything above in a function called processRequest
# Your should abstract out function as much as reasonably possible

bannedVisitors = ["Charles", "Grace", "Bruce"]
memberStatus = {
    "Ally": True,
    "David": True,
    "Brendan": False
}

request = {
    "applicants": ["Amy", "Ally", "David", "Brendan", "Zoho"]
}


try:
        
    def processRequest(request):
        # Your code here
        totalCost = 0
        tickets = {}
        successfulApplicants = list()
        bannedApplications = list()
        big_dict = {}
        big_dict["successfulApplicants"] = successfulApplicants
        big_dict["banneedApplicants"] = bannedApplications
    
        for name in request["applicants"]:
            if name not in bannedVisitors:
                successfulApplicants.append(name)
            else:
                bannedApplications.append(name)   
        #print(successfulApplicants)
        #print(bannedApplications)
        
        for name in request["applicants"]:
            if name in memberStatus:
                if memberStatus[name]:
                    totalCost += 3.50
                else:
                    totalCost += 5              
            else:
                totalCost += 5
        big_dict["totalCost"] = totalCost
        
        big_dict["tickets"] = list()
        for name in request["applicants"]:
            if name in memberStatus:
                if memberStatus[name]:
                    tickets["name"] = name
                    tickets["membershipStatus"] = True
                    tickets["price"] = 3.50
                    big_dict["tickets"].append(tickets.copy())
                else:
                    tickets["name"] = 5
                    tickets["membershipStatus"] = False
                    tickets["price"] = 5
                    big_dict["tickets"].append(tickets.copy())               
            else:
                tickets["name"] = name
                tickets["membershipStatus"] = False
                tickets["price"] = 5
                big_dict["tickets"].append(tickets.copy())
        #print(totalCost)
        #print(big_dict)
        return(big_dict)
                

    print(processRequest(request))

except:
    print("No Applicants")

# {
#   successfulApplicants:
#   bannedApplicatns:
#   totalCost:
#   tickets: [
#       {
#            "name": ,
#            "membershipStatus": ,
#            "price":
#       }, ....
#   ]
#
# }


# OR

# {"error": "No applicants"}