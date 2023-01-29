import sys, os

if len(sys.argv) == 1:
    print("Github CLI Is Bad (GIB)\nFor the command list, go to https://github.com/Cintill/GIB/blob/master/commands.md")
    exit()

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
    os.system(f"rmdir /s /q \"{os.getcwd()}\\.git\"")

elif sys.argv[1] == "release":
    if sys.argv[2] == "create":
        if len(sys.argv) == 5:
            os.system(f"gh release create {sys.argv[3]} --title \"{sys.argv[4]}\" --generate-notes")
        elif sys.argv[5] == "notes-str":
            os.system(f"gh release create {sys.argv[3]} --title \"{sys.argv[4]}\" --notes \"{sys.argv[6]}\"")
        elif sys.argv[5] == "notes-file":
            os.system(f"gh release create {sys.argv[3]} --title \"{sys.argv[4]}\" --notes-file \"{sys.argv[6]}\"")

elif sys.argv[1] == "clone":
    os.system(f"git clone https://github.com/{sys.argv[2]}")