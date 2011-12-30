require 'formula'

class Attach < Formula
  url 'https://github.com/sorin-ionescu/attach/tarball/1.0.5'
  head 'https://github.com/sorin-ionescu/attach.git'
  homepage 'http://github.com/sorin-ionescu/attach'
  md5 '351d3ad4356513fe8a6bed05696726bb'

  depends_on 'dtach'

  def install
    bin.install 'attach'
    man1.install 'attach.1'
  end
end

