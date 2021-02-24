from django.shortcuts import render, HttpResponse


# Create your views here.
def word(request):
    paras = {'name': 'aashish'}
    return render(request, 'index.html', paras)


def analize(request):
    # get the text
    text1 = request.POST.get('text', 'default')
    punch = request.POST.get('punk', 'off')
    caps = request.POST.get('caps', 'off')
    newline = request.POST.get('newline', 'off')
    extra = request.POST.get('extra', 'off')
    count = request.POST.get('count', 'off')
    if punch == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text1:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {
            'purpose': 'Remove Punctuations',
            'analyzed_text': analyzed
        }
        return render(request, 'analize.html', params)
    elif (caps == 'on'):
        analyzed = ""
        for char in text1:
            analyzed = analyzed + char.upper()

        params = {
            'purpose': 'Change to Uppercase',
            'analyzed_text': analyzed
        }
        return render(request, 'analize.html', params)

    elif (newline == 'on'):
        analized = ''
        for char in text1:
            if char != '\n':
                analized = analized + char

        params = {
            'purpose': 'Remove newline',
            'analyzed_text': analized
        }
        return render(request, 'analize.html', params)


    elif (extra == 'on'):
        analyzed = ""
        for index, char in enumerate(text1):
            if text1[index] == ' ' and text1[index + 1] == ' ':
                pass
            else:
                analyzed = analyzed + char

        params = {
            'purpose': 'Remove extra space',
            'analyzed_text': analyzed
        }
        return render(request, 'analize.html', params)

    elif (count == 'on'):
        analized = len(text1)
        params = {
            'purpose': 'count text',
            'analyzed_text': analized,
            'text2': 'here is the number of word is'
        }
        return render(request, 'analize.html', params)


    else:
        return HttpResponse('error')
