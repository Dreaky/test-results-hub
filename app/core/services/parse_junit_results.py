import re
from xml.dom import minidom

DEFAULT_RESULT_COMMENT = 'automation test result'


def load_test_cases_from_file(input_file):
    results = []

    with open(input_file, 'r') as f:
        xml_content = f.read()
        xml_doc = minidom.parseString(xml_content)

    # Iterate over each testsuite
    for testsuite in xml_doc.getElementsByTagName('testsuite'):
        app_name = testsuite.getAttribute('hostname')  # Extract hostname as app name
        for testcase in testsuite.getElementsByTagName('testcase'):
            tc_name = testcase.getAttribute('name')  # Test case name
            case_ids = parse_case_ids(tc_name)  # Extract case IDs
            parsed_time = parse_time(testcase.getAttribute('time'))
            payload = {'name': str(tc_name).replace('â€º', '->'), 'team': 'QA', 'link': 'http://example.com',
                       'test_ids': ','.join(map(str, case_ids)), 'app_name': app_name,
                       'elapsed': parsed_time if parsed_time else '0'}
            status_node = get_status_node(testcase)
            payload['status_id'], payload['comment'] = map_status_to_comment(status_node)

            # Add to the results if needed for further processing
            results.append({'caseId': payload['test_ids'], 'payload': payload})

    return results


def load_total_information(input_file):
    # Initialize a dictionary to hold the total information
    total = {}

    # Parse the JUnit XML file using minidom
    with open(input_file, 'r') as f:
        xml_content = f.read()

    # Parse the XML string
    xml_doc = minidom.parseString(xml_content)
    # Extract total information from the <testsuites> tag
    testsuites = xml_doc.getElementsByTagName('testsuites')[0]

    # Extract attributes from the testsuites tag
    total['total_tests'] = testsuites.getAttribute('tests')
    total['total_failures'] = testsuites.getAttribute('failures')
    total['total_skipped'] = testsuites.getAttribute('skipped')
    total['total_errors'] = testsuites.getAttribute('errors')
    total['total_time'] = round(float(testsuites.getAttribute('time')))

    return total


def parse_case_ids(tc_name):
    # Find all occurrences of 'C' followed by digits (e.g., C11604, C11605)
    test_cases = re.findall(r'C(\d{4,})', tc_name)
    return [int(tc) for tc in test_cases]


def parse_time(time_string):
    try:
        time = float(time_string)
        return f'{int(time)}s' if time < 60 else f'{int(time // 60)}m {int(time % 60)}s'
    except ValueError:
        return '0'


def get_status_node(testcase):
    if testcase.getElementsByTagName('failure'):
        return 'failure'
    elif testcase.getElementsByTagName('skipped'):
        return 'skipped'
    else:
        return 'passed'


def map_status_to_comment(status_node):
    if status_node == 'failure':
        return 5, 'FAILED automation test result'
    elif status_node == 'skipped':
        return 6, 'SKIPPED automation test result'
    else:
        return 1, 'PASSED automation test result'
