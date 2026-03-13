import subprocess


def open_firefox():
    subprocess.run(["firefox", "&"], shell=True)


if __name__ == "__main__":
    open_firefox()
