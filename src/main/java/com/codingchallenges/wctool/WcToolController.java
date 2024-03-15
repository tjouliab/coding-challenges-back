package com.codingchallenges.wctool;

import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class WcToolController {
  private final WcToolService wcToolService;

  public WcToolController(WcToolService wcToolService) {
    this.wcToolService = wcToolService;
  }

  @GetMapping("/all-files-names")
  public List<String> getAllFilesNames() {
    return wcToolService.getAllFilesNames();
  }
}

