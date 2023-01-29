import sys, os

if len(sys.argv) == 0:
    print("Github CLI Is Bad (GIB)")

if sys.argv[1] == "create":
    dir = os.getcwd()
    os.system(f"git -C \"{dir}\" init")
    os.system(f"gh repo create {sys.argv[2]} --source=\"{dir}\" --{sys.argv[3]}")
elif sys.argv[1] == "update":
    os.system("git add .")
    os.system(f"git commit -m \"{sys.argv[2]}\"")
    os.system("git push --set-upstream origin master")
elif sys.argv[1] == "remove":
    os.system("gh repo delete --yes")
    os.system("rmdir /s /q .git")