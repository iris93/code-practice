package com.tongji.web.controller;

import com.tongji.web.domain.User;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloWorldController {
    @RequestMapping("/getMysqlUser")
    public User getUser(){
        User user = new User();
        user.setUserName("小明");
        user.setPassWord("1234");
        return user;
    }
}
