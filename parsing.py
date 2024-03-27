# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parsing.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yroussea <yroussea@student.42angouleme.fr  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/26 23:56:01 by yroussea          #+#    #+#              #
#    Updated: 2024/03/27 00:07:03 by yroussea         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def open_file():
    if (0): #if you want to use a precise tab replace 0 by 1
        return []
    try:
        with open("anim.steps", "r", encoding="utf-8") as file:
            txt = file.read()
        tabs = []
        for line in txt.split("\n"):
            s = line.split()
            if s:
                tabs.append(list(map(float, s)))
        return tabs


    except:
        print("Error parsing")
        return [10, 3, 0, 2]
