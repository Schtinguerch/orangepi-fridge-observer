package com.example.inetapp.models;

public abstract class Request {
    public String TargetUrl;

    public Request(String targetUrl) {
        TargetUrl = targetUrl;
    }

    public abstract Object executeRequest();
}
