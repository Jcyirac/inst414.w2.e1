#!/usr/bin/env python
# coding: utf-8

# In[29]:


import json
counter = 0
with open('imdb_movies_1985to2022.json') as in_file:
    for line in in_file:
        print(line)
        this_movie = json.loads(line)
        
        actors = this_movie['actors']
        for actor in actors:
            actor_name = actor[1]
            print("\t", actor_name)
            
        ratings = this_movie['rating']
        for rating in ratings:
            avg = rating
        
        counter += 1
        
        if counter > 5:
            break
        
        


# In[24]:


this_movie['rating']


# In[8]:


this_movie['actors']


# In[9]:


help(json.loads)


# In[10]:


json.loads(this_movie)


# In[ ]:




