package com.ssafy.prosn.converter;

import com.ssafy.prosn.oauth.Platform;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.convert.converter.Converter;

@Configuration
public class PlatformConverter implements Converter<String, Platform> {

    @Override
    public Platform convert(String source) {
        return Platform.valueOf(source.toUpperCase());
    }
}
