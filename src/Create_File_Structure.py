'''
Created on Mar 30, 2014

@author: roger
'''

Linux_OS = {
        'Type': ['CENTOS', 'RHEL'],
        'Version': ["5", "6"],
        'Purpose': ["extras", "updates"],
        'Arch': ["x86_64", "i386"],
        'default': 'package',
        }


for k, v in Linux_OS.iteritems():
    if k == 'Type':
        for i in v:
            if i == 0:
                pass
            else:
                for k, v in Linux_OS.iteritems():
                    if k == 'Version':
                        for x in v:
                            if x == 0:
                                pass
                            else:
                                for k, v in Linux_OS.iteritems():
                                    if k == 'Purpose':
                                        for y in v:
                                            if y == 0:
                                                pass
                                            else:
                                                for k, v in Linux_OS.iteritems():
                                                    if k == 'Arch':
                                                        for z in v:
                                                            if z == 0:
                                                                pass
                                                            else:
                                                                print i + '/' + x + '/' + y + '/' + z + "/Package"

if __name__ == '__main__':
    pass