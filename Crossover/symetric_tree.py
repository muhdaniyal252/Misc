def solution(t):

  def helper(left,right):
    if not left and not right:
      return True
    if not left or not right:
      return False

    return (left.value == right.value and helper(left.left,right.right) and helper(left.right,right.left))

  if not t:
    return True
  return helper(t.left,t.right)
