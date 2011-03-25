require 'formula'

class Attach < Formula
  url 'git://github.com/sorin-ionescu/attach.git', :tag => '1.0.4'
  head 'git://github.com/sorin-ionescu/attach.git'
  homepage 'http://github.com/sorin-ionescu/attach'
  version '1.0.4'
  depends_on 'dtach'

  def install
    bin.install 'attach'
    man1.install 'attach.1'
  end
end

