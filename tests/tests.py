
from utils import consts
from utils.sql_conn import select_all
from utils.utils import init_log, get_expected_data

log = init_log()


def test_validate_data_in_db():
    error_list = []
    tested_table_name = "test_table"
    # read all data from DB and validate
    raw_data = select_all(tested_table_name)
    actual_data = []
    # convert all data from DB to dict
    for line in raw_data:
        actual_data.append(dict(zip(consts.DB_COLUMNS, line)))
    # get expected data from json
    expected_data = get_expected_data(tested_table_name)
    # validate that the table has expected amount of lines
    if len(expected_data) != len(actual_data):
        error_list.append(f"Expected amount of records '{len(expected_data)}', Actual:{len(actual_data)}")
    else:
        log.info("amount of lines as expected")
    db_codes = [i[consts.COLUMN_CODE] for i in actual_data]
    # validate that the keys are as expected
    if not all(elem in db_codes for elem in expected_data.keys()):
        error_list.append("Not all codes are equal")
    else:
        log.info("The 'code' column as expected")
    # validate for each key that it has the expected value
    for line in actual_data:
        code_items = expected_data[line[consts.COLUMN_CODE]]
        if code_items[consts.COLUMN_DESC] != line[consts.COLUMN_DESC]:
            error_list.append(
                f'The description is wrong, code:{line[consts.COLUMN_CODE]},\nExpected: '
                f'{code_items[consts.COLUMN_DESC]}\nActual: {line[consts.COLUMN_DESC]}')
        if code_items[consts.COLUMN_LIST] != line[consts.COLUMN_LIST]:
            error_list.append(
                f'The list is wrong, code:{line[consts.COLUMN_CODE]}\nExpected:'
                f'{code_items[consts.COLUMN_LIST]}\nActual: {line[consts.COLUMN_LIST]}')
        if code_items[consts.COLUMN_DURATION] != line[consts.COLUMN_DURATION]:
            error_list.append(
                f'The duration is wrong, code:{line[consts.COLUMN_CODE]}'
                f'\nExpected:{code_items[consts.COLUMN_DURATION]}\n'
                f'Actual: {line[consts.COLUMN_DURATION]}')
    if error_list:
        log.error("-> The test failed <-")
        for error in error_list:
            log.error(error)
        raise Exception("The test failed, please chech the logs")
    log.info("The data of each 'code' is correct")
    log.info("-= The End =-")