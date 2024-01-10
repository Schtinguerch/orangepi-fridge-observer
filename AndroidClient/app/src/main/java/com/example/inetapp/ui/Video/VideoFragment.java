package com.example.inetapp.ui.Video;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.VideoView;
import android.widget.MediaController;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;

import com.example.inetapp.R;
import com.example.inetapp.databinding.FragmentVideoBinding;

public class VideoFragment extends Fragment {

    private FragmentVideoBinding binding;
    VideoView videoPlayer;

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {

        binding = FragmentVideoBinding.inflate(inflater, container, false);
        View root = binding.getRoot();

        Button button = binding.videoButton;
        button.setOnClickListener(v -> this.play(binding.videoButton));
        return root;
    }

    public void play(View sender) {
        videoPlayer = binding.videoPlayer;
        videoPlayer.setVideoPath(getString(R.string.targetUrl) + "get-video");
        MediaController mediaController = new MediaController(this.getContext());
        videoPlayer.setMediaController(mediaController);
        mediaController.setMediaPlayer(videoPlayer);
        videoPlayer.start();
    }

    @Override
    public void onDestroyView() {
        super.onDestroyView();
        binding = null;
    }
}