# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 13:42:33 2019

@author: Fang
"""

#%%
import os
import pandas as pd

cwd = os.getcwd()

import igtv_helpers

os.chdir(cwd)

#%%
class igtv_show:
    
    def __init__(self, ig_handle):
        
        self.ig_handle = ig_handle
        self.show_url = 'https://www.instagram.com/{0}/channel/?hl=en'.format(ig_handle)
        self.summary_engagements = None
        self.post_source_list = []
        self.posts = None
        self.can_pull_sources = False
        
    def get_show_info(self):
        self.summary_engagements, self.post_source_list = igtv_helpers.get_main_html_source(self.show_url, 
                                                                                            cwd, 
                                                                                            self.ig_handle)
        
        self.can_pull_sources = True
        
    def get_show_posts(self):
        if self.can_pull_sources:
            self.posts = pd.concat([igtv_helpers.get_show_posts_df(self.ig_handle, source) for source in self.post_source_list], axis = 0)
            self.posts = self.posts.drop_duplicates().reset_index(drop = True)
            
        
    def __str__(self):
        output_string = '''Show IG URL: {0} \n Summary Engagements: {1} \n Post Counts {2}'''
        
        if self.summary_engagements == None:
            engagement_summary = None
        else:
            engagement_summary = str(self.summary_engagements)
        
        if self.posts == None:
            post_counts = None
        else:
            post_counts = len(self.posts)
        
        return output_string.format(self.show_url,
                                    engagement_summary,
                                    post_counts)
