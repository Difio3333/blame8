import subprocess
import sys


def main():
    # in order to be able to count if a singular 


    # here is a list of the hooks we are using. Key is name of the hook, value is the command with which the terminal calls it, I think
    # the --edits make it so they don't actually change anyhting but just check and report errors
    # need to discuss this in person since the bottom three commands are behaving very arcanely.  
    hooks = {
        "isort": "isort . --check-only",
        "flake8": "flake8 . --check",
        "black": "black . --ignore=E501",
        "trailing-whitespace": "pre-commit run trailing-whitespace --all-files",
        "end-of-file-fixer": "pre-commit run end-of-file-fixer --all-files",
        "check-added-large-files": "pre-commit run check-added-large-files --all-files",
    }

    # would be cool to make this so it draws from .pre-commit-config.yaml dynamically

    error_counter = 0  # Track whether all hooks passed

    # this error_counter needs to be hooked up to a local json that counts permanentely.
    # but 

    for hook, command in hooks.items():
        if run_hook(hook, command) is False:
            error_counter += 1  # At least one hook failed

    # Exit with code 0 if all passed, 1 if any failed
    if error_counter == 0:
        sys.exit(0)
        #leads to "Success" output in prehook
    elif error_counter > 0:
        sys.exit(1)
        #leads to "Failed" output in prehook

def run_hook(hook_name, command) -> bool:
    verbose = False

   
    if "isort" in hook_name:
        pass

    elif "black" in hook_name:
        pass

    elif "flake8" in hook_name:
        pass

    else:
        verbose = True
        # make it so it's only talking when doing the integrated pre-commit hooks.

    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True)
        if verbose:
            print(f"{hook_name} passed!")
        return result.returncode == 0
        # this could just say return True I think but I'm too afraid to change it.
        #returncode = 0 is succes and 1 is failure.

    except subprocess.CalledProcessError:
        if verbose:
            print(f"{hook_name} failed!")
        return False


if __name__ == "__main__":
    print(
        "You don't want to run this file like this I think. This is only intended to be run as a yaml file."
    )
