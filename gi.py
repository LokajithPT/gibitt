import os
import sys
from termcolor import colored

def banner():
    print(colored("""
              $$\ $$\       $$\   $$\     $$\     
          \__|$$ |      \__|  $$ |    $$ |    
 $$$$$$\  $$\ $$$$$$$\  $$\ $$$$$$\ $$$$$$\   
$$  __$$\ $$ |$$  __$$\ $$ |\_$$  _|\_$$  _|  
$$ /  $$ |$$ |$$ |  $$ |$$ |  $$ |    $$ |    
$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$\ $$ |$$\ 
\$$$$$$$ |$$ |$$$$$$$  |$$ |  \$$$$  |\$$$$  |
 \____$$ |\__|\_______/ \__|   \____/  \____/ 
$$\   $$ |                                    
\$$$$$$  |                                    
 \______/
                  """, "cyan"))

def help():
    print(colored("\n:: Git Repo Manager ::", "yellow"))
    print(colored(":: Commands ::", "green"))
    print(colored("(main) - Create repo, add, commit, push", "blue"))
    print(colored("(side) - Add, commit, push", "blue"))
    print(colored("(newbranch) - Create & switch to new branch", "blue"))
    print(colored("(verabranch) - Push to a specified branch", "blue"))
    print(colored("(changebranch) - change branches", "blue"))
    print(colored("(justadd) - Add files", "blue"))
    print(colored("(justcommit) - Commit changes", "blue"))
    print(colored("(justpush) - Push changes", "blue"))
    print(colored("(status) - Show Git status", "blue"))
    print(colored("(log) - Show commit history", "blue"))
    print(colored("(status) - Show Git status", "blue"))
    print(colored("(exit) - Quit the tool", "red"))

def main():
    banner()
    help()
    while True:
        val = input(colored("\n>>> ", "cyan")).replace(" ", "")
        if val == "main":
            name = input(colored("\nRepo name: ", "magenta"))
            mm = input(colored("Public or private (pu/pr): ", "magenta"))
            if mm == "pr":
                os.system(f"gh repo create {name} --private")
            elif mm == "pu":
                os.system(f"gh repo create {name} --public")
            else:
                print(colored("Invalid choice!", "red"))
                continue
            os.system(f"git remote add origin https://github.com/LokajithPT/{name}.git")
            os.system("git init && git add .")
            commit = input(colored("Commit message: ", "magenta"))
            os.system(f"git commit -m \"{commit}\"")
            os.system("git branch -M main && git push -u origin main")
        elif val == "branch":
            os.system("git branch")
        elif val == "side":
            os.system("git add .")
            commit = input(colored("Commit message: ", "magenta"))
            os.system("git branch -m main ")
            os.system(f"git commit -m \"{commit}\" && git push -u origin main")
        elif val == "newbranch":
            name = input(colored("New branch name: ", "magenta"))
            os.system(f"git branch {name} && git checkout {name}")
        elif val == "verabranch":
            name = input(colored("Branch name: ", "magenta"))
            os.system("git add .")
            commit = input(colored("Commit message: ", "magenta"))
            os.system(f"git commit -m \"{commit}\" && git push -u origin {name}")

        elif val == "changebranch":
            name = input(colored("New branch name: ", "magenta"))
            os.system(f"git checkout {name}")
            printf(colored("changing branch ..." , "magenta"))
        elif val == "log":
            os.system("git log --oneline")
        elif val == "status":
            os.system("git status")
        elif val == "exit":
            print(colored("Bye!", "red"))
            sys.exit()

        elif val == "help":
            help()
        else:
            print(colored("Invalid command! Type 'help' for options.", "red"))

main()

