#!/usr/bin/env python

import sys
import subprocess
import optparse
import shutil
import os

##########################################
## Options and defaults
##########################################
def getOptions():
    parser = optparse.OptionParser('python trinity_pipeline.py [option]"')
    parser.add_option('--left',dest='left',help='/1 file for pair-end data', default='')
    parser.add_option('--right',dest='right',help='/2 file for pair-end data', default='')
    parser.add_option('--single',dest='single',help='single-end data', default='')
    parser.add_option('--project',dest='project',help='project name used of filename', default='project')
    parser.add_option('--out',dest='outdir',help='directory for output', default=os.getcwd())
    parser.add_option('--trinity',dest='trinityOptions',help='Trinity options that are passed to the command line, e.g. --seqType fa --JM 50G', default='')
    parser.add_option('--cap3',dest='cap3Options',help='cap3 options that are passed to the command line, e.g. -p 98 -o 50', default='')
    parser.add_option('--cdhit',dest='cdhitOptions',help='cdhit options that are passed to the command line, e.g. -c 0.98 -G 0 -aS 0.90', default='')
    parser.add_option('--cpu',dest='cpu',type="int",help='number of cpu',default=1)
    options, args = parser.parse_args()
    paired='n'
    same='y'
    if (options.left!='' or options.right!=''):
        paired='y'
    if (options.left!='' and options.right=='') or (options.left=='' and options.right!=''):
        same='n'
    #print same
    if (options.single=='' and paired!='y') or (options.single!='' and same=='n'):
        parser.print_help()
        print ''
        print 'You forgot to provide some data files!'
        print 'Current options are:'
        print options
        sys.exit(1)
    return options

def checkProgram(program):
	try:
	    p = subprocess.Popen([program], stdout=subprocess.PIPE)
	    return True
	except OSError:
	    print "Could not find %s" % (program)
	    print "Make sure that it is properly installed on your path"
	    sys.exit(1)
	    assert False


def run_trinity(options,left,right,outpath):
	os.chdir(outpath)
	if left=='' and right=='':
		tr_line="Trinity.pl --single %s --CPU %s --inchworm_cpu %s --bflyCPU %s %s --output %s" % (options.single,options.cpu,options.cpu,options.cpu,options.trinityOptions,outpath)
	else:
		tr_line="Trinity.pl --left %s --right %s --CPU %s --inchworm_cpu %s --bflyCPU %s %s --output %s" % (left,right,options.cpu,options.cpu,options.cpu,options.trinityOptions,outpath)
	print tr_line
	os.popen(tr_line)
	
def run_cap3_cdhit(options,trinity_cp):
    cap3_line="cap3 %s %s" % (trinity_cp,options.cap3Options)
    print cap3_line
    os.popen(cap3_line)
    os.popen("cat %s.fa.cap.contigs %s.fa.cap.singlets > %s_combine.fa" % (options.project,options.project,options.project))
    cdhit_line="cd-hit-est -i %s_combine.fa -o %s.cdhit.fa -T %s %s" % (options.project,options.project,options.cpu,options.cdhitOptions)
    print cdhit_line
    os.popen(cdhit_line)
    contig_name=options.project+'_contig'
    rename_line="python /share1/scripts/kw/fa_rename.py -in %s.cdhit.fa -pfix %s -out %s.cdhit.rename.fa" % (options.project,contig_name,options.project)
    os.popen(cdhit_line)
    

##########################################
## Master function
##########################################
def main():
    options = getOptions()
    try:
        if options.left[0]!='/':
            options.left=os.getcwd()+'/'+options.left
    except:
        pass
    try:
        if options.right[0]!='/':
            options.right=os.getcwd()+'/'+options.right
    except:
        pass
    try:
        if options.single[0]!='/':
            options.single=os.getcwd()+'/'+options.single
    except:
        pass
    

    print "option:"
    
    
    for i in ['Trinity.pl','cap3','cd-hit-est']:
        checkProgram(i)
    
        
    if options.outdir[0]!='/':
        options.outdir=os.getcwd()+'/'+options.outdir
    if options.outdir[-1]!='/':
        outpath=options.outdir+'/'
    else:
        outpath=options.outdir
    trinity_dir=outpath+'trinity'
    print options
    try:
        os.mkdir(trinity_dir)
    except:
        pass
    os.chdir(trinity_dir)
    if options.single!='' and options.left!='' and options.right!='':
        left=trinity_dir+"/"+os.path.split(options.left)[1]+'.new.'+options.left.split('.')[-1]
        print "cat single and paire end data...%s" % left
        print ('cat %s %s > %s' % (options.left,options.single,left))
        os.popen('cat %s %s > %s' % (options.left,options.single,left))
        right=options.right
    else:
        left=options.left
        right=options.right
    print "running trinity"
    run_trinity(options,left,right,trinity_dir)
    cap3_cdhit_dir=outpath+'cap3_cdhit/'
    try:
        os.mkdir(cap3_cdhit_dir)
    except:
        pass
    os.chdir(cap3_cdhit_dir)
    trinity_result=trinity_dir+'/Trinity.fasta'
    trinity_cp=cap3_cdhit_dir+options.project+'.fa'
    os.popen("cp %s %s" % (trinity_result,trinity_cp))
    print "running cap3 and cdhit"
    run_cap3_cdhit(options,trinity_cp)
    #os.popen("rm -rf %s" % trinity_dir)
      
if __name__ == "__main__":
	main()
