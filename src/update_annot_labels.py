#!/usr/bin/env python3

import os,sys
import nibabel as nib
import json

def load_annot(filepath):

    annotation = nib.freesurfer.read_annot(filepath)

    return annotation

def update_labels(labels):

    labels = [ f.decode() for f in labels ]
    labels.insert(0,'???')

    return labels

def save_annot(filepath,annotation_data,ctab,labels):

    nib.freesurfer.write_annot(filepath,annotation_data,ctab,labels)

def main():

    with open('config.json','r') as config_f:
        config = json.load(config_f)

    atlas = config['atlas']

    hemispheres = ['lh','rh']

    for hem in hemispheres:
        annot_file = './output/'+atlas+'/'+hem+'.'+atlas+'.annot'
        annotation_data, ctab, labels = load_annot(annot_file)
        labels = update_labels(labels)
        save_annot(annot_file,annotation_data,ctab,labels)

if __name__ == "__main__":
    main()
