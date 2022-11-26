Angle=int(input("what is the angle between ball and bat after batsman hit?"))
players = [
    {"player":" p1","Angle":0,"Distance": 5},
    {"player":" p2","Angle":20,"Distance":50},
    {"player":" p3","Angle":60,"Distance":30},
    {"player":" p4","Angle":80,"Distance":60},
    {"player":" p5","Angle":120,"Distance":70},
    {"player":" p6","Angle":180,"Distance":5},
    {"player":" p7","Angle":190,"Distance":5},
    {"player":" p8","Angle":200,"Distance":5},
    {"player":" p9","Angle":250,"Distance":60},
    {"player":" p10","Angle":330,"Distance":40},
    {"player":" p11","Angle":350,"Distance":60},
    ]
def place_players(angle):
   for player in players:
       if player["Angle"] in range(angle-10,angle+11):
           print (player["player"])
                 
place_players(Angle)  
  



