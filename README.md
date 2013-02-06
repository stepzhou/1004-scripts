Mass Emailing for 1004 TA
=========================

Simple tool for mass sending grade report emails.

Usage
-----

Fill out config.py with the your smtp configurations.

See sample for config examples.

Then run script in following format

    python mass_send.py <email_text> <UNI_emails> <grade_report_path>

**email_text:**

Text file of the email in the format of:

    SUBJECT
    BODY

First line is email subject. Rest is body.

**UNI_emails:**

Text file of all university emails (keep the @columbia.edu).

The emails should be newline separated, e.g.

    aaa1001@columbia.edu
    bbb2002@barnard.edu
    ...

**grade_report_path:**

Directory that contains the grade reports named as UNI.txt

Example
-------

    python mass_send.py email.txt student_emails.txt /grade_reports/


