# OOTOMAST Survey Parser

### Steps to parse
1. Convert the survey form to desired format
- Add directly for questions with 1 answer only
- Add '=' for english tagalog translation e.g. eng_ques = tag_ques
-- To add choices, add & at the end of the question separated with '/' e.g. eng_ques = tag_ques & choice1 / choice2 / ... / choiceN
- For transition, add '*' at the beginning, e.g. *This is transition screen
