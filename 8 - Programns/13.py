original_list_form = [
    'segment',
    'unit',
    'influence_area',
    'coverage',
    'nature',
    'hired_companies',
    'facilitator_managements',
    'interested_managements',
    'facilitator_responsibles',
    'interested_responsibles',
    'documents_access',
    'recurrent_manifestation',
    'locality',
    'city',
    'category',
    'classification',
    'attendance_type',
    'reception_way',
    'theme',
    'subtheme',
    'protester',
    'management',
    'default_answer',
    'protester_answer_date',
    'sensible_data_comments'
]

actual_form = [
    'datetime',
    'protester_anonymous',
    'protester',
    'is_recurrent_manifestation',
    'segment',
    'unit',
    'influence_area',
    'city',
    'locality',
    'attendance_type',
    'hired_companies',
    'nature',
    'coverage',
    'theme',
    'subtheme',
    'facilitator_managements',
    'interested_managements',
    'facilitator_responsibles',
    'interested_responsibles',
    'has_sensible_data',
    'detailing',
    'comments',
    'category',
    'classification',
    'reception_way',
    'default_answer',
    'documents_confidentiality',
    'manifestationdocument_set',
]

original_list_form_qnt = actual_form_qnt = 0

for element in original_list_form:
    print('\t', element)
    original_list_form_qnt += 1

print(f' \033[33m -> Original list form has {original_list_form_qnt} elements \033[m')


for element in actual_form:
    print('\t', element)
    actual_form_qnt += 1

print(f' \033[33m -> Actual list form has {actual_form_qnt} elements \033[m')


if original_list_form_qnt > actual_form_qnt:
    print(f' Original is bigger')

else:
    print(f' Actual is bigger')

while len(original_list_form) <= len(actual_form):
    original_list_form.append('')


print()
print('NOT IN LIST')
for i in range(len(actual_form)):
    if original_list_form[i] not in actual_form:
        print(f'{original_list_form[i]}')
