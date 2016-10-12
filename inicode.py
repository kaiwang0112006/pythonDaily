# -*- coding: utf-8 -*-
import argparse
import base64
import ConfigParser

##########################################
## Options and defaults
##########################################
def getOptions():
    parser = argparse.ArgumentParser(description='python *.py [option]"')
    requiredgroup = parser.add_argument_group('required arguments')
    requiredgroup.add_argument('--in', dest='input', help='input,required', default='', required=True)
    parser.add_argument('--out',dest='output',help='output', default='output.ini')
    parser.add_argument('--encode',dest='encode',help='true or false', default='true')
    args = parser.parse_args()

    return args

def base64Encode(code):
    return base64.b64encode(code)
def base64Decode(code):
    return base64.b64decode(code)



##########################################
## Master function
##########################################           
def main():
    options = getOptions()
    if options.encode == 'true':
        trans = base64Encode
    else:
        trans = base64Decode
        
    configin = ConfigParser.ConfigParser()  
    
    configin.readfp(open(options.input))
    secs = configin.sections()
    print secs
    for sec in secs:
        opts = configin.options(sec)
        
        for opt in opts:
            val = configin.get(sec, opt)
            #print sec,opt,val
            configin.set(sec, opt, trans(val))
    

    configin.write(open(options.output, "w"))

if __name__ == "__main__":
    main()