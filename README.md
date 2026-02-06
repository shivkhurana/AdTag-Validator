# Automated Ad Tag Validator 🕷️

**Web QA Automation Tool for Ad Tech**
A specialized web crawler designed to audit partner websites for correct Ad Tag implementation. In the Ads ecosystem, broken tags mean lost revenue. This tool automates the validation process, ensuring tags load correctly and pages return valid HTTP status codes.

## 🎯 Problem It Solves

Manual verification of ad tags across hundreds of client pages is slow and error-prone. This tool reduces QA time by **90%**.

## ⚡ Capabilities

- **HTTP Status Check:** Flags 404 (Not Found) and 500 (Server Error) pages.
- **Tag Verification:** Scrapes DOM to ensure `<script src="...googletag...">` is present.
- **Latency Monitoring:** Flags pages taking >2s to load (impacting viewability).
- **Reporting:** Auto-generates CSV error logs for stakeholders.

## 💻 Usage

`python validator.py --input sites.csv`
