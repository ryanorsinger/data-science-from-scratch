# FINDING KEY CONNECTORS (chapter section)
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

# Each pair is (user_id, number_of_friends)
# [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3), (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]
# What we've done in the above operation is compute the network metric of "degree centrality"




# DATA SCIENTISTS YOU MAY KNOW (chapter section)

def foaf_ids_bad(user):
    """foaf is short for "friend of friend" """
    return [foaf_id 
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]

# Fiends of friends for Hero at users[0]
print(foaf_ids_bad(users[0]))
# The above implementation is "Bad" because it includes user 0 and user 3 twice


# Let's try to do better
from collections import Counter 

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]   # For each of my friends
        for foaf_id in friendships[friend_id]   # find their friends
        if foaf_id != user_id                   # who aren't me
        and foaf_id not in friendships[user_id] # and aren't my friends
    )

print(friends_of_friends(users[0]))
print(friends_of_friends(users[3]))
print(friends_of_friends(users[5]))

# Setup the list of interests for each user
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def data_scientists_who_like(target_interest):
    """Find the ds of all users who like the target interest"""
    return [user_id for user_id, user_interest in interests if user_interest == target_interest]

print(data_scientists_who_like("Java"))

# Let's setup a more efficient lookup structure
# Keys are interests (because they're unique), values are a list of user_ids with that interest
# We're using a defaultdict to map interests to users
from collections import defaultdict
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# Add another defaultdict to map users to interests
# Keys are user_ids and values are lists of interests for that user
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)
interests_by_user_id

# Consider how to find who has the most interests in common with another user
# Step 1. iterate ver the user's interest.
# Step 2. For each interest, iterate over the other users with that interest
# Step 3. Keep count of how many times we see each other user

def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    )

most_common_interests_with(users[0])


# Salaries and tenure data
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

# Keys are years to lists of salaries for each tenure
# map years of tenure to lists of salaries
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

# Keys are years, each value is the average salary
# We're mapping tenure to average salary here
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

average_salary_by_tenure

## This doesn't really work well (with this data) because nobody shares a tenure date.
## Let's bucket the tenures

def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "less than five"
    else:
        return "more than five"
    
# Keys are tenure buckets, values are lists of salaries for that bucket
salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

salary_by_tenure_bucket

# Now let's compute the average salary for each group
# Keys are tenure buckets, values are the average salary for that bucket
average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

average_salary_by_bucket

# And voila! We have the soundbyte "Data scientists with more than five years experience earn 65% more than those with little or no experience"
# A wrinkle here is that we chose those buckets fairly arbitrarily... stay tuned!

# Let's try to predict who pays in the future.
# Say we notice that novices and experienced users pay, but average experienced users dont.
def predict_paid_or_unpaid(years_of_experience):
    if years_of_experience < 3.0:
        return "paid"
    elif years_of_experience < 8.5:
        return "unpaid"
    else:
        return "paid"


interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

# Topics of interest
# A simple way to find the most popular interests is to count the words
# step 1 - lowercase each interest
# step 2 - split it into words
# step 3 - count the results
words_and_counts = Counter(word
    for user, interest in interests
    for word in interest.lower().split())

for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)