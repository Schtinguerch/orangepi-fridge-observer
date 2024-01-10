package com.example.inetapp.models;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class PostRequest extends Request {


    public PostRequest(String targetUrl) {
        super(targetUrl);
    }

    @Override
    public Object executeRequest() {

        String requestText = "";

        try {
            URL url = new URL(TargetUrl);
            HttpURLConnection con = (HttpURLConnection)url.openConnection();
            con.setRequestMethod("POST");

            BufferedReader in = new BufferedReader(
                    new InputStreamReader(
                            con.getInputStream()));
            String inputLine;

            while ((inputLine = in.readLine()) != null) {
                System.out.println(inputLine);
                requestText += inputLine;
            }
            in.close();
        }
        catch (Exception e) {
            requestText = e.getMessage();
        }
        return requestText;
    }
}
