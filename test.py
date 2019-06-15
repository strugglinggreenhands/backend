def my_finish(request):
    if request.method == "GET":
        my_finish = models.Transaction.objects.filter(Q(acceptor=request.session.get('user_name')) & Q(is_finish=True)).values_list()
        my_finish_trans = []
        for i in range(len(my_finish)):
            dict = {
                '任务编号': my_finish[i][0],
                '任务类型': get_type(my_finish[i][1]),
                '积分奖励': my_finish[i][2],
                '发布者': my_finish[i][3],
                '联系电话': my_finish[i][4],
                '任务内容': my_finish[i][5],
                '截止日期': my_finish[i][6],
                '接受状态': my_finish[i][8],
                '执行人': my_finish[i][9],
                '完成状态': my_finish[i][10]
            }
            my_finish_trans.append(
                dict
            )
        return render(request, 'login/my_finish.html', {'key': my_finish_trans})
    return render(request, 'login/my_finish.html')