import git
from lib.info import VERSION
git.Git(f".\\{VERSION}").clone("https://github.com/TheHerowither/Nebula-lang.git")