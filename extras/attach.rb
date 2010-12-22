class Attach <Formula
  head 'git://github.com/spookyet/attach.git'

  depends_on 'dtach'

  def install
    bin.install "attach"
  end
end
