require 'formula'

class Attach < Formula
  url 'git://github.com/SpookyET/attach.git', :tag => '1.0.0'
  head 'git://github.com/SpookyET/attach.git'
  homepage 'http://github.com/SpookyET/attach'
  version '1.0.0'
  depends_on 'dtach'

  def install
    bin.install 'attach'
    man1.install 'attach.1'
  end
end

