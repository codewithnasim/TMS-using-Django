echo "BUILD START"
pip install -r requirement.txt
python3.10.2 manage.py collectstatic
echo "BUILD END"
