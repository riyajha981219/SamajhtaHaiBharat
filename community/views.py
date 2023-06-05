from django.shortcuts import render,redirect
from .models import *
# Create your views here.


## main page of community
def index(request, commid, memid):
    communities = Map.objects.get(pk=commid)
    posts = communities.group.all()
    member= Member.objects.get(pk=memid)
    memid=member.id
    return render(request,"community/index.html",{
        "posts":posts,
        "memid":memid,
        "commid":commid,
        "community":communities.name
    })


## add a post to some community    
def add_post(request, commid, memid):
    if request.method=="POST":
        member = Member.objects.get(pk=memid)
        community = Map.objects.get(pk=commid)
        post = Post()
        post.user= member
        post.status= request.POST["status"]
        post.community=community
        try:
            post.save()
        except:
            ValueError("Didn't work")
            return render(request,'community/addpost.html',{
                "error":"Internal Server Error",
                "memid":memid,
                "commid":commid
            })
        return redirect('community:index', commid, memid)
    return render(request, "community/addpost.html",{
        "memid":memid,
        "commid":commid
    })


## personal profile of anybody
def profile(request,memid,name,commid):
    member= Member.objects.get(nickname=name)
    loggedinmember = Member.objects.get(pk=memid)
    posts=member.poster.all()
    if member.id == loggedinmember.id:
        return redirect("community:memberpage", memid, commid)
    
    return render(request, "community/profile.html",{
        "posts":posts,
        "member":member,
        "memid":memid,
        "commid":commid
    })


## Logged in member's post
def mem_post(request, memid,commid):
    loggedmember=Member.objects.get(pk=memid)
    name = loggedmember.nickname
    posts= loggedmember.poster.all()
    return render(request,"community/member_profile.html",{
        "memid":loggedmember.id,
        "name":loggedmember,
        "commid":commid,
        "postlist":posts,
        "edityes":0
    })

## delete your post
def del_post(request,postid):
    post= Post.objects.get(pk=postid)
    comm= post.community
    username= CustomUser.objects.get(pk=request.user.id)
    allmember= Member.objects.get(user=username,community=comm)
    try:
        post.delete()
    except:
        return render(request, "community/member_profile.html",{
            "status":"Couldn't delete post! Try again later!",
            "commid":comm
        })
    return redirect('community:memberpage', allmember.id, comm.id)


## post a comment
def post_comment(request,memid, postid,commid):
    post=Post.objects.get(pk=postid)
    member= Member.objects.get(pk=memid)
    try:
        comments= Comment.objects.filter(post=post)
        mycomments= Comment.objects.filter(post=post,commenter=member)
    except:
        comments=None
        mycomments=None
    if request.method == "POST":
        comment= Comment()
        comment.comment= request.POST["comment"]
        comment.commenter=Member.objects.get(pk=memid)
        comment.post=Post.objects.get(pk=postid)
        try:
            comment.save()
        except:
            return render(request,"community/comment.html",{
                "mem":memid,
                "post":postid,
                "commid":commid,
                "edityes":0,
                "status":"Couldn't post the comment. Try again later!"
            })
        return redirect('community:comment', memid,postid,commid)
    return render(request, "community/comment.html",{
            "memid":memid,
            "post":post,
            "commid":commid,
            "edityes":0,
            "mycomments":mycomments,
            "comments":comments
        })
   
## delete comment         
def del_comment(request, commentid, memid, postid,commid):
    try:
        comment= Comment.objects.get(pk=commentid)
        comment.delete()
    except:
        comment=None
    return redirect('community:comment', memid,postid,commid)


## edit your post
def edit(request, memid, postid, commid):
    edityes = 1
    post = Post.objects.get(pk=postid)
    if request.method == "POST":
        newstatus= request.POST["status"]
        post.status = newstatus
        edityes=0
        try:
            post.save(update_fields=["status",])
        except:
                return render(request,"community/comment.html",{
                "commid":commid,
                "memid":memid,
                "post": post,
                "edityes": edityes,
                "status":"Couldn't edit the post! Try again later!"       
            })
        else:
            return redirect("community:memberpage", memid, commid)        
    return render(request,"community/comment.html",{
        "memid":memid,
        "commid":commid,
        "post":post,
        "edityes": edityes
    })


## like a post
# def post_like(request, memid, postid, commid):
#     post=Post.objects.get(id=postid)
#     posts = Post.objects.all()
#     member= Member.objects.get(id=memid)
#     likes = post.specpost.all()
#     liked = PostLikes.objects.all()
#     state = request.POST["postbutton"]
#     if member in likes:
#         state = 0
#         return render("community/index.html",{
#         "commid":commid,
#         "memid":memid,
#         "state": state
#     })
#     if request.method == "POST":
#         print(request.POST["postbutton"])
#         if request.POST["postbutton"] == 1:
#             liked.user = member
#             liked.post = post
#             try: 
#                 liked.save()
#                 post.likes +=1
#                 post.save(update_fields=["likes"])
#                 state = 1
#                 return render(request, "community/index.html",{
#                     "commid":commid,
#                     "post":posts,
#                     "memid":memid,
#                     "state":1
#                 })
#             except:
#                 return render(request, "community/index.html",{
#                     "commid":commid,
#                     "post":posts,
#                     "memid":memid,
#                     "state":state,
#                     "status":"Couldn't like the post. Try again later"
#                 })    
#         return render(request, "community/index.html",{
#         "commid":commid,
#         "memid":memid,
#         "posts":posts,
#         "state": state
#     })
    
