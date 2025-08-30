from optparse import OptionParser, OptionGroup
import os

def main():
    usage = 'usage: %prog [options] filename'
    parser = OptionParser(usage=usage)

    # 基本オプション
    parser.add_option('-f', '--file', action='store', type='string',
                      dest='filename', help='読み込むファイル名')
    parser.add_option('-v', '--verbose', action='store_true', dest='verbose',
                      help='詳細モード')
    parser.add_option('-q', '--quiet', action='store_false', dest='verbose',
                      help='静かなモード')

    # 危険なオプショングループ
    group = OptionGroup(parser, 'Dangerous options')
    group.add_option('--delete', action='store_true', help='ファイルを削除する')
    parser.add_option_group(group)

    options, args = parser.parse_args()

    if not options.filename:
        parser.error("ファイル名を指定してください -f filename")

    if not os.path.exists(options.filename):
        parser.error(f"ファイルが存在しません: {options.filename}")

    # 行数カウント
    with open(options.filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        count = len(lines)

    if options.verbose:
        print(f"ファイル名: {options.filename}")
    print(f"行数: {count}")

    # 危険操作
    if getattr(options, 'delete', False):
        os.remove(options.filename)
        print(f"⚠️ ファイル {options.filename} を削除しました")

if __name__ == '__main__':
    main()
