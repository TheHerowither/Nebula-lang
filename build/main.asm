extern _ExitProcess@4
section .text
   global _start
_start:
    push ebp
    mov ebp, esp
    sub esp, 4
    mov dword [ebp-4], 60
    mov eax, [ebp-4]
    sub esp, 8
    mov dword [ebp-8], 256
    mov eax, [ebp-8]
    sub esp, 12
    mov dword [ebp-12], 14
    mov eax, [ebp-12]
    mov eax, [ebp-8]
    push eax
    call _ExitProcess@4