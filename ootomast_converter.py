import csv

lines = open('survey.txt', 'r').readlines()

count = 0
id_prefix = 'a'
idx = 1
def is_idx_in_list(a_list, index):
    return index < len(a_list)

with open('ootomast_survey_form.csv', mode='w') as ootomast_survey_form:
    ootomast_survey_form_wrier = csv.writer(ootomast_survey_form, delimiter=',')

    for line in lines:
        line = line.replace('\n', '')

        # var holder for choices to add in csv
        temp_global_choices_eng = []
        temp_global_choices_tag = []

        if (line.strip()):

            # transition
            if('*' in line):
                transition_eng, transition_fil = line.replace('*', '').split('=')
                row = ['^', 0, id_prefix+str(idx), transition_eng.strip(), transition_fil.strip()] # question tag; # of questions; id; english; tagalog

            # one answer question
            elif ('&' not in line):
                question = line.split('=')

                if (len(question) == 1): # no translation, directly append or write
                    row = ['^', 1, id_prefix+str(idx), question[0].strip(), ''] # question tag; # of questions; id; english; tagalog
                else:
                    question_eng, question_tag =question
                    row = ['^', 1, id_prefix+str(idx), question_eng.strip(), question_tag.strip()] # question tag; # of questions; id; english; tagalog
            
            # multiple choice question
            else: 
                question_eng, question_tag_choices = line.split('=')
                question_tag, choices = question_tag_choices.split('&')
                
                choices = choices.split(';')

                ## START Parse choice ##
                choices_eng = choices[0]
                for choice in choices_eng.split('/'):
                    temp_global_choices_eng.append(choice.strip())

                if (len(choices) == 2):
                    choices_tag = choices[1]
                    for choice in choices_tag.split('/'):
                        temp_global_choices_tag.append(choice.strip())
                ## END Parse choice ##

                row = ['^', len(temp_global_choices_eng), id_prefix+str(idx), question_eng, question_tag] # question tag; # of questions; id; english; tagalog

            # print(row)
            ootomast_survey_form_wrier.writerow(row)
            if (len(temp_global_choices_eng) != 0): # check if there are choices and add to csv if ever
                for idx_choice, choice_eng in enumerate(temp_global_choices_eng):

                    # assign choice_tag
                    if (is_idx_in_list(temp_global_choices_tag, idx_choice)):
                        choice_tag = temp_global_choices_tag[idx_choice]
                    else:
                        choice_tag = ''

                    # create row
                    if (idx == 1): # assign the transition to the next question for choice 1
                        row = ['a', id_prefix+str(idx+1), idx_choice, choice_eng, choice_tag] # category of choice; skip to; index of question; english; tagalog
                    else:
                        row = ['a', '', idx_choice, choice_eng, choice_tag] # category of choice; skip to; index of question; english; tagalog
                    
                    # print row
                    ootomast_survey_form_wrier.writerow(row)

        idx += 1