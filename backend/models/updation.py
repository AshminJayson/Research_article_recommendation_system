import csv


def updation(art_id, submitter, auth, title, comments, journ_ref, doi, cate, abstr, ver):
    new_entry = []
    new_entry.extend(art_id, submitter, auth, title, comments,
                     journ_ref, doi, cate, abstr, ver)
    # id,submitter,authors,title,comments,journal-ref,doi,report-no,categories,license,abstract,versions/0/version,versions/0/created,versions/1/version,versions/1/created,update_date,authors_parsed/0/0,authors_parsed/0/1,authors_parsed/0/2,authors_parsed/1/0,authors_parsed/1/1,authors_parsed/1/2,authors_parsed/2/0,authors_parsed/2/1,authors_parsed/2/2,authors_parsed/3/0,authors_parsed/3/1,authors_parsed/3/2,versions/2/version,versions/2/created,authors_parsed/4/0,authors_parsed/4/1,authors_parsed/4/2,authors_parsed/5/0,authors_parsed/5/1,authors_parsed/5/2,authors_parsed/6/0,authors_parsed/6/1,authors_parsed/6/2,authors_parsed/0/3,authors_parsed/1/3,versions/3/version,versions/3/created,authors_parsed/2/3,authors_parsed/3/3,authors_parsed/4/3,authors_parsed/5/3,authors_parsed/6/3,authors_parsed/7/0,authors_parsed/7/1,authors_parsed/7/2,authors_parsed/8/0,authors_parsed/8/1,authors_parsed/8/2,authors_parsed/9/0,authors_parsed/9/1,authors_parsed/9/2,authors_parsed/10/0,authors_parsed/10/1,authors_parsed/10/2,authors_parsed/11/0,authors_parsed/11/1,authors_parsed/11/2,authors_parsed/12/0,authors_parsed/12/1,authors_parsed/12/2,authors_parsed/13/0,authors_parsed/13/1,authors_parsed/13/2,versions/4/version,versions/4/created,authors_parsed/14/0,authors_parsed/14/1,authors_parsed/14/2,authors_parsed/15/0,authors_parsed/15/1,authors_parsed/15/2,authors_parsed/16/0,authors_parsed/16/1,authors_parsed/16/2,authors_parsed/17/0,authors_parsed/17/1,authors_parsed/17/2,authors_parsed/18/0,authors_parsed/18/1,authors_parsed/18/2,authors_parsed/19/0,authors_parsed/19/1,authors_parsed/19/2,authors_parsed/20/0,authors_parsed/20/1,authors_parsed/20/2,authors_parsed/21/0,authors_parsed/21/1,authors_parsed/21/2,authors_parsed/22/0,authors_parsed/22/1,authors_parsed/22/2,authors_parsed/23/0,authors_parsed/23/1,authors_parsed/23/2,authors_parsed/24/0,authors_parsed/24/1,authors_parsed/24/2,authors_parsed/25/0,authors_parsed/25/1,authors_parsed/25/2,authors_parsed/7/3,authors_parsed/8/3,versions/5/version,versions/5/created,versions/6/version,versions/6/created,versions/7/version,versions/7/created,authors_parsed/26/0,authors_parsed/26/1,authors_parsed/26/2,authors_parsed/27/0,authors_parsed/27/1,authors_parsed/27/2,authors_parsed/28/0,authors_parsed/28/1,authors_parsed/28/2,authors_parsed/29/0,authors_parsed/29/1,authors_parsed/29/2,authors_parsed/30/0,authors_parsed/30/1,authors_parsed/30/2,authors_parsed/31/0,authors_parsed/31/1,authors_parsed/31/2,authors_parsed/32/0,authors_parsed/32/1,authors_parsed/32/2,authors_parsed/33/0,authors_parsed/33/1,authors_parsed/33/2,authors_parsed/34/0,authors_parsed/34/1,authors_parsed/34/2,authors_parsed/35/0,authors_parsed/35/1,authors_parsed/35/2,authors_parsed/36/0,authors_parsed/36/1,authors_parsed/36/2,authors_parsed/37/0,authors_parsed/37/1,authors_parsed/37/2,authors_parsed/38/0,authors_parsed/38/1,authors_parsed/38/2,authors_parsed/39/0,authors_parsed/39/1,authors_parsed/39/2,authors_parsed/40/0,authors_parsed/40/1,authors_parsed/40/2,authors_parsed/41/0,authors_parsed/41/1,authors_parsed/41/2,authors_parsed/42/0,authors_parsed/42/1,authors_parsed/42/2,authors_parsed/43/0,authors_parsed/43/1,authors_parsed/43/2,authors_parsed/9/3,authors_parsed/10/3,authors_parsed/11/3,authors_parsed/12/3,authors_parsed/13/3,authors_parsed/14/3,authors_parsed/15/3,authors_parsed/16/3,authors_parsed/17/3,authors_parsed/18/3,authors_parsed/19/3,authors_parsed/20/3,authors_parsed/21/3,authors_parsed/22/3,authors_parsed/23/3,authors_parsed/24/3,authors_parsed/25/3,authors_parsed/26/3
