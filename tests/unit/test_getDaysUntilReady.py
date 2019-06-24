import pytest
import json
import os
from pypineapple import pineapple as p

# uses hard coded values to test, not a best practice
def test_getDaysUntilReadyHardCoded():
    with open('tests\\unit\\readyLookup.json') as lookUpFile:
        lookUpTable = json.load(lookUpFile)
    smellStrength = 1
    days = p.getDaysUntilReady(smellStrength, lookUpTable)
    assert days == 5

@pytest.fixture(scope='module')
def createTempJson(tmpdir_factory, request):
    filePath = tmpdir_factory.mktemp('data').join('readyLookupSample.json')
    
    #region Build a temporary json file
    smellLookUpTable = []
    smellLookUpTable.append({
        "SmellStrength": 0,
        "daysFromBeingReady": 5
    })
    smellLookUpTable.append({
        "SmellStrength": 1,
        "daysFromBeingReady": 5
    })
    with open(filePath, 'w') as outJson:  
        json.dump(smellLookUpTable, outJson)
    #endregion Build a temporary json file

    # remove the temporary directory and JSON file after they have been used.
    def cleanUpJson():
        dataDir = os.path.dirname(filePath)
        os.remove(filePath)
        os.rmdir(dataDir)

    request.addfinalizer(cleanUpJson)
    return str(filePath)

def test_getDaysUntilReady(createTempJson):
    with open(createTempJson) as lookUpFile:
        lookUpTable = json.load(lookUpFile)
    smellStrength = 1
    days = p.getDaysUntilReady(smellStrength, lookUpTable)
    assert days == 5


