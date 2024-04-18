users =[
    {'username': "samuel", 'tweets': ["I love cake", "i love pie"]},
    {'username': "katie", 'tweets': ["I love cat"]},
    {'username': "jeff", 'tweets': []},
    {'username': "bob123", 'tweets': []},
    {'username': "dogg_luvre", 'tweets': ["Dogs are best"]},
    {'username': "guiter_gal", 'tweets': []}
]

incative_user = list(filter(lambda user: not['tweets'],users))
print(incative_user)

inactive_profile = list(map(lambda u: u['username'],
                        filter(lambda user: not user['tweets'], users)))

print(inactive_profile)
