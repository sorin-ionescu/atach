require 'formula'

class Attach <Formula
  head 'git://github.com/SpookyET/attach.git'

  depends_on 'dtach'

  def install
    bin.install "attach"
  end
end

