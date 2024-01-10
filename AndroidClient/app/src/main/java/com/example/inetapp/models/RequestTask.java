package com.example.inetapp.models;

import android.os.AsyncTask;

public class RequestTask extends AsyncTask<Void, Void, Object> {

    public Request request;

    public RequestTask(String targetUrl, String requestMethod) {

        if (requestMethod.equals("GET") && targetUrl.contains("get-photo")) {
            request = new GetImageRequest(targetUrl);
        }
        else if (requestMethod.equals("GET")) {
            request = new GetRequest(targetUrl);
        }
        else if (requestMethod.equals("POST")) {
            request = new PostRequest(targetUrl);
        }
    }

    @Override
    protected Object doInBackground(Void... unused) {
        return request.executeRequest();
    }
}
