package com.example.inetapp.ui.Controller;

import android.graphics.Bitmap;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;

import com.example.inetapp.R;
import com.example.inetapp.databinding.FragmentControllerBinding;
import com.example.inetapp.models.RequestTask;

import java.util.concurrent.TimeUnit;

public class ControllerFragment extends Fragment {

    private FragmentControllerBinding binding;

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {

        binding = FragmentControllerBinding.inflate(inflater, container, false);
        View root = binding.getRoot();

        Button button = binding.centerButton;
        button.setOnClickListener(v -> this.rotateCamera(binding.centerButton));

        button = binding.leftButton;
        button.setOnClickListener(v -> this.rotateCamera(binding.leftButton));

        button = binding.rightButton;
        button.setOnClickListener(v -> this.rotateCamera(binding.rightButton));

        button = binding.photoButton;
        button.setOnClickListener(v -> this.getPhoto(binding.imageView));

        return root;
    }

    public void rotateCamera(View sender) {
        String targetUrl = getString(R.string.targetUrl);
        if (sender == binding.leftButton) {
            targetUrl += "set_servo_value/-1000";
        } else if (sender == binding.centerButton) {
            targetUrl += "set_servo_value/0";
        } else if (sender == binding.rightButton) {
            targetUrl += "set_servo_value/1000";
        }

        RequestTask requestTask = new RequestTask(targetUrl, "GET");
        try {
            requestTask.execute().get(10L, TimeUnit.SECONDS);
        }
        catch (Exception e) {
            e.getMessage();
        }
    }

    public void getPhoto(View sender) {
        ImageView imageView = (ImageView)sender;
        String targetUrl = getString(R.string.targetUrl) + "get-photo";
        RequestTask requestTask = new RequestTask(targetUrl, "GET");
        Object requestObject;
        try {
            requestObject = requestTask.execute().get(30L, TimeUnit.SECONDS);
        }
        catch (Exception e) {
            requestObject = e.getMessage();
        }

        if (requestObject.getClass() != String.class) {
            imageView.setImageBitmap((Bitmap) requestObject);
        }
    }

    @Override
    public void onDestroyView() {
        super.onDestroyView();
        binding = null;
    }
}