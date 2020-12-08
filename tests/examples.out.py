name = [1,2,3]
alpha = 1
beta = 2
gamma = 3
root = '/'
image_id = 'temp.png'
image_ext = '.png'
print("hello, {}".format(name[0]))
s = "{},{},{:06d}".format(alpha, beta, gamma)
s2 = "{}/training/label_2/{}.txt".format(root, image_id)
s3 = "{}/training/image_2/{}.{}".format(root, image_id, image_ext)