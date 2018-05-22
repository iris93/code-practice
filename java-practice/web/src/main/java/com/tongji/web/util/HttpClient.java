package com.tongji.web.util;

import org.springframework.http.HttpMethod;
import org.springframework.stereotype.Service;
import org.springframework.util.MultiValueMap;

@Service
public class HttpClient {
    public String client(String url, HttpMethod method, MultiValueMap<String,String> params){
        return "hello";

    }
}
