let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/Documents/PycharmProjects/Courses/Computational_Finance/other
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
if &shortmess =~ 'A'
  set shortmess=aoOA
else
  set shortmess=aoO
endif
badd +1 inv_BS.py
badd +1 ~/Documents/PycharmProjects/Courses/Computational_Finance/Hand-in_1/1.3.py
badd +2 ~/Documents/PycharmProjects/Courses/Computational_Finance/Hand-in_1/1.8.py
argglobal
%argdel
$argadd inv_BS.py
edit ~/Documents/PycharmProjects/Courses/Computational_Finance/Hand-in_1
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
split
1wincmd k
wincmd _ | wincmd |
vsplit
wincmd _ | wincmd |
vsplit
2wincmd h
wincmd w
wincmd w
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe '1resize ' . ((&lines * 44 + 31) / 62)
exe 'vert 1resize ' . ((&columns * 51 + 102) / 204)
exe '2resize ' . ((&lines * 44 + 31) / 62)
exe 'vert 2resize ' . ((&columns * 76 + 102) / 204)
exe '3resize ' . ((&lines * 44 + 31) / 62)
exe 'vert 3resize ' . ((&columns * 75 + 102) / 204)
exe '4resize ' . ((&lines * 15 + 31) / 62)
argglobal
balt inv_BS.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 13 - ((12 * winheight(0) + 22) / 44)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 13
normal! 0
lcd ~/Documents/PycharmProjects/Courses/Computational_Finance/other
wincmd w
argglobal
if bufexists(fnamemodify("~/Documents/PycharmProjects/Courses/Computational_Finance/Hand-in_1/1.3.py", ":p")) | buffer ~/Documents/PycharmProjects/Courses/Computational_Finance/Hand-in_1/1.3.py | else | edit ~/Documents/PycharmProjects/Courses/Computational_Finance/Hand-in_1/1.3.py | endif
if &buftype ==# 'terminal'
  silent file ~/Documents/PycharmProjects/Courses/Computational_Finance/Hand-in_1/1.3.py
endif
balt ~/Documents/PycharmProjects/Courses/Computational_Finance/other/inv_BS.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 1 - ((0 * winheight(0) + 22) / 44)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
wincmd w
argglobal
if bufexists(fnamemodify("~/Documents/PycharmProjects/Courses/Computational_Finance/Hand-in_1/1.3.py", ":p")) | buffer ~/Documents/PycharmProjects/Courses/Computational_Finance/Hand-in_1/1.3.py | else | edit ~/Documents/PycharmProjects/Courses/Computational_Finance/Hand-in_1/1.3.py | endif
if &buftype ==# 'terminal'
  silent file ~/Documents/PycharmProjects/Courses/Computational_Finance/Hand-in_1/1.3.py
endif
balt ~/Documents/PycharmProjects/Courses/Computational_Finance/other/inv_BS.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 1 - ((0 * winheight(0) + 22) / 44)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
wincmd w
argglobal
if bufexists(fnamemodify("term://~/Documents/PycharmProjects/Courses/Computational_Finance/other//7550:/bin/zsh;\#toggleterm\#1", ":p")) | buffer term://~/Documents/PycharmProjects/Courses/Computational_Finance/other//7550:/bin/zsh;\#toggleterm\#1 | else | edit term://~/Documents/PycharmProjects/Courses/Computational_Finance/other//7550:/bin/zsh;\#toggleterm\#1 | endif
if &buftype ==# 'terminal'
  silent file term://~/Documents/PycharmProjects/Courses/Computational_Finance/other//7550:/bin/zsh;\#toggleterm\#1
endif
balt ~/Documents/PycharmProjects/Courses/Computational_Finance/Hand-in_1/1.3.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 1 - ((0 * winheight(0) + 7) / 15)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 022|
wincmd w
4wincmd w
exe '1resize ' . ((&lines * 44 + 31) / 62)
exe 'vert 1resize ' . ((&columns * 51 + 102) / 204)
exe '2resize ' . ((&lines * 44 + 31) / 62)
exe 'vert 2resize ' . ((&columns * 76 + 102) / 204)
exe '3resize ' . ((&lines * 44 + 31) / 62)
exe 'vert 3resize ' . ((&columns * 75 + 102) / 204)
exe '4resize ' . ((&lines * 15 + 31) / 62)
tabnext 1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20
let &shortmess = s:shortmess_save
let &winminheight = s:save_winminheight
let &winminwidth = s:save_winminwidth
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
