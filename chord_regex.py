#!/usr/bin/python

import re

class AttrDict(dict):  
    """ utility func, replaces AttrDict module on python3.7+ 
    gives object namespace to dictionaries"""
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

sharps = '𝄳𝄫♭b#♯'
note = f"[CDEFGAB][{sharps}]?"
root = f"(?P<root>{note})"
minor = "(?P<minor>m|min)?"
abrev = "(?P<shorts>add9|aug|maj[1379]|dim|sus[24]|6add9|7sus4|ø|o|°)?"
nums = f"(?P<nums>[1-9,+{sharps}-]{{0,7}})"
bass = f'(?P<bass>/[A-G])*'
regstr = rf'\b{root}{minor}{abrev}{nums}{bass}\b'
#regstr = rf'\b{root}{minor}{abrev}\b'
regex = re.compile(regstr)

replacements = {
    '7sus4': '7,4',
    'maj7':  '7+',
    'sus':   '',
    'dim':   'o',
    '°':     'o',
    '♯':     '#',
    '♭':     'b',
    '6add9': '6,9',

}

def normalize(chord):
    for old, new in replacements.items():
        chord = chord.replace(old, new)
    return chord

samples = {
    'A A♯5-7 Bb C#maj7 Chorus Dbsus2 Aba Ebm E79/C Ima Fø/F♯ F#dim G5+7- G#4 A♭6 Ar': '',
    'Yester[C#5+]day[Am]': '',
}

if __name__=='__main__':
  for sample in samples:
      print(sample)
      #results = regex.search(sample)
      results = regex.finditer(sample)
      print(results)
      for ret in results:
          d = AttrDict(ret.groupdict())
          d.root = normalize(d.root)
          print(d)
      print(' - - - - - - ')
  
