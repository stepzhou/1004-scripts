Mass Emailing for 1004 TA
=========================

Simple tool for mass sending grade report emails.

Usage
-----

    python mass_send.py <email_text> <UNI_emails> <grade_report_path>

**email_text:**

Text file of the email in the format of:

    SUBJECT\n
    BODY

**UNI_emails:**

Text file of all university emails (keep the @columbia.edu).

The emails should be newline separated, e.g.

    aaa1001@columbia.edu
    bbb2002@barnard.edu
    etc.

**grade_report_path:**

Directly that contains the grade reports named as UNI.txt

