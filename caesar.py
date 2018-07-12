#coded by nabla t3ch channel on youtuble
#youtube.com/nablat3ch
#mohammed abdo al-muntalib
import sys
import getopt
class caesar:
    def usage(self):
        help="""\
        Usage:
        caesar --mode=encrypt|decript  --key=num
        caesar -d |-e --key=num
        default num=13
        """
        return help
    def cliopt(self):
        global mode
        global opts
        global args
        global key
        key=13   #default key=13
        try:
            opts,args=getopt.getopt(sys.argv[1:],"de",["mode=","key="])
        except getopt.GetoptError as ERR:
            print(ERR)
            self.usage()
            sys.exit(1)

        for o, a in opts:
            if o in ('-d'):
                mode='decrypt'
            elif o in ('-e'):
                mode='encrypt'
            elif o in ('--mode'):
                #mode=a
                if a == 'encrypt':
                    mode=a
                elif a == 'decrypt':
                    mode=a
                else:
                    print("""\
ERR on mode= must be
mode=decrypt
mode=encrypt
                    """)
                    sys.exit(1)
            elif o in ("--key"):
                if type(int(a)) == type(7):
                    key=int(a)
                else:
                    print("key arg must be number you enter {}" .format(type(a)))
                    sys.exit(1)
            else:
                assert False, 'an ERR occurred through handling options'
                #print("ERRRRRRRRRRRR")
                sys.exit(1)
        return True
    def main(self):
        plantxt=sys.stdin.read()
        #key=13
        #mode='encrypt'
        #mode='decrypt'
        LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ciphertxt=''
        plantxt=plantxt.upper()
        for i in plantxt:
            if i in LETTERS:
                num=LETTERS.find(i)
                if mode=='encrypt':
                    num=num+key
                elif mode=='decrypt':
                    num=num-key

                if num >=len(LETTERS):
                    num=num-len(LETTERS)
                elif num < 0:
                    num=num+len(LETTERS)
                ciphertxt=ciphertxt+LETTERS[num]

            else:
                pass
                #ciphertxt=ciphertxt+i
        print(ciphertxt)


obj=caesar()
if not len(sys.argv[1:]):
     #print("no arg")
     print(obj.usage())
     sys.exit(1)
global mode
global opts
global args

chh=obj.cliopt()
if chh:
    if __name__ == '__main__':
        obj.main()
else:
    print("""\
there are an ERR occurred
check you code :(
:(
    """)
