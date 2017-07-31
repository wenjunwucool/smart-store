# nvme-cli SPDK support Test Plan

# Sytem/Integration testing
- Run nvme-cli command with SPDK and kernel driver, comparing the command output.
The commands are as below:
  - nvme list;
  - nvme smart-log;
  - nvme id-ctrlr;
  - nvme id-ns;
  - nvme get-ns-id;
  - nvme get-log;
  - nvme fw-log;
  - nvme error-log;
  - nvme get-feature;
  - nvme set-feature;
  - nvme dsm;
  - nvme flush;
  - nvme read;
  - nvme write;
  - nvme write-zero;
  - nvme write-uncor;
  - nvme reset;
  - nvme create-ns;
  - nvme list-ns;
  - nvme delete-ns;
  - nvme attach-ns;
  - nvme detach-ns;
  - nvme list-ctrlr;
  - nvme format;
  - nvme fw-activate;
  - nvme fw-download;
  - nvme admin-passthru;
  - nvme io-passthru;
  - nvme security-send;
  - nvme security-recv;
  - nvme resv-acquire;
  - nvme resv-register;
  - nvme resv-release;
  - nvme resv-report;
  - nvme compare;
  - nvme subsystem-reset;
  - nvme show-regs;
  - nvme discovr;
  - nvme connect-all;
  - nvme connect;
  - nvme disconnect;
  - nvme gen-hostnqn;

#Test Cases Description

##Test Cases Execution Prerequisites
1. Clone and compile SPDK in a directory;
2. Clone and compile nvme-cli with SPDK.

##Test Case 1: nvme list command

##Test Case 1: nvme smart-log command

##Test Case 2: nvme id-ctrlr command

##Test Case 3: nvme id-ns command

##Test Case 4: nvme get-ns-id command

##Test Case 5: nvme get-log command

##Test Case 6: nvme fw-log command

##Test Case 7: nvme error-log command

##Test Case 8: nvme get-feature command

##Test Case 9: nvme set-feature command

##Test Case 10: nvme dsm command

##Test Case 11: nvme flush command

##Test Case 12: nvme read command

##Test Case 13: nvme write command

##Test Case 14: nvme write-zero command

##Test Case 15: nvme write-uncor command

##Test Case 16: nvme reset command

