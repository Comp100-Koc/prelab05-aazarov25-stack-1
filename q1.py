def longest_palindromic_substring(s):
    n = len(s)
    m_len = 0 
    res = "" 
    
    for i in range(n):
        l, r = i, i 
        while l >= 0 and r < n and s[l] == s[r]: 
            if (r - l + 1) > m_len:
                m_len = r - l + 1
                res = s[l:r+1]
            l -= 1
            r += 1
            
        
        l, r = i, i + 1 
        
        while l >= 0 and r < n and s[l] == s[r]: 
            if (r - l + 1) > m_len:
                m_len = r - l + 1
                res = s[l:r+1]
                
            l -= 1
            r += 1

    if m_len < 2:
        return ""  

    return res