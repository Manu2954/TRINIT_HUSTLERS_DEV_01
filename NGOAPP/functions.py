def handel_file(f):
    with open('./media/'+f.name,'wb+') as destinantion:
        for chunk in f.chunks():
            destinantion.write(chunk)
