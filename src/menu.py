def banner():
    banner = open("src/banner.txt")
    print(f"\033[1;34m{banner.read()}")
    print(f"""
   \033[1;34m+----------------------------------*/
   \033[1;34mAuthor      : (\033[1;32mOlliv3r\033[1;34m)
   \033[1;34mFont Author : (\033[1;32mRemo7777\033[1;34m)
   \033[1;34m+----------------------------------*/\033[0m
    """)
