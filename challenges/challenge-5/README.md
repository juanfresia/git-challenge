# I don't remember...

After four commits of hard work, the Python script is ready; and the company
wants to open source it. It will get a lot of stars on GitHub for sure, Great stuff!

However, there is a slight issue. We cannot make the repository public just yet.
In the past, some credentials (a critical API token) was commited alongside the
code. It is not in the _latest version_, but it is in the _history_; and anyone
rummaging through our commits may be able to found it.

You have been asked to mingle with time itself and _rewrite_ the entire history
of the repository _erasing the credentials_. A task as heroic as it is
ridiculous.

> - Can't we invalidate that token?
> - NO, and no more questions!

Alright...

To clarify, we would make anyone in the open-soruce communitty that we got it
right from the first commit.
The token (`"2d85d816-91f5-4592-afdc-f4c76e816b8d"`) should be replaced by the
expression in the latest commit (`os./os.getenv("TOP_SECRET_API_TOKEN")`). The
folks in the SRE team will figure out how to inject it later on.
Also, we want every commit to run without errors, so if the statement `import
os` is not present; it should be added _after_ the last import.

Do not change anything else. Not a single line. Force push.
You'll be a hero.

And never do it again.

----------

Rewrite the _whole history of your repository_ getting rid of the secret API token.
Folllow the instructions above, then _force push_ the amended history.

After you are done, run the `check_challenge` command to check if you passed the challenge.

Hint: GLaDOS said she would help, keep an eye out.

