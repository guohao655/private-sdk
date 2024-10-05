import requests
import os

class GetPngs:
    # 创建下载文件
    def MakeDir(self, dir):
        if not os.path.exists(dir):
            os.makedirs(dir)
    
    # 创建下载url列表
    def MakeUrlList(self, base_url, start, end):
        url_list = []
        for i in range(start, end + 1):
            url = f'{base_url}/{i}.png'
            url_list.append(url)
        print(url_list)
        return url_list
    
    # 下载文件并写入对应文件夹
    def download_image(self, url, folder):
        try:
            response = requests.get(url)
            response.raise_for_status()  # 检查请求是否成功
            filename = url.split('/')[-1]  # 从URL获取文件名
            filepath = os.path.join(folder, filename)
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"图片已下载并保存为：{filepath}")
        except requests.RequestException as e:
            print(f"下载图片时出错：{e}")

    # 下载所有文件
    def download(self, image_urls, folder):
        for url in image_urls:
            self.download_image(url, folder)

if __name__ == '__main__':
    base_url = 'https://s3.ananas.chaoxing.com/sv-w9/doc/54/da/0c/5cae2a0d9dffe203123d78fe1d43c95f/thumb'
    save_folder = 'test'
    start = 1
    end = 5
    handler = GetPngs()
    handler.MakeDir(save_folder)
    url_list = handler.MakeUrlList(base_url, start, end)
    handler.download(url_list, save_folder)
