#!/usr/local/bin/python3
# Import Monday CLI libraries
from moncli import MondayClient
from moncli import BoardKind
from moncli import ColumnType
# Import Google Classroom functions
from gc_getCourses import getCourses

# Instantiating a new client interface to Monday.com
client = MondayClient(user_name='mikephamdavis@gmail.com', api_key_v1='eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjkxNTcxMzE0LCJ1aWQiOjE3Mjk4ODA2LCJpYWQiOiIyMDIwLTExLTIxVDE0OjQzOjE5LjAwMFoiLCJwZXIiOiJtZTp3cml0ZSJ9.G7UsLWL1XKlmClx5lFMxLK_yYG8f2WslO9idr3li09Y', api_key_v2='eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjkxNTcxMzE0LCJ1aWQiOjE3Mjk4ODA2LCJpYWQiOiIyMDIwLTExLTIxVDE0OjQzOjE5LjAwMFoiLCJwZXIiOiJtZTp3cml0ZSJ9.G7UsLWL1XKlmClx5lFMxLK_yYG8f2WslO9idr3li09Y')

# Creating a new board in the Main Workspace
board_name = 'New Public Board'
board_kind = BoardKind.public
new_board = client.create_board(board_name, board_kind)

# Getting a board by it's ID
board_id = '881643972'
board_by_id = client.get_board(id=board_id)

## Flow of activity to set up the Monday.com Google Classroom Agenda board:

# 1. Call Google Classroom API to get the list of courses
# 1a. First check to see if the board already exists
#board_name = 

# 2. Build a group called <UserName>'s Courses from the list returned above

# 3. For each course, get a list of Assignments and add them to a Monday group called Assignments

# 4. Determine next steps.

