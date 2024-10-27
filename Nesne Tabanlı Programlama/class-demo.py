class Comment:
    def __init__(self,username,text,likes,dislikes):
        self.username=username
        self.text=text
        self.likes=likes
        self.dislikes=dislikes
comment1=Comment("htunc29","Harika bir paylaşım",5,2)
comment2=Comment("bedis23","merhaba nasıl gidiyor hayat ?",12,2)
comment3=Comment("kingmiko20","Nasılsın ?",34,2)
comment4=Comment("memo2","Hangi manzaraya bakıyoruz ?",17,2)
comment5=Comment("higammze","Tatlım nasılsın ?",18,1)

comments=[comment1,comment2,comment3,comment4,comment5]
for comment in comments:
    print(f"{comment.username}:{comment.text} \n Like:{comment.likes} Dislike:{comment.dislikes} ")