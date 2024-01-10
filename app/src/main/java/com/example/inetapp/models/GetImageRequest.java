package com.example.inetapp.models;

import android.graphics.BitmapFactory;

import java.io.BufferedInputStream;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class GetImageRequest extends Request {
    public GetImageRequest(String targetUrl) {
        super(targetUrl);
    }

    @Override
    public Object executeRequest() {

        String errorText = "";

        try {
            URL url = new URL(TargetUrl);
            HttpURLConnection con = (HttpURLConnection)url.openConnection();
            con.setRequestMethod("GET");

            InputStream in = new BufferedInputStream(con.getInputStream());
            ByteArrayOutputStream out = new ByteArrayOutputStream();

            byte[] buf = new byte[2048];
            int length = 0;
            while ((length = in.read(buf)) != -1) {
                out.write(buf, 0, length);
            }

            out.close();
            in.close();
            byte[] response = out.toByteArray();
            return BitmapFactory.decodeByteArray(response, 0, response.length);
        }
        catch (Exception e) {
            errorText = e.getMessage();
            return errorText;
        }
    }
}
