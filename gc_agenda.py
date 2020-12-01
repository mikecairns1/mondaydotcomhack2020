#!/usr/local/bin/python3
# Import Monday CLI libraries
from moncli import MondayClient
from moncli import BoardKind
from moncli import ColumnType
from moncli import WorkspaceKind
#from moncli import ColumnValue

# Import Google Classroom functions
#from gc_getCourses import getCourses, getUser
from gc_getCourses import getCourses

# Instantiating a new client interface to Monday.com
client = MondayClient(user_name='mikephamdavis@gmail.com', api_key_v1='eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjkxNTcxMzE0LCJ1aWQiOjE3Mjk4ODA2LCJpYWQiOiIyMDIwLTExLTIxVDE0OjQzOjE5LjAwMFoiLCJwZXIiOiJtZTp3cml0ZSJ9.G7UsLWL1XKlmClx5lFMxLK_yYG8f2WslO9idr3li09Y', api_key_v2='eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjkxNTcxMzE0LCJ1aWQiOjE3Mjk4ODA2LCJpYWQiOiIyMDIwLTExLTIxVDE0OjQzOjE5LjAwMFoiLCJwZXIiOiJtZTp3cml0ZSJ9.G7UsLWL1XKlmClx5lFMxLK_yYG8f2WslO9idr3li09Y')

## Flow of activity to set up the Monday.com Google Classroom Agenda board:

## Build a new workspace to hold all of these things
## - Not using since board is not associating to the workspace.
#gc_user = getUser
#student_name = gc_user[0]['fullName']
student_name = "Bob"
#ws_description = "{}'s Google Classroom Workspace".format(student_name)
#client.create_workspace(name=student_name, kind="open", description=ws_description)
#student_workspace = client.create_workspace(student_name, WorkspaceKind.open, 'id', 'name')
#student_workspace_id = student_workspace['id']

# 1. Setup Monday Workspace and Groups
b_name = "{} - School Board".format(student_name)
try: 
    # 1a. First check to see if the board already exists
    school_board = client.get_board_by_name(b_name)
    board_does_not_exist = False
except:
    board_does_not_exist = True
    
if board_does_not_exist:
    # 1b. Create new board
    #school_board = client.create_board(name=board_name, kind=board_kind, 'id', 'name')
    #school_board = client.create_board(board_name=b_name, board_kind=BoardKind.public, workspace_id='id', 'name')
    school_board = client.create_board(b_name, BoardKind.public)

# 2. Build a group called <UserName>'s Courses from Google Classroom API
new_group_name = "{} - Courses".format(student_name)

try: 
    # 2a. First check to see if the group already exists
    course_group = school_board.get_group(None, new_group_name)
    group_does_not_exist = False
except:
    group_does_not_exist = True

if group_does_not_exist:
    # 2b. Create new group
    course_group = school_board.add_group(new_group_name)
    #2c. Add Columns to group
    school_board.add_column(title='id', column_type=ColumnType.item_id)
    school_board.add_column(title='name', column_type=ColumnType.text)
    school_board.add_column(title='section', column_type=ColumnType.text)
    school_board.add_column(title='descriptionHeading', column_type=ColumnType.text)
    school_board.add_column(title='ownerId', column_type=ColumnType.item_id)
    school_board.add_column(title='creationTime', column_type=ColumnType.date)
    school_board.add_column(title='updateTime', column_type=ColumnType.date)
    school_board.add_column(title='enrollmentCode', column_type=ColumnType.text)
    school_board.add_column(title='courseState', column_type=ColumnType.status)
    school_board.add_column(title='alternateLink', column_type=ColumnType.link)
    school_board.add_column(title='teacherGroupEmail', column_type=ColumnType.email)
    school_board.add_column(title='courseGroupEmail', column_type=ColumnType.email)
    school_board.add_column(title='teacherFolder', column_type=ColumnType.item_id)
    school_board.add_column(title='guardiansEnabled', column_type=ColumnType.checkbox)
    school_board.add_column(title='calendarId', column_type=ColumnType.email)

g_courses_list = getCourses()
for course in g_courses_list:
    course_name = course['name']
    course_values = dict(course)
    course_values.pop('name')
    #new_item = course_group.add_item(item_name=course_name, column_values=course_values)
    new_item = course_group.add_item(course_name)

    #for sb_col in school_board.columns:
    #    col_name = sb_col['id']
    #    new_item.

# 3. For each course, get a list of Assignments and add them to a Monday group called Assignments

# 4. Determine next steps.

