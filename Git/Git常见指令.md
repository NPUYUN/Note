# �������
``` bash
git init       # ��ʼ�����ֿ⣨�����²ֿ⣩                            
git config --global user.name "xxx"             # �����û���    
git config --global user.email "xxx@xxx.com"    # �����ʼ�    
git config --global color.ui true               # git status�������Զ�ɫ               
git config --global color.status auto    
git config --global color.diff auto    
git config --global color.branch auto    
git config --global color.interactive auto    
git config --global http.proxy                  # �鿴��ǰ��������      
git config --global http.proxy 'http://127.0.0.1:1080'  # ����http����??    
git config --global https.proxy 'socks5://127.0.0.1:1080' # ����https����??   
git config --global --unset http.proxy    #ɾ�� proxy git config
```

# �������ύ���
``` bash
git status                           # �鿴��ǰ�汾״̬   
git add t.txt                        # ��ӵ����ļ����ݴ���   
git add .     # �������и��Ĺ����ļ���index��������ɾ��               
git add -u    # �����������Ѿ����ٵ��ļ���index�����������ļ�         
git add -A    # git add . �� git add -u�ĺϼ�      
git commit -m 'xxx'                  # �ύ    
git commit --amend -m 'xxx'          # �ϲ���һ���ύ�����ڷ����޸ģ�    
git commit -am 'xxx'                 # ��add��commit��Ϊһ��    
git rm xxx                           # ɾ��index�е��ļ�    
git rm -r *                          # �ݹ�ɾ��    
git log                              # ��ʾ�ύ��־    
git log -1                           # ��ʾ1����־ -nΪn��      
git log --stat                       # ��ʾ�ύ��־����ر䶯�ļ�    
git log -p -m    
git log -- filename                  # �鿴�ļ����޸���־     
git show xxxx                        # ��ʾĳ���ύ����ϸ����    
git show dfb02                       # ��ֻ��commitid��ǰ��λ    
git show HEAD                        # ��ʾHEAD�ύ��־    
git show HEAD^                       # ��ʾ��һ���汾���ύ��־ ^^Ϊ�������汾 ^5Ϊ��5���汾                    
git whatchanged                      # ��ʾ�ύ��ʷ��Ӧ���ļ��޸�    
git revert xxxxxx                    # �����ύxxxxx
git reset xxxxxx(��ʷ�ύλ��)        # ����HEAD��xxxxx(��Զ�̷�֧��Ч)

```

# tag���
```bash
git tag                              # �г����б�ǩ
git tag -l "v1*"                     # ֧��ģ��ƥ��
git tag v2.3 <��������>               # ������ǩ��Ĭ��Ϊ��HEAD����
git tag v2.4 -a -m "test"            # ����������ǩ��������ʱʹ�ã�-a ����ʡ�ԣ�
git push origin v1.0                 # ���͵�����ǩ
git push origin --tags               # ����ȫ����ǩ
git tag -d v1.0                      # ɾ����ǩ
git push origin -- delete v1.0       # ��Զ�̿���ɾ����ǩ
git checkout v1.1                    # �����ǩ
git checkout -b v1.1-dev v1.1        # ��ĳ�� tag �Ļ������ύ����(����һ���·�֧)
git diff                             # ��ʾ����δ�����index�ı��    
git diff --cached                    # ��ʾ���������index����δcommit�ı��    
git diff HEAD^                       # �Ƚ�����һ���汾�Ĳ���    
git diff HEAD -- ./lib               # �Ƚ���HEAD�汾libĿ¼�Ĳ���    
git diff origin/master..master        # �Ƚ�Զ�̷�֧master���б��ط�֧master��û�е�                   
git diff origin/master..master --stat # ֻ��ʾ������ļ�������ʾ��������
```

# ��֧���
``` bash
git clone git+ssh://git@xxx.xxx.xxx.xxx/xx.git       # cloneԶ�ֿ̲�    
git remote add origin git+ssh://git@xxx.xxx.xxx.xxx/xx.git # ����Զ�̶��壨����push/pull/fetch��    
git branch                           # ��ʾ���ط�֧    
git branch --contains 50089          # ��ʾ�����ύ50089�ķ�֧    
git branch -a                        # ��ʾ���з�֧    
git branch -r                        # ��ʾ����ԭ����֧    
git branch --merged                  # ��ʾ�����Ѻϲ�����ǰ��֧�ķ�֧    
git branch --no-merged               # ��ʾ����δ�ϲ�����ǰ��֧�ķ�֧    
git branch -m master master_copy     # ���ط�֧����    
git branch -f ��֧�� ��ʷ�ύλ��      # ǿ�н���ָ֧�����ʷ�ύ 
git checkout -b master_copy          # �ӵ�ǰ��֧�����·�֧master_copy�����    
git checkout -b master master_copy   # �����������    
git checkout dev/minibear2333        # ����Ѵ��ڵķ�֧    
git checkout --track dev/minibear2333   # ���Զ�̷�֧dev/minibear2333���������ظ��ٷ�֧    
git checkout v2.0                    # ����汾v2.0    
git checkout -b devel origin/develop # ��Զ�̷�֧develop�����±��ط�֧devel�����    
git checkout -- README               # ���head�汾��README�ļ����������޸Ĵ�����ˣ�    
git merge origin/master              # �ϲ�Զ��master��֧����ǰ��֧    
git cherry-pick xxxxxx               # �ϲ��ύxxxxxx���޸ģ�xxxx����Ϊ����ύ��¼��    
git push origin master               # ����ǰ��֧push��Զ��master��֧    
git push origin :dev/minibear2333    # ɾ��Զ�ֿ̲��dev/minibear2333��֧    
git fetch                            # ��ȡ����Զ�̷�֧�������±��ط�֧������merge��    
git fetch --prune                    # ��ȡ����ԭ����֧���������������ɾ���ķ�֧    
git pull origin master               # ��ȡԶ�̷�֧master��merge����ǰ��֧    
git mv README README2                # �������ļ�READMEΪREADME2    
git reset --hard HEAD                # ����ǰ�汾����ΪHEAD��ͨ������mergeʧ�ܻ��ˣ�    
git rebase                           # �ϲ���֧����������Ե��ύ��ʷ(ȡ��һϵ�е��ύ��¼������һ���ط�����ȥ)
git rebase -i xxxxx                  # ��xxxxx�ύUI���棬�ɵ���˳���Լ�ȡ���
git branch -d dev/minibear2333       # ɾ����֧dev/minibear2333����Ҫȷ�ϱ���֧�޸��Ѻϲ���������֧��    
git branch -D dev/minibear2333       # ǿ��ɾ����֧dev/minibear2333��С�Ĳ���    
git ls-files                         # �г�git index�������ļ�    
git show-branch                      # ͼʾ��ǰ��֧��ʷ    
git show-branch --all                # ͼʾ���з�֧��ʷ
```

# ͼʾ����
``` bash
git ls-tree HEAD                   # �ڲ������ʾĳ��git����    
git rev-parse v2.0                 # �ڲ������ʾĳ��ref���ڵ�SHA1 HASH    
git reflog                         # ��ʾ�����ύ�����������ڵ�    
git show xxx                       # �鿴xxx�ύ�ı�����Щ�ļ�����  
git show HEAD                      # ��ʾ��ǰ��֧�����״̬    
git log --pretty=format:'%h %s' --graph             # ͼʾ�ύ��־    
git show HEAD~3                    # �鿴�����������ύ�ı�����Щ����  
git show -s --pretty=raw xxxxxx
```

# �ݴ����
``` bash
git stash                            # �ݴ浱ǰ�޸ģ���������ΪHEAD״̬    
git stash list                       # �鿴�����ݴ�    
git stash show -p stash@{0}          # �ο���һ���ݴ�    
git stash apply stash@{0}            # Ӧ�õ�һ���ݴ�
```

# ����
``` bash
git grep "delete from"               # ���ҵ�ǰ��֧�µ��ļ����ݣ�����git grep --help�������÷�                              
git grep "delete from" v2.0          # ָ��tag������
```

# ׷��
``` bash
git update-index ��assume-unchanged �ļ���      # ȡ�����ظ���    
git update-index ��no-assume-unchanged �ļ���   # �ָ����ظ���    
git ls-files -v| grep '^h\ '                  # ���Կ������ز����ٵ��ļ�
```

# ����Զ�̷�֧
``` bash
git remote              # �����������г��Ѿ����ڵ�Զ�̷�֧                          
git remote -v           #(-v�ǨCverbose �ļ�д,ȡ����ĸ)�г���ϸ��Ϣ����ÿһ�����ֺ����г���Զ��url                          
git remote add [shortname]  url              #���Զ�ֿ̲�    
git fetch origin        # �ַ��� origin ָ����Ӧ�Ĳֿ��ַ��.����˵,Ҫץȡ���� origin �е�,�����زֿ�û�е���Ϣ,������
```

# �������
``` bash
<��������>^                       # �����ƶ�һ�����ύ��¼
<��������>~<num>                  # �����ƶ�������ύ��¼
```