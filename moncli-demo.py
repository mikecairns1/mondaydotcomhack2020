#!/usr/local/bin/python3
from moncli import MondayClient
from moncli import BoardKind
from moncli import ColumnType

# Instantiating a new client interface to Monday.com
client = MondayClient(user_name='mikephamdavis@gmail.com', api_key_v1='eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjkxNTcxMzE0LCJ1aWQiOjE3Mjk4ODA2LCJpYWQiOiIyMDIwLTExLTIxVDE0OjQzOjE5LjAwMFoiLCJwZXIiOiJtZTp3cml0ZSJ9.G7UsLWL1XKlmClx5lFMxLK_yYG8f2WslO9idr3li09Y', api_key_v2='eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjkxNTcxMzE0LCJ1aWQiOjE3Mjk4ODA2LCJpYWQiOiIyMDIwLTExLTIxVDE0OjQzOjE5LjAwMFoiLCJwZXIiOiJtZTp3cml0ZSJ9.G7UsLWL1XKlmClx5lFMxLK_yYG8f2WslO9idr3li09Y')

# Creating a new board in the Main Workspace
board_name = 'New Public Board'
board_kind = BoardKind.public
new_board = client.create_board(board_name, board_kind)

# Getting a board by it's ID
board_id = '881643972'
board_by_id = client.get_board(id=board_id)

# Getting a board by it's name (this does not work well as it is not native to Monday)
# board_name = 'Hack Tasks'
# retrieved_board = client.get_board(name=board_name)

# Archiving a board
# archived_board = client.archive_board(board_id)

# Add a new column to the board
new_column = board.add_column(title='New Text Column', column_type=ColumnType.text)

# Retrieving Columns from a board
columns = board.get_columns('id', 'title', 'type')

# Retrieving Groups from a board
groups = board.get_groups('id','name')

# Add a new Group to a board
group_name = 'New Group'
group = board.add_group(group_name, 'id', 'name')

# Duplicate a group.
duplicate_group = group.duplicate()

# Archive a group.
archived_group = group.archive()

# Delete a group.
deleted_group = group.delete()

# Add items (individual record that contains column value data) to a group
item_name = 'New Item 1'
# Add item via board.
group_id = 'group_1'
item = board.add_item(item_name, group_id=group_id)

# Add item via group.
item = group.add_item(item_name)

# Add item with column values
column_values = {'text_column_1': 'New Text Value'}
new_item_with_values = board.add_item(item_name='New Item With Text Value', column_values=column_values)

# Get items from a board (can also get from a Client or group)
items = board.get_items()
# items = client.get_items()
# items = client.get_items()

# After retrieving an item, it can be moved, duplicated, archived or deleted
