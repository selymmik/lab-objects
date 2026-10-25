"""Build a feed for a community you choose.

See the course lab page for the demonstration checklist.
"""

from lab_classes import User, Tweet


def build_feed():
    # Create your accounts and posts, then call their methods.
    # Return the two lists: return users, posts

    a = User('Klein11') 
    t = Tweet('Klein11', 'So sad that EA is closing bioware #ScrewSaudiArabia #ScrewJaredKushner')
    t2 = Tweet('Klein11', 'I love John Kiriakou')
    b = User('BibiCandice')
    t3 = Tweet('BibiCandice', 'My favorite Mass Effect Game is ME Andromeda #NotSatire!')
    users = [a, b]
    posts = [t, t2, t3]
    a.follow()
    a.follow()
    a.unfollow()
    b.follow()
    b.follow()
    b.follow()
    t.like()
    t.like()
    t3.like()
    t3.unlike()
    t2.like()
    t2.like()
    t2.like()
    t2.unlike()

    return users, posts

    


def main():
    # Call build_feed and display the returned objects and hashtags.
    users, posts = build_feed()
    for user in users:
        print(user)
        print("Followers: " + str(user.followers))
    for post in posts:
        print(post)
        print("Likes: " + str(post.likes))
        print (post.hashtags())
    


if __name__ == '__main__':
    main()
