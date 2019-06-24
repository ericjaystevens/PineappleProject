import pytest
import csv
import os
import datetime

def test_equality():
    assert 1 == 1

def test_transitive():
    x = 1
    y = x
    assert y == 1

@pytest.mark.parametrize("equal_input, expected", [
    (1,1),
    (2,2),
    (3,4),
    (5,5),
])

def test_equal(equal_input, expected):
    assert equal_input == expected

@pytest.fixture(scope='module')
def createCsv(tmpdir_factory, request):
    filePath = tmpdir_factory.mktemp('data').join('usPresidents.csv')
    headers = ['name','order','termsElected']
    with open(filePath,'w') as csvFile:
        writer = csv.DictWriter(csvFile,fieldnames=headers)
        writer.writeheader()
        writer.writerow({'name': 'Wasington', 'order': 1, 'termsElected': 2})
        writer.writerow({'name': 'Lincon', 'order': 16, 'termsElected': 2})
    
    def cleanUpCsv():
        dataDir = os.path.dirname(filePath)
        tempDir = os.path.dirname(dataDir)
        os.remove(filePath)
        os.rmdir(dataDir)

    request.addfinalizer(cleanUpCsv)
    return str(filePath)

def test_CsvExists(createCsv):
    assert os.path.isfile(createCsv) == True
    #assert 0

#mock
def isTodaySaturday():
    today = datetime.datetime.now()
    return (today.weekday() == 5)

@pytest.fixture
def mock_datetime_now(monkeypatch):
    mockTime = datetime.datetime(1985, 10, 26, 1, 21, 00)
    class mocktoday:
        @classmethod
        def now(cls):
            return mockTime

    monkeypatch.setattr(datetime, 'datetime', mocktoday)


def test_IsTodaySaturday(mock_datetime_now):
    assert isTodaySaturday() == True