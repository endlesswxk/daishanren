# latestVersion 阴阳师最最最终版
* ## 阴阳师流程细化说明
   1. ###  流程： 包含一系列的行为 可重复
   2. ###  行为： 包含三个操作(上一个操作， 本次操作， 下一个操作)
   3.   *  ### 操作：
      * 一张图
      * 判断存在、点击、滑动滚轮
      * 坐标(坐标图片同时存在的情况下判断图片是否存在，如不存在点击对应坐标 说明： 或许可以不使用)
      * 操作的描述
  4. ### 异常处理， 一个行为三个操作都没有捕捉到,则在下一个行为死等 5分钟
#### ps: 以后再也不新增脚本