d:
cd D:\pycharm\ezmanager
pytest ./cases/edit/test_room.py -s -q --alluredir=./report/result
allure generate ./report/result/ -o ./report/report --clean 
