#Github Repo Information Tool 
#Repos
#Made By Muhammad Rafli
#!/usr/bin/python

import os

os.system("clear")



class color:
    header = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    white = '\033[0m'
    b = '\033[1m'
    ul = '\033[4m'
    bgreen = '\033[1;92m'
    bred = '\033[1;91m'
    byellow = '\033[1;93m'
    bblue = '\033[1;94m'
    bheader = '\033[1;95m'
    
color()

def rep1():
    api2 = api+sys.argv[2]
    apt = urlopen(api2).read().decode('UTF-8')
        #print(apt)
    #print(color.bheader+"\nInformation Starting....")
    rep = json.loads(apt)
    print(color.bgreen+"[i] User Name           "+color.white+'',rep["login"])
    print(color.bgreen+"[i] Id                  "+color.white+'',rep["id"])
    print(color.bgreen+"[i] Node Id             "+color.white+'',rep["node_id"])
    print(color.bgreen+"[i] Profile Pic Url     "+color.white+'',rep["avatar_url"])
    print(color.bgreen+"[i] Gravatar Id         "+color.white+'',rep["gravatar_id"])
    print(color.bgreen+"[i] Url                 "+color.white+'',rep["html_url"])
    print(color.bgreen+"[i] Type                "+color.white+'',rep["type"])
    print(color.bgreen+"[i] Site Admin          "+color.white+'',rep["site_admin"])
    print(color.bgreen+"[i] Name                "+color.white+'',rep["name"])
    print(color.bgreen+"[i] Company Name        "+color.white+'',rep["company"])
    print(color.bgreen+"[i] Blog                "+color.white+'',rep["blog"])
    print(color.bgreen+"[i] Location            "+color.white+'',rep["location"])
    print(color.bgreen+"[i] Email               "+color.white+'',rep["email"])
    print(color.bgreen+"[i] Bio Data            "+color.white+'',rep["bio"])
    print(color.bgreen+"[i] Repostorie          "+color.white+'',rep["public_repos"])
    print(color.bgreen+"[i] Gists               "+color.white+'',rep["public_gists"])
    print(color.bgreen+"[i] Followers           "+color.white+'',rep["followers"])
    print(color.bgreen+"[i] Following           "+color.white+'',rep["following"])
    print(color.bgreen+"[i] Hireable            "+color.white+'',rep["hireable"])
    print(color.bgreen+"[i] Create Date & Time  "+color.white+'',rep["created_at"])
    print(color.bgreen+"[i] Updated Date & Time "+color.white+'',rep["updated_at"])
    
def repz():    
    mb = "https://api.github.com/users/"+sys.argv[2]+"/repos"
    vb = urlopen(mb).read().decode("utf-8")
    rw = json.loads(vb) 
    #print(banner)
     #print(color.byellow+"\n[Â°] Repostories Information.....")
     


    asd = "https://api.github.com/users/"+sys.argv[2]
    sd = urlopen(asd).read().decode("utf8")
    de = json.loads(sd)
    gh = de["public_repos"]
    for x in range(gh):
        print(color.bheader+"[+] Next Repo* Information.....\n")
        print(color.bgreen+"[",x,"] Repo* Name             "+color.white+'',rw[x]["name"])
        print(color.bgreen+"[i] Description               "+color.white+'',rw[x]["description"])
        print(color.bgreen+"[i] Url                       "+color.white+'',rw[x]["html_url"])
        print(color.bgreen+"[i] Clone Url                 "+color.white+'',rw[x]["clone_url"])
        print(color.bgreen+"[i] Mirror Url                "+color.white+'',rw[x]["mirror_url"])
        print(color.bgreen+"[i] Archived                  "+color.white+'',rw[x]["archived"])
        print(color.bgreen+"[i] Private                   "+color.white+'',rw[x]["private"])
        
        
        print(color.bgreen+"[i] Language                  "+color.white+'',rw[x]["language"])
        print(color.bgreen+"[i] Homepage                  "+color.white+'',rw[x]["homepage"])
        print(color.bgreen+"[i] Size                      "+color.white+'',rw[x]["size"])
        print(color.bgreen+"[i] Git Url                   "+color.white+'',rw[x]["git_url"])
        print(color.bgreen+"[i] Ssh Url                   "+color.white+'',rw[x]["ssh_url"])
        print(color.bgreen+"[i] Issues                    "+color.white+'',rw[x]["has_issues"])
        print(color.bgreen+"[i] Project                   "+color.white+'',rw[x]["has_projects"])
        print(color.bgreen+"[i] Wiki                      "+color.white+'',rw[x]["has_wiki"])
        print(color.bgreen+"[i] Pages                     "+color.white+'',rw[x]["has_pages"])
        print(color.bgreen+"[i] Open Issues               "+color.white+'',rw[x]["open_issues_count"])
        print(color.bgreen+"[i] Branch                    "+color.white+'',rw[x]["default_branch"])
        print(color.bgreen+"[i] License                   "+color.white+'',rw[x]["license"])
        
        print(color.bgreen+"[i] Stargazer(s)              "+color.white+'',rw[x]["stargazers_count"])
        print(color.bgreen+"[i] Watcher(s)                "+color.white+'',rw[x]["watchers_count"])
        print(color.bgreen+"[i] Created Date & Time       "+color.white+'',rw[x]["created_at"])
        print(color.bgreen+"[i] Updated Date & Time       "+color.white+'',rw[x]["updated_at"])
       
       
       # print(color.bred+"[+] Next Repo Information......")
        print(color.white+'')

def follo():
    dc = urlopen(api+sys.argv[2]).read().decode('utf-8')
    tt = json.loads(dc)
    dd = tt["followers"]
    g = "https://api.github.com/users/"+sys.argv[2]+"/followers"
    zx = urlopen(g).read().decode('utf-8')
    xz = json.loads(zx)
    for x in range(dd):
        print(color.bblue+"\n[+] Followers (",x,")\n")
        print(color.bgreen+"[i] Username                "+color.white+'',xz[x]["login"])
        print(color.bgreen+"[i] Id                      "+color.white+'',xz[x]["id"])
        print(color.bgreen+"[i] Node Id                 "+color.white+'',xz[x]["node_id"])
        print(color.bgreen+"[i] Profile Pic Url         "+color.white+'',xz[x]["avatar_url"])
        print(color.bgreen+"[i] Gravatar Id             "+color.white+'',xz[x]["gravatar_id"])
        print(color.bgreen+"[i] Type                    "+color.white+'',xz[x]["type"])
        print(color.bgreen+"[i] Site Admin              "+color.white+'',xz[x]["site_admin"])
        print("\n----------------------------------------------\n")

api = "https://api.github.com/users/"
banner = color.bblue+'''
    
   _____ _____ _______ _    _ _    _ ____  
  / ____|_   _|__   __| |  | | |  | |  _ \ 
 | |  __  | |    | |  | |__| | |  | | |_) |
 | | |_ | | |    | |  |  __  | |  | |  _ < 
 | |__| |_| |_   | |  | |  | | |__| | |_) |
  \_____|_____|  |_|  |_|  |_|\____/|____/ 
                                           
'''+color.bred+"[x] Information Github Repositories!\n"+color.bheader+"____________Kalsel[E]Xploit___________\n"+color.white+"\t-----Muhammad Rafli-----"
from urllib.request import urlopen

def about():
    print(color.byellow+"Author Name  â†’  M.Rafli")
    print(color.bblue+"TEAM : Kalsel[E]Xploit"+color.white+'')
    
def ver():
    print(color.bheader+"GITHUB-USER Version v2.0")
    print(color.byellow+"New Update Coming Soon With New Features."+color.white+'')
def usage():
    print(color.byellow+"Usage : "+color.green+"python",sys.argv[0] ,"-h")
try:
    import sys, json
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        comand = '''
    Command Option: 
        -h or --help        For Help
        -u or --user        For User Id Information
        -r or --repo        For Repostories Gethering
        -f or --follower    Find All Followers
        -sa or --show_all   Show All Information
        -a or --about       About Author
        -v or --version     Check Version With Updated
        
        Example : python github.py -u RabbitCL4Y
                  python github.py -r RabbitCL4Y
        '''
        print(banner)
        usage()
        print(color.white+comand)
   
    
    elif sys.argv[1] == '-u' or sys.argv[1] == '--user':
        print(banner)
        print(color.byellow+" \n[Â°] Information Gethering Starting.....")
        #api2 = api+sys.argv[2]
    #    apt = urlopen(api2).read().decode('UTF-8')
        #print(apt)
        rep1()
        
    elif sys.argv[1] == '-r' or sys.argv[1] == '--repo':
        print(banner)
        print(color.byellow+"\n[Â°] Repostories Information....\n")
        repz()
    
    elif sys.argv[1] == '-f' or sys.argv[1] == '--follower':
        print(banner)
        print(color.byellow+"\n[Â°] Followers Information....\n")
        follo()
        
    elif sys.argv[1] == '-sa' or sys.argv[1] == '--show_all':
        print(banner)
        print("\n[Â°] Information Gethering.....\n")
        rep1()
        print("\n[Â°] Repostories Information....\n")
        repz()
        print("\n[Â°] Followers Information.....\n")
        follo()
    
    elif sys.argv[1] == '-a' or sys.argv[1] == '--about':
        print(banner)
        print(color.bblue+"\n[Â°] About Author....\n") 
        about()
    
    elif sys.argv[1] == '-v' or sys.argv[1] == '--version':
        print(banner)
        print(color.bblue+"\n[Â°] Check Version....\n")
        ver()
        
    else:
        print(banner)
        print(color.bred+"\n\n \t    ðŸ˜ˆ Wrong Command ðŸ˜ˆ"+color.white+'')
        usage()
except:    
    print(banner)
    usage()
