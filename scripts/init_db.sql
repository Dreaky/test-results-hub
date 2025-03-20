-- Stores all test runs (even passed ones) for historical tracking
CREATE TABLE test_run (
    id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    database TEXT NOT NULL,
    deployment TEXT NOT NULL,
    date TIMESTAMP NOT NULL DEFAULT NOW(),
    version TEXT NOT NULL,
    total_tests INT NOT NULL,
    total_failures INT NOT NULL,
    total_skipped INT NOT NULL,
    total_errors INT NOT NULL,
    total_time INT NOT NULL,
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
CREATE TABLE test_results (
    id UUID PRIMARY KEY,
    tc_id UUID NOT NULL REFERENCES test_case(id) ON DELETE CASCADE,
    run_id UUID NOT NULL REFERENCES test_run(id) ON DELETE CASCADE,
    status TEXT NOT NULL,
    elapsed TEXT NOT NULL,
    error_message TEXT,
    log_url TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE (tc_id, run_id)  -- Avoid duplicate failures for the same test case in one run
);

-- Indexes for performance
CREATE INDEX idx_test_run_date ON test_run(date);
CREATE INDEX idx_test_results_tc_id ON test_results(tc_id);
CREATE INDEX idx_test_results_run_id ON test_results(run_id);
