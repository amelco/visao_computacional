-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

Format: 3.0 (quilt)
Source: opencv
Binary: opencv-doc, libopencv-dev, opencv-data, libopencv-core-dev, libopencv-core4.2, libopencv-ml-dev, libopencv-ml4.2, libopencv-imgproc-dev, libopencv-imgproc4.2, libopencv-imgcodecs-dev, libopencv-imgcodecs4.2, libopencv-video-dev, libopencv-video4.2, libopencv-videoio-dev, libopencv-videoio4.2, libopencv-objdetect-dev, libopencv-objdetect4.2, libopencv-highgui-dev, libopencv-highgui4.2, libopencv-calib3d-dev, libopencv-calib3d4.2, libopencv-flann-dev, libopencv-flann4.2, libopencv-dnn-dev, libopencv-dnn4.2, libopencv-features2d-dev, libopencv-features2d4.2, libopencv-ts-dev, libopencv-photo-dev, libopencv-photo4.2, libopencv-videostab-dev, libopencv-videostab4.2, libopencv-stitching-dev, libopencv-stitching4.2, libopencv-shape-dev, libopencv-shape4.2, libopencv-superres-dev, libopencv-superres4.2, libopencv-viz-dev, libopencv-viz4.2, libopencv-contrib-dev, libopencv-contrib4.2, libopencv4.2-java, libopencv4.2-jni, python3-opencv
Architecture: any all
Version: 4.2.0+dfsg-5
Maintainer: Debian Science Team <debian-science-maintainers@lists.alioth.debian.org>
Uploaders:  Sam Hocevar (Debian packages) <sam+deb@zoy.org>, Nobuhiro Iwamatsu <iwamatsu@debian.org>, Mo Zhou <lumin@debian.org>,
Homepage: https://opencv.org
Standards-Version: 4.5.0
Vcs-Browser: https://salsa.debian.org/science-team/opencv
Vcs-Git: https://salsa.debian.org/science-team/opencv.git
Testsuite: autopkgtest
Testsuite-Triggers: python3, python3-numpy
Build-Depends: ant [!hppa !hurd-any !kfreebsd-any], cmake (>= 2.8.7), debhelper-compat (= 12), default-jdk [!hppa !hurd-any !kfreebsd-any], dh-python, doxygen, javahelper, ninja-build, libavcodec-dev, libavformat-dev, libavresample-dev, libdc1394-22-dev [linux-any], libeigen3-dev, libgdal-dev, libgdcm-dev [!hppa !m68k !powerpcspe !sh4 !sparc64 !x32], libgl1-mesa-dev, libglu1-mesa-dev, libgoogle-glog-dev, libgphoto2-dev, libgtk-3-dev, libjpeg-dev, liblapack-dev (>= 3.2.1), libleptonica-dev, libopenexr-dev (>= 1.6.1-8.1), libilmbase-dev, libpng-dev, libprotobuf-dev, libraw1394-dev [linux-any], libswscale-dev, libtbb-dev [amd64 arm64 armel armhf i386 mips mips64el mipsel ppc64el s390x powerpc powerpcspe ppc64 riscv64 sh4 sparc64], libtesseract-dev, libtiff-dev, libv4l-dev [linux-any], libvtk6-dev, libvtkgdcm-dev [!alpha !ppc64 !x32], libgdcm-tools, libgstreamer1.0-dev, libgstreamer-plugins-base1.0-dev, maven-repo-helper [!hppa !hurd-any !kfreebsd-any], ocl-icd-opencl-dev, protobuf-compiler, python3-dev, python3-numpy, python3-bs4, zlib1g-dev (>= 1.2.5)
Package-List:
 libopencv-calib3d-dev deb libdevel optional arch=any
 libopencv-calib3d4.2 deb libs optional arch=any
 libopencv-contrib-dev deb libdevel optional arch=any
 libopencv-contrib4.2 deb libs optional arch=any
 libopencv-core-dev deb libdevel optional arch=any
 libopencv-core4.2 deb libs optional arch=any
 libopencv-dev deb libdevel optional arch=any
 libopencv-dnn-dev deb libdevel optional arch=any
 libopencv-dnn4.2 deb libs optional arch=any
 libopencv-features2d-dev deb libdevel optional arch=any
 libopencv-features2d4.2 deb libs optional arch=any
 libopencv-flann-dev deb libdevel optional arch=any
 libopencv-flann4.2 deb libs optional arch=any
 libopencv-highgui-dev deb libdevel optional arch=any
 libopencv-highgui4.2 deb libs optional arch=any
 libopencv-imgcodecs-dev deb libdevel optional arch=any
 libopencv-imgcodecs4.2 deb libs optional arch=any
 libopencv-imgproc-dev deb libdevel optional arch=any
 libopencv-imgproc4.2 deb libs optional arch=any
 libopencv-ml-dev deb libdevel optional arch=any
 libopencv-ml4.2 deb libs optional arch=any
 libopencv-objdetect-dev deb libdevel optional arch=any
 libopencv-objdetect4.2 deb libs optional arch=any
 libopencv-photo-dev deb libdevel optional arch=any
 libopencv-photo4.2 deb libs optional arch=any
 libopencv-shape-dev deb libdevel optional arch=any
 libopencv-shape4.2 deb libs optional arch=any
 libopencv-stitching-dev deb libdevel optional arch=any
 libopencv-stitching4.2 deb libs optional arch=any
 libopencv-superres-dev deb libdevel optional arch=any
 libopencv-superres4.2 deb libs optional arch=any
 libopencv-ts-dev deb libdevel optional arch=any
 libopencv-video-dev deb libdevel optional arch=any
 libopencv-video4.2 deb libs optional arch=any
 libopencv-videoio-dev deb libdevel optional arch=any
 libopencv-videoio4.2 deb libs optional arch=any
 libopencv-videostab-dev deb libdevel optional arch=any
 libopencv-videostab4.2 deb libs optional arch=any
 libopencv-viz-dev deb libdevel optional arch=any
 libopencv-viz4.2 deb libs optional arch=any
 libopencv4.2-java deb java optional arch=all
 libopencv4.2-jni deb java optional arch=amd64,arm64,armel,armhf,i386,mips64el,mipsel,ppc64el,s390x,alpha,ia64,m68k,powerpc,ppc64,riscv64,sh4,sparc64,x32
 opencv-data deb libdevel optional arch=all
 opencv-doc deb doc optional arch=all
 python3-opencv deb python optional arch=any
Checksums-Sha1:
 636b76bc1cee81f0286457694965d7dd0ebca99f 54221512 opencv_4.2.0+dfsg.orig-contrib.tar.xz
 ce9188b63d1eaf9bd64af6f3d136617ad6867bf7 72063656 opencv_4.2.0+dfsg.orig.tar.xz
 f2567e43f2515cf6ab2a3fe5dd19eeb12afc6d6b 32204 opencv_4.2.0+dfsg-5.debian.tar.xz
Checksums-Sha256:
 c5b1e63326d2932f35fc3e631f39aa7f17ca1634d28f441e537d21915ab4fb53 54221512 opencv_4.2.0+dfsg.orig-contrib.tar.xz
 3072f9e25cbf48643a406c497d63cf12e71606da8b82fe2e2ed7b57a42a66b42 72063656 opencv_4.2.0+dfsg.orig.tar.xz
 d06f7bfc1206076f44dcc533dc030dfff9e6dd76936dd64e83d5930248c104eb 32204 opencv_4.2.0+dfsg-5.debian.tar.xz
Files:
 39e6e6965933d387b0ccfa81accf5903 54221512 opencv_4.2.0+dfsg.orig-contrib.tar.xz
 a7b5cdd3421bf76603a9104dc3f15362 72063656 opencv_4.2.0+dfsg.orig.tar.xz
 2e9f9b0ae0e757664bfec3ca9b4ce4f8 32204 opencv_4.2.0+dfsg-5.debian.tar.xz

-----BEGIN PGP SIGNATURE-----

iQJFBAEBCgAvFiEEY4vHXsHlxYkGfjXeYmRes19oaooFAl5LWwgRHGx1bWluQGRl
Ymlhbi5vcmcACgkQYmRes19oaooiqQ/+JczxZ5CjDgcHsCGpVqlXhP3aWU5z+Ac6
/1ueSp5EN9XMm+zp9bsNAlnhfv5ZvFoLQIhAEQZbEchj3EyH4ovHMZu7w/16PwRx
22g7caLTjbHrdWeFXh/MlWePpdpyESUxvoZaQWsiVz3LC1WMB+YP1QZi1VA+ABF4
SmWe72UqyIb161G+r6NwDp7VNt6MnFW9NXcyWJImdUIfB6PbuepuUJT8MG5jXg8u
YKFxko9zCAUM21JRPvWWIU+UrjzOv7k8aRE1MuON7mvLxW4947TyI1sgeKtD6/7V
LlbLrIjy4C4ehDsgQZdiKu2C6apNIN9BY55MkDwd3Iz+J3Z/B9Wx/1jqlUdvxfSZ
1dVvFP2O//kmSUCrXvyfciDQWg1WiiDS021vSXAh9M/MINE6umy63eKdJjDeLpOU
AGmpHQ9wtbNHsISsi8RHZhNDTdmOipu1Ifyyf62DoI4ZVUNUS8isewG4Sdk/lCeQ
UZTTmOC8uvf3Ka1zeXilh7FTGpcOoxI57ZMFN3UIHh1vWmAWnH2tknC2axskSoJP
vwT/pC+3jj7f8AIOb6HKwbXPunbkd2ThIGmnq+mLHG8wv0Pa/tTEzEuPkEwXIArv
kJFTV0RvF0utWGgNEAQplZiUKJgFYEZMYqAFJhtJjpKn9UvSLvS+JV0X40nGIVRG
hi/yra9yboU=
=lcNp
-----END PGP SIGNATURE-----
