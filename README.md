Mass Emailing for 1004 TA
=========================

Simple tool for mass sending grade report emails.

Usage
-----

    python mass_send.py <email_text> <UNI_emails> <grade_report_path>

Have another file called credentials.py with the following:

    credentials.py

    USERNAME = '<your_gmail_username>'
    PWD = '<your_gmail_pwd>'

**email_text:**

Text file of the email in the format of:

    SUBJECT
    BODY
    BODY
    BODY
    ...

In that the subject is one line ending in a newline, and the rest of the file is
the body.

**UNI_emails:**

Text file of all university emails (keep the @columbia.edu).

The emails should be newline separated, e.g.

    aaa1001@columbia.edu
    bbb2002@barnard.edu
    etc.

**grade_report_path:**

Directory that contains the grade reports named as UNI.txt

Example
-------

    python mass_send.py email.txt student_emails.txt /grade_reports/


