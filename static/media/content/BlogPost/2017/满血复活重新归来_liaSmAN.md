![ͼ1][1]

**Django ���˲���֮MARKDOWN**
  ����ʽ����ǰ��������һ��ͼƬ��
  ![�˴�����ͼƬ������][2]


  ͼ�Ļ�ϱ༭����ţ�ƣ���������������
  ![�˴�����ͼƬ������][3]


  [1]: http://127.0.0.1:8000/media/filer/filer_public/5e/2c/5e2c2c35-be21-4145-b39c-4e54c7311bc5/xia-zai-_1.jpg
  [2]: http://127.0.0.1:8000/media/filer/filer_public/1a/1b/1a1b7b4b-5ea2-4f6e-a97e-f78ccd5e46e6/xia-zai-_2.jpg
  [3]: http://127.0.0.1:8000/media/filer/filer_public/eb/c6/ebc63758-8ed0-4e3d-813e-5872382584cc/xia-zai-_3.jpg
  

        title = models.CharField(max_length=200)
    # �洢�Ƚ϶̵��ַ���������CharField�����������µ�������˵���ܻ���һ����ı���������ʹ��TextField
    # body,md_file.���ն�ת����html_file��չʾ
    body = models.TextField(blank=True)
    html_file = models.FileField(upload_to=get_html_name, blank=True)    # generated html file
    md_file = models.FileField(upload_to=get_upload_md_name, blank=True)  # uploaded md file
    # ����ժҪ������û������ժҪ����Ĭ�������CharField Ҫ�����Ǳ���������ݣ�����ᱨ��
    # ����ֻҪ����blank = True �Ϳ��������ֵ�ˡ�
    excerpt = models.CharField(max_length=200,blank=True)
    # �ֱ��Ƿ���ʱ�������޸�ʱ�䡣
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    last_edit_date = models.DateTimeField('last edited', auto_now=True)
    
    **Markdown ����չʾ���֣��������ۡ�**
    ��һ��������
    

 1. ֱ��д
 2. �ϴ�md�ļ�

**�������£�**
Ϊʲô��ҳ��ͼƬ����ʾ�������������������������⣿������

**30�������**
��{{blogpost.index_image|safe}}����ӡ�url���ܽ����ҳͼƬ����ʾ���⡣{{blogpost.index_image.url|safe}}

���⣬Description�ֶβ�û��ʲô���ã����Կ���ɾ���ɡ�