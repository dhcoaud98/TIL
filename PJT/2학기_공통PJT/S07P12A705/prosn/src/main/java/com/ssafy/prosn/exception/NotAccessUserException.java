package com.ssafy.prosn.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

/**
 * created by seongmin on 2022/08/08
 */
@ResponseStatus(HttpStatus.FORBIDDEN)
public class NotAccessUserException extends RuntimeException {
    public NotAccessUserException(String message) {
        super(message);
    }
}
