from datetime import datetime
from turtle import title
from blog import db
from blog.models import Rating, User, Post

# Clear out existing database
db.drop_all()
# Create the database schema
db.create_all()
# Create objets representing data
user1 = User(username="test", password="passuser1", email="user1@test.ac.uk")


post1 = Post(title="Badminton", content="Badminton, initially known as Poona (or Poonah), its a sport that consists in players hitting a feather (or shuttlecock) with a racquet across a net and try to make it hit the ground on the other player’s side. This was part of my life growing up back in Portugal.\n” I joined the team back in 6th grade, all the way till university! It’s a fun sport that asks for team-work which actually helps with interpersonal relationships and gives you the opportunity to build friendships! Some of them which I still have to this day, and It is great to have shared this experience with them. Badminton is also a lot more physically demanding that most people think, you have to have fast reaction and movement in order to hit the feather properly and in time, so it is also a great cardio workout whilst being fun! I recommend to everyone who likes team sports and has wants to do some physical work to try badminton, its fun and simple to learn!", image_file="badminton.jpg")

post2 = Post(title="Video Games", content="I think I had my first ever desktop back when I was 6 years ago (2004), and I was so excited about games like Ball Pool and Minesweeper, and the legendary Tomb Raider!! I instantly got addicted and couldn’t stop playing. Until this day I still actively play with my friends, although not for long periods of time because, you know, life! Interesting enough, studies say that playing games is a great mental workout that will increase your problem-solving skills, reaction times, and imagination. As well as that, it has been proven to help reduce symptoms of stress, depression, and anxiety. And I can confirm this! When I play games with my peers, I feel very relaxed and at ease. It is a good leisure that people should try. It doesn’t necessarily have to be online, board games are just as efficient, if not better, due to the human interaction part of it. I play them every now and then and always have a good time! Give it a try and let me know how it feels!", image_file="gaming.jpg")

post3 = Post(title="Future Me", content="I sometimes think of the future, and where I will be, but I think we all do, no? Yes. I used to see myself as being part of a charity where I help people with domestic abuse and homelessness, and I saw myself that way for a long time, as long as I can remember really. But now I find myself thinking if that is really what I wanted to, because I wanted to help them, or was just reflecting what I felt about myself. But that is gone now. I think. I also saw myself joining the force as Police community support officer (PCSO) to help keep people safe, and whilst that is still in my mind, I am not sure what I want. Pretty complicated mind if mine right?! I would like to see myself working in something that I am passionate about. Is that IT? Maybe, maybe not. Policing? I don’t really know exactly what the future holds for me, but bring it in!",
             image_file="future.jpg")

# Add those objects to the database session
db.session.add(user1)
db.session.add(post1)
db.session.add(post2)
db.session.add(post3)

# Commit the database session
db.session.commit()
