---
title: CompletionStage
permalink: /Java/CompletionStage/
date: 2021-01-11
key: Java.C.CompletionStage
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CompletionStage.description }}

## Sintaxis
~~~java
public interface CompletionStage<T>
~~~

## Métodos
* [acceptEither()](/Java/CompletionStage/acceptEither)
* [acceptEitherAsync()](/Java/CompletionStage/acceptEitherAsync)
* [applyToEither()](/Java/CompletionStage/applyToEither)
* [applyToEitherAsync()](/Java/CompletionStage/applyToEitherAsync)
* [exceptionally()](/Java/CompletionStage/exceptionally)
* [handle()](/Java/CompletionStage/handle)
* [handleAsync()](/Java/CompletionStage/handleAsync)
* [runAfterBoth()](/Java/CompletionStage/runAfterBoth)
* [runAfterBothAsync()](/Java/CompletionStage/runAfterBothAsync)
* [runAfterEither()](/Java/CompletionStage/runAfterEither)
* [runAfterEitherAsync()](/Java/CompletionStage/runAfterEitherAsync)
* [thenAccept()](/Java/CompletionStage/thenAccept)
* [thenAcceptAsync()](/Java/CompletionStage/thenAcceptAsync)
* [thenAcceptBoth()](/Java/CompletionStage/thenAcceptBoth)
* [thenAcceptBothAsync()](/Java/CompletionStage/thenAcceptBothAsync)
* [thenApply()](/Java/CompletionStage/thenApply)
* [thenApplyAsync()](/Java/CompletionStage/thenApplyAsync)
* [thenCombine()](/Java/CompletionStage/thenCombine)
* [thenCombineAsync()](/Java/CompletionStage/thenCombineAsync)
* [thenCompose()](/Java/CompletionStage/thenCompose)
* [thenComposeAsync()](/Java/CompletionStage/thenComposeAsync)
* [thenRun()](/Java/CompletionStage/thenRun)
* [thenRunAsync()](/Java/CompletionStage/thenRunAsync)
* [toCompletableFuture()](/Java/CompletionStage/toCompletableFuture)
* [whenComplete()](/Java/CompletionStage/whenComplete)
* [whenCompleteAsync()](/Java/CompletionStage/whenCompleteAsync)

## Ejemplo
~~~java
{{ site.data.Java.C.CompletionStage.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CompletionStage.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
