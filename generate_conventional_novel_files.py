import xml.etree.ElementTree as ET
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np

# Download the necessary resources if not already downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

tree = ET.parse('VUAMC_with_novelty_scores.xml')
root = tree.getroot()

ns = {'default': 'http://www.tei-c.org/ns/1.0'}
s_tags = root.findall(".//default:s", namespaces=ns)
print("Total number of sentences =",len(s_tags))

all_sentences=[]
all_literal_sentences=[]
literal_sentences_count=0
metaphor_sentences_count=0
num=0
for s_tag in s_tags:
    num+=1
    sentence=[]
    count=0
    all_metaphor_idx=[]
    scores=[]
    flag=1
    for child in s_tag:
      if len(child)>0:
        if "type" not in child.attrib.keys():
          continue
        for children in child:
          if "score" not in  children.attrib.keys():

            sentence.append(children.text.replace(" ","").replace("\n",""))
          else:
            sentence.append(children.text.replace(" ","").replace("\n",""))
            #print(children.tag,children.attrib,children.attrib.keys(),children.text)
            scores.append(children.attrib["score"])
            all_metaphor_idx.append(count)

          count+=1

      else:
        #For Punctuations, adding them to the previous word itself so that it doesn't count as another index.
        #print(child.attrib.keys())
        if "type" not in child.attrib.keys():
          continue
        if child.attrib["type"]=="PUN":
          if len(sentence)>0:
            last_word=sentence[-1]
            last_word=last_word+child.text
            sentence[-1]=last_word
          else:
            sentence.append(child.text.replace(" ","").replace("\n",""))
            flag=0
        else:
          if flag==0 and len(sentence)>0:
            last_word=sentence[-1]
            last_word=last_word+child.text
            sentence[-1]=last_word
            count+=1
            flag=1
          else:

            sentence.append(child.text.replace(" ","").replace("\n",""))
            count+=1
    sentences=" ".join(e for e in sentence)
    if len(all_metaphor_idx)==0:
      literal_sentences_count+=1
      #ind=len(sentence)
      #print(sentence)
      sent=" ".join(e for e in sentence)
      ind=len(sent)
      tokens = word_tokenize(sent)
      pos_tags = pos_tag(tokens)

      sentence_length=len(sent)
      curr_ind=0
      for word,tag in pos_tags:
        if tag[0]=="V" and tag[1]=="B":
        #print("Verb")
            all_literal_sentences.append((sent,curr_ind))
        curr_ind+=1
        break
    if len(all_metaphor_idx)>0:
      metaphor_sentences_count+=1
    if len(all_metaphor_idx)==len(scores):
      pass
    else:
      print("Number of metaphor indices and scores do not match")

    for i in range(len(all_metaphor_idx)):
      all_sentences.append((sentence,all_metaphor_idx[i],scores[i]))
    #print(num,len(all_sentences))
print("Number of literal sentences = ",len(all_literal_sentences))
print("Number of metaphor sentences = ",metaphor_sentences_count)

if len(all_literal_sentences)+metaphor_sentences_count==len(s_tags):
  print("The literal sentences and metaphors sentences match the total number of sentences")
else:
  print("DOES NOT MATCH!!!")

print("Number of metaphorical sentences (a sentences may be counted twice if it has multiple)",len(all_sentences))


columns=["label","sentence","pos","v_index"]
conventional_metaphors=[]
novel_metaphors=[]
for i in range(len(all_sentences)):
  if float(all_sentences[i][2])>0.3:
    curr_lis=[]
    curr_lis.append(1)
    sent=" ".join(e for e in all_sentences[i][0])

    curr_lis.append(sent)
    curr_lis.append("verb")
    curr_lis.append(int(all_sentences[i][1]))
    novel_metaphors.append(curr_lis)
  else:
    curr_lis=[]
    curr_lis.append(1)
    sent=" ".join(e for e in all_sentences[i][0])
    curr_lis.append(sent)
    curr_lis.append("verb")
    curr_lis.append(int(all_sentences[i][1]))
    conventional_metaphors.append(curr_lis)

conventional_df = pd.DataFrame(conventional_metaphors, columns=columns)
novel_df = pd.DataFrame(novel_metaphors, columns=columns)

print("The shape of conventional dataframe is ",conventional_df.shape)
print("The shape of Novel dataframe shape is ",novel_df.shape)

#conventional_df.to_csv("conventional.tsv",index=True,sep="\t")
#novel_df.to_csv("novel.tsv",index=True,sep="\t")
