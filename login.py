# -*- coding: utf-8 -*-
import itchat


itchat.login()

filename = itchat.search_friends()

itchat.send_msg('11111', toUserName=filename)


itchat.logout()
