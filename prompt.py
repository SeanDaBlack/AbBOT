#!/usr/bin/env python3
import random

suspect_words = [
    'suspect',
    'have reason to suspect',
    'believe',
    'have reason to believe',
    'think',
    'have evidence',
    'have strong evidence',
    'am convinced',
    'am certain',
]
my_family_words = [
    (0.5, 'father'),
    (0.5, 'mother'),
    (1.0, 'brother'),
    (1.0, 'sister'),
    (0.5, 'older brother'),
    (0.5, 'older sister'),
    (0.5, 'younger brother'),
    (0.5, 'younger sister'),
    (1.0, 'cousin'),
    (2.0, 'aunt'),
    (0.5, 'uncle'),
    (0.6, 'daughter'),
    (0.6, 'son'),
    (0.2, 'step-son'),
    (0.1, 'step son'),
    (0.2, 'step-daughter'),
    (0.1, 'step daughter'),
    (0.7, 'nephew'),
    (0.7, 'niece'),
    (0.5, 'grandmother'),
    (0.2, 'grandma'),
    (0.5, 'grandfather'),
    (0.2, 'grandpa'),
    (0.5, 'granddad'),
    (1.0, 'grandson'),
    (1.0, 'granddaughter'),
    (1.0, 'son-in-law'),
    (1.0, 'daughter-in-law'),
    (1.0, 'mother-in-law'),
    (1.0, 'father-in-law'),
    (0.1, 'half-brother'),
    (0.1, 'half-sister'),
]
subjects = [
    'science',
    'math',
    'history',
    'social studies',
    'chemistry',
    'algebra',
    'Spanish',
    'calculus',
    'art',
    'music',
    'P.E.',
    'gym',
    'English',
]
my_teacher_words = [
    (1.0, 'teacher'),
    *[
        (0.2, k + ' teacher') for k in subjects
    ],
    (0.5, 'tutor'),
    *[
        (0.1, k + ' tutor') for k in subjects
    ],
    (1.0, 'babysitter')
]
my_nonfamily_words = [
    (2.0, 'neighbor'),
    (0.6, 'next-door neighbor'),
    (1.5, 'boss'),
    (0.7, 'landlord'),
    (1.5, 'doctor'),
    (0.7, 'employee'),
    (0.5, 'roommate'),
    (1.0, 'friend'),
    (1.0, 'girlfriend'),
    (1.0, 'boyfriend'),
    (0.3, 'maid'),
    (0.2, 'live-in maid'),
    (0.1, 'live in maid'),
    (2.0, 'ex'),
    (0.3, 'therapist'),
    (0.5, 'supervisor'),
    (1.0, 'employer'),
    (0.2, 'lawyer'),
    (0.4, 'dentist'),
    (0.2, 'plumber'),
    (1.5, 'pastor'),
    (0.5, 'deacon'),
    (0.8, 'priest'),
    (0.2, 'accountant'),
]
my_family_possessive_adj = [
    (k[0], k[1] + "'s ") for k in my_nonfamily_words
]
my_family_possessive_adj.append((20.0, ''))
my_nonfamily_possessive_adj = [
    (k[0], k[1] + "'s ") for k in my_family_words
]
my_nonfamily_possessive_adj.append((20.0, ''))
my_teacher_possessive_adj = [
    (0.2, 'younger brother'),
    (0.2, 'younger sister'),
    (0.8, 'brother'),
    (0.8, 'sister'),
    (1.0, 'cousin'),
    (2.0, 'daughter'),
    (2.0, 'son'),
    (0.4, 'step-son'),
    (0.2, 'step son'),
    (0.4, 'step-daughter'),
    (0.2, 'step daughter'),
    (0.7, 'nephew'),
    (0.7, 'niece'),
]
my_teacher_possessive_adj = [ (k[0], k[1] + "'s ") for k in my_teacher_possessive_adj ]
violated_words = [
    'violated', 'disregarded', 'disobeyed'
]
days_of_the_week = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
]
got_words = [
    'got', 'had'
]
past_time_frames = [
    'last week', 'last month', 'this week', 'this month', 'yesterday', 'a week ago', 'two weeks ago', 'two days ago', 'on the weekend', 'this weekend', 'last weekend'
]
past_time_frames.extend([ 'last ' + k for k in days_of_the_week ])
past_time_frames.extend([ 'on ' + k for k in days_of_the_week ])
will_get_words = [
    'is getting', 'will get', 'plans on having', 'is trying to get', 'is trying to have', 'will try to get'
]
future_time_frames = [
    'next week', 'this week', 'tomorrow', 'two days from now', 'a week from now', 'after she leaves work', 'after work', 'on the weekend', 'this weekend', 'next weekend'
]
future_time_frames.extend([ 'next ' + k for k in days_of_the_week ])
future_time_frames.extend([ 'on ' + k for k in days_of_the_week ])
abortion_ban_words = [
    'abortion ban', 'ban on abortion', 'new abortion law', 'law on abortion', 'recent abortion law', 'abortion restrictions', 'restrictions on abortion', 'law'
]
abortion_ban_words = [ *["Texas's " + k for k in abortion_ban_words], *["the " + k for k in abortion_ban_words] ]
abortion_ban_words.extend(['Texas law', 'the new law'])

def random_select_weighted_list(ls):
    return random.choices([k[1] for k in ls], weights = [k[0] for k in ls], k = 1)[0]

def gen_abortion_prompt_I(accused):
    abortion_prompt = 'I '
    abortion_prompt += random.choice(suspect_words)
    abortion_prompt += random.choices([' that', ''], weights = [0.75, 0.25], k = 1)[0]
    abortion_prompt += ' my '
    abortion_prompt += accused
    abortion_prompt += random.choice([' has ', ' '])
    abortion_prompt += random.choice(violated_words)
    abortion_prompt += ' '
    abortion_prompt += random.choice(abortion_ban_words)
    abortion_prompt += '.'
    return abortion_prompt

def gen_abortion_prompt_My(accused):
    abortion_prompt = 'My '
    abortion_prompt += accused
    abortion_prompt += ' '
    past = random.random() > 0.5
    if past:
        abortion_prompt += random.choice(got_words)
    else:
        abortion_prompt += random.choice(will_get_words)
    abortion_prompt += ' an'
    abortion_prompt += random.choices(['', ' illegal', ' unlawful'], weights = [ 0.625, 0.375 / 2.0, 0.375 / 2.0 ], k = 1)[0]
    abortion_prompt += ' abortion'
    if random.random() > 0.5:
        abortion_prompt += ' '
        if past:
            abortion_prompt += random.choice(past_time_frames)
        else:
            abortion_prompt += random.choice(future_time_frames)
    abortion_prompt += '.'
    return abortion_prompt

def gen_abortion_prompt():
    accused_family_person = random_select_weighted_list(my_family_possessive_adj)
    accused_family_person += random_select_weighted_list(my_family_words)
    accused_nonfamily_person = random_select_weighted_list(my_nonfamily_possessive_adj)
    accused_nonfamily_person += random_select_weighted_list(my_nonfamily_words)
    accused_teacher = random_select_weighted_list(my_teacher_possessive_adj)
    accused_teacher += random_select_weighted_list(my_teacher_words)
    accused = random_select_weighted_list([
        (1.0, accused_family_person),
        (1.5, accused_nonfamily_person),
        (0.5, accused_teacher)
    ])
    abortion_prompts = [
        (5.2, gen_abortion_prompt_I(accused)),
        (2.6, gen_abortion_prompt_My(accused))
    ]
    return random_select_weighted_list(abortion_prompts)

if __name__ == "__main__":
    total_number = 2000000
    sample_abortion_prompts = { gen_abortion_prompt() for k in range(total_number) }
    for k in sorted(list(sample_abortion_prompts)[:200], key = lambda o: random.random()):
        print(k)
    print(total_number - len(sample_abortion_prompts))
    print(len(sample_abortion_prompts))
    print(len([k for k in sample_abortion_prompts if 'I' in k]))
    print(len(sample_abortion_prompts) - len([k for k in sample_abortion_prompts if 'I' in k]))
