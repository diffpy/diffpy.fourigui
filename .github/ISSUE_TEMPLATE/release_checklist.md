---
name: Release
about: Checklist and communication channel for PyPI and GitHub release
title: "Ready for <version-number> PyPI/GitHub release"
labels: "release"
assignees: ""
---

### Release checklist for GitHub contributors

- [ ] All PRs/issues attached to the release are merged.
- [x] All the badges on the README are passing.
- [x] License information is verified as correct. If you are unsure, please comment below.
- [x] Locally rendered documentation contains all appropriate pages, including API references (check no modules are
  missing), tutorials, and other human written text is up-to-date with any changes in the code.
- [x] Installation instructions in the README, documentation and on the website (e.g., diffpy.org) updated.
- [x] Successfully run any tutorial examples or do functional testing with the latest Python version
- [x] Grammar and writing quality have been checked (no typos).

Please mention @sbillinge when you are ready for release. Include any additional comments necessary, such as
version information and details about the pre-release here:

### Post-release checklist

Before closing this issue, please complete the following:

- [ ]  Run tutorial examples and conduct functional testing using the installation guide in the README.
- [ ]  Documentation (README, tutorials, API references, and websites) is deployed without broken links or missing figures.
