from git import Repo,GitCommandError
import sys
import csv
import os

def git_clone(roster_file_name,basedir,repo_prefix):
    os.makedirs(basedir, exist_ok=True)
    os.chdir(basedir)

    with open(f"../{roster_file_name}") as rosterf:
        roster_reader = csv.reader(rosterf)
        skip = next(roster_reader)

        for line in roster_reader:
            bc_id = line[1]
            git_id = line[2]
            repo_url = f"git@github.com:BC-CSCI1101-Wiseman-Fall2023/{repo_prefix}{git_id}"
            local_dir = f"{bc_id}"
            try:
                Repo.clone_from(repo_url, local_dir)
            except GitCommandError:
                print(f"Error with {bc_id}'s repo.", file=sys.stderr)

    os.chdir("..")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python clone_assignment.py roster.csv assignment_number")
        print("example: python clone_assignment.py grading-Charlie.csv 1")
        sys.exit()

    roster_file_name = sys.argv[1]
    assignment_number = sys.argv[2]
    basedir = f"a{assignment_number}"
    repo_prefix = f"csci1101-assignment-{assignment_number}-"

    try:    
        git_clone(roster_file_name, basedir, repo_prefix)
    except OSError:
        print(f"Error with {roster_file_name}?")
        sys.exit()
