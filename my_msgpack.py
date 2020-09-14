import msgpack
import json
import os


# 解文件夹包 解压数据在同级目录中
def unpack_dir(file_path):
    buf = open(file_path +"/assets.msgpack", "rb")
    unpacker = msgpack.Unpacker(buf, raw=False)
    print(type(unpacker))
    for unpacked in unpacker:
        print(type(unpacked), len(unpacked))
        for i in unpacked:
            print(i)
            if os.path.exists(file_path + "/" + i[:i.rindex('/')]) is False:
                os.makedirs(file_path + "/" + i[:i.rindex('/')])
            open(file_path + "/" +i, "wb+").write(unpacked[i])


# 序列化文件夹包  打包的数据在文件夹内
def pack_dir(dir_root):
    file_dict = {}
    for root, dirs, files in os.walk(dir_root):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            path = os.path.join(root, f)
            path = path.replace("\\", "/")
            print(path)
            file_dict[str(path).replace(dir_root + "/", "")] = open(path, "rb").read()

    with open(dir_root+"\\new_assets.msgpack", 'wb') as f:
        msgpack.dump(file_dict, f)

# 格式化文本数据
def unpack_file(file):
    buf = open(file, "rb")
    unpacker = msgpack.Unpacker(buf, raw=False)
    print(type(unpacker))
    for unpacked in unpacker:
        print(unpacked)
        open(file+"_.txt", "wb").write(json.dumps(unpacked, ensure_ascii=False, indent=4))


# 序列化文本
def pack_file(file):
    data = json.loads(open(file, "r+", encoding="utf8").read())
    with open(file + "_.msgpack", 'wb') as f:
        # 存储数据
        msgpack.dump(data, f)


if __name__ == '__main__':
    pack_dir(r'D:/xx')
