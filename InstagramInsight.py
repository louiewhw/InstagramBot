#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 03:36:21 2019

@author: louiewhw
"""

from instaloader import Instaloader
from instaloader import Profile
import pandas as pd

class InstagramInsight:
    
        def getFollowList(self, userName, passWord):
            
            loader = Instaloader()
            loader.login(userName, passWord)  
            profile = Profile.from_username(loader.context, userName)
            followingList = []
            followerList = []
            
            for followee in profile.get_followees():
                followingList.append([followee.username, followee.followers, followee.followees])
            
                                
            followingList = pd.DataFrame(followingList, columns = ['username', 'followers', 'following'])
            followingList.to_csv('following.csv', index=False)
            
            
            for follower in profile.get_followers():
                followerList.append([follower.username, follower.followers, follower.followees])
            
            followerList = pd.DataFrame(followerList, columns = ['username', 'followers', 'following'])
            followerList.to_csv('follower.csv', index=False)
            
            
            
            notFollowBackList = followingList[~followingList.username.isin(followerList.username)]
            notFollowBackList.to_csv('notFollowingBack.csv', index=False)
                
            unfollowList = notFollowBackList[notFollowBackList.followers<1000]
            unfollowList.to_csv('unfollowList.csv', index = False)
            
if __name__ == "__main__":
    ints = InstagramInsight()
    user
    pw
    ints.getFollowList(user, pw)
