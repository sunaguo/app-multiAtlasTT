__author__ = 'jfaskowitz'

'''
josh faskowitz
Indiana University
Computational Cognitive Neurosciene Lab

Copyright (c) 2018 Josh Faskowitz
See LICENSE file for license
'''

import numpy as np
import nibabel as nib
from sys import argv
import json

def main():

    i_file = str(argv[1])
    o_file = str(argv[2])
    labs_file = str(argv[3])

    i_img = nib.load(i_file)
    i_data = i_img.get_data()

    # get labs from first colum of LUT table
    labs = [x.split()[0] for x in open(labs_file).readlines()]  
    names = [x.split()[1] for x in open(labs_file).readlines()]  

    # init o_data
    o_data = np.zeros(i_data.shape,dtype=np.int32)
        
    labels=[]

    # print remap to file
    with open(o_file+'_remapKey.txt','w') as f:
        for x in range(0,len(labs)):
            w = np.where(i_data == int(labs[x]))
            o_data[w[0],w[1],w[2]] = (x + 1)

            f.write( "{}\t->\t{}\t== {} \n".format(str(labs[x]), str(x + 1), str(names[x]) ) ) 
            labels.append({'name': names[x], 'label': labs[x], 'voxel_value': (x+1)})

    # add 14 regions to label
    f14 = [
            {"name": "Freesurfer Aseg / Left thalamus", "label": "10"},
            {"name": "Freesurfer Aseg / Left caudate", "label": "11"},
            {"name": "Freesurfer Aseg / Left putamen", "label": "12"},
            {"name": "Freesurfer Aseg / Left pallidum", "label": "13"},
            {"name": "Freesurfer Aseg / Left hippocampus", "label": "17"},
            {"name": "Freesurfer Aseg / Left amygdala", "label": "18"},
            {"name": "Freesurfer Aseg / Left accumbens", "label": "26"},

            {"name": "Freesurfer Aseg / Right thalamus", "label": "49"},
            {"name": "Freesurfer Aseg / Right caudate", "label": "50"},
            {"name": "Freesurfer Aseg / Right putamen", "label": "51"},
            {"name": "Freesurfer Aseg / Right pallidum", "label": "52"},
            {"name": "Freesurfer Aseg / Right hippocampus", "label": "53"},
            {"name": "Freesurfer Aseg / Right amygdala", "label": "54"},
            {"name": "Freesurfer Aseg / Right accumbens", "label": "58"},
    ]
    for x in range(0,14):
        labels.append({'name': f14[x]['name'], 'label': f14[x]['label'], 'voxel_value': (x+len(labs)+1)})

    with open(o_file+'_label.json','w') as labeljson:
        json.dump(labels, labeljson)

    # save output
    o_img = nib.Nifti1Image(o_data, i_img.get_affine())
    nib.save(o_img, o_file)

if __name__ == '__main__':
    main()
