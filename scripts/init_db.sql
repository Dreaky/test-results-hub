-- Stores all test runs (even passed ones) for historical tracking
CREATE TABLE test_run (
    id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    database TEXT NOT NULL,
    os TEXT NOT NULL,
    ci TEXT NOT NULL,
    date TIMESTAMP NOT NULL DEFAULT NOW(),
    version TEXT NOT NULL,
    total_tests INT NOT NULL,  -- How many tests were in the run
    failed_tests INT NOT NULL, -- How many failed
    report_url TEXT -- Link to full test report in MinIO
);

-- Stores test cases information
CREATE TABLE test_case (
    id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    team TEXT NOT NULL,
    link TEXT,
    test_ids TEXT,  -- Store multiple test case IDs as comma-separated values
    app_name TEXT NOT NULL
);

-- Stores ONLY failed test cases per test run
CREATE TABLE failed_test (
    id UUID PRIMARY KEY,
    tc_id UUID NOT NULL REFERENCES test_case(id) ON DELETE CASCADE,
    run_id UUID NOT NULL REFERENCES test_run(id) ON DELETE CASCADE,
    status TEXT CHECK (status = 'failed') NOT NULL,
    elapsed TIME NOT NULL,
    error_message TEXT,  -- Stores failure reason
    failure_type TEXT CHECK (failure_type IN ('Assertion', 'Timeout', 'Crash', 'Other')),
    log_url TEXT,  -- Link to failure logs in MinIO
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE (tc_id, run_id)  -- Avoid duplicate failures for the same test case in one run
);

-- Indexes for performance
CREATE INDEX idx_test_run_date ON test_run(date);
CREATE INDEX idx_failed_test_tc_id ON failed_test(tc_id);
CREATE INDEX idx_failed_test_run_id ON failed_test(run_id);
CREATE INDEX idx_failed_test_failure_type ON failed_test(failure_type);
