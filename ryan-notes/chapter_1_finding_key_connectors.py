# Finding Key Connectors

# social media users
users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

# friendship data represented as pairs of IDs
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Exercise 1
# Create a dict where the keys are user ids and the values are lists of friend ids. 
# Output:
# {
#   0: [1, 2],
#   1: [0, 2, 3],
#   2: [0, 1, 3],
#   etc...
# }

friendships = {user["id"]: [] for user in users}

for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

# obtain the number of friends for a given person
def number_of_friends(user):
    user_id = user["id"]
    friends_ids = friendships[user_id]
    return len(friends_ids)


# Determine the total number of connections:
total_connections = sum(number_of_friends(user) for user in users)
print(total_connections)

# average number of connections
average_connections = total_connections / len(users)    

# Degree Centrality
# A simple count of the total number of connections linked to a vertex
# The degree centrality of a node is simply its degree—the number of edges it has. 

# create a list of tuples that have (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

# sort by most friends to least friends
num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse=True)

# write a function that determines the count of friends of friends for a user
# do not count friends of friends that are already friends
# 
# output should be:
# { id_of_friend_of_friend: number_of_connections,
#   id_of_friend_of_friend: number_of_connectsion,
#   etc... }