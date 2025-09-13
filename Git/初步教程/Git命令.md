# Git常用命令

Git除了可以使用Linux的命令，还有滋生独特的命令

---

## 设置用户签名
设置用户名：
``` bash
git config --global user.name 用户名
```

设置邮箱：
``` bash
git config --global user.email 邮箱
```

## 初始化本地库
让git获取文件的管理权限
```bash
git init
```
这样会生成一个.git文件

## 查看本地库状态
``` bash
git status
```
输出三行状态：
- 分支名称
- (版本信息状态)
- (文件状态)
- (提交状态)

## 将文件添加到暂存区
```bash
git add 文件名
```
暂存区内文件可以删除，但在工作区内仍然保留：
```bash
git rm --cached 文件名
```

## 将暂存区文件提交本地库
```bash
git commit -m "版本信息" 文件名
```
查看版本信息:
``` bash
git reflog
```
查看详细版本信息（提交作者、日期等）:
``` bash
git log
```

## 修改文件
- 修改文件后，文件需要重新追踪（添加到暂存区）以及重新添加到本地库
- git显示文件修改按行显示，即只能显示新增行数和删除行数。当一行被修改时，git会认为将这行删去，然后添加一行
- git指针默认指向新版本，且修改记录不会生成副本

## 历史版本
查看版本信息:
``` bash
git reflog
```
查看详细版本信息（提交作者，日期等）:
``` bash
git log
```
版本穿梭：将指针指向指定的版本号
``` bash
git reset --hard 版本号
```