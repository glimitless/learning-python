domains = ['www.google.com', 'openai.com', 'apple.com', 'gian-i.media', 'localhost', 'WWW.BLUESWORLD.COM']

accepted_top_levels = ('.com', '.media', '.org', '.ai')
find_top_level = lambda d: d[d.rindex('.'):] 

cleaned = [
    domain.lower().replace('www.', '')
    for domain in domains
    if '.' in domain
    if find_top_level(domain.lower()) in accepted_top_levels
]
print(cleaned)

# cleaned_domains = []
# for domain in domains:
#     domain_to_clean = domain
#     if domain_to_clean != domain_to_clean.lower():
#         domain_to_clean = domain_to_clean.lower()
#     if domain_to_clean.count('.') > 2 or domain_to_clean.count('.') < 1:
#         print(f'Domain {domain} is an unnacceptable format.')
#         continue
#     if find_top_level(domain_to_clean) not in accepted_top_levels:
#         print(f'We do not support {find_top_level(domain)} domains. {domain} does not fit our criteria.')
#         continue

#     cleaned_domains.append(domain_to_clean)
# else:
#     print('Successfully parsed through domain list.')
#     print(cleaned_domains)
    

