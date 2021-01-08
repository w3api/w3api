---
title: CompletableFuture
permalink: Java/CompletableFuture
date: 2021-01-04
key: JavaJava.C.CompletableFuture
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'clase java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CompletableFuture.description }}

## Sintaxis
~~~java
public class CompletableFuture<T> extends Object implements Future<T>, CompletionStage<T>
~~~

## Constructores
* [CompletableFuture()](/Java/CompletableFuture/CompletableFuture/)

## Métodos
* [allOf()](/Java/CompletableFuture/allOf)
* [anyOf()](/Java/CompletableFuture/anyOf)
* [cancel()](/Java/CompletableFuture/cancel)
* [complete()](/Java/CompletableFuture/complete)
* [completeAsync()](/Java/CompletableFuture/completeAsync)
* [completedFuture()](/Java/CompletableFuture/completedFuture)
* [completedStage()](/Java/CompletableFuture/completedStage)
* [completeExceptionally()](/Java/CompletableFuture/completeExceptionally)
* [completeOnTimeout()](/Java/CompletableFuture/completeOnTimeout)
* [copy()](/Java/CompletableFuture/copy)
* [defaultExecutor()](/Java/CompletableFuture/defaultExecutor)
* [delayedExecutor()](/Java/CompletableFuture/delayedExecutor)
* [exceptionally()](/Java/CompletableFuture/exceptionally)
* [failedFuture()](/Java/CompletableFuture/failedFuture)
* [failedStage()](/Java/CompletableFuture/failedStage)
* [get()](/Java/CompletableFuture/get)
* [getNow()](/Java/CompletableFuture/getNow)
* [getNumberOfDependents()](/Java/CompletableFuture/getNumberOfDependents)
* [isCancelled()](/Java/CompletableFuture/isCancelled)
* [isCompletedExceptionally()](/Java/CompletableFuture/isCompletedExceptionally)
* [isDone()](/Java/CompletableFuture/isDone)
* [join()](/Java/CompletableFuture/join)
* [minimalCompletionStage()](/Java/CompletableFuture/minimalCompletionStage)
* [newIncompleteFuture()](/Java/CompletableFuture/newIncompleteFuture)
* [obtrudeException()](/Java/CompletableFuture/obtrudeException)
* [obtrudeValue()](/Java/CompletableFuture/obtrudeValue)
* [orTimeout()](/Java/CompletableFuture/orTimeout)
* [runAsync()](/Java/CompletableFuture/runAsync)
* [supplyAsync()](/Java/CompletableFuture/supplyAsync)
* [toCompletableFuture()](/Java/CompletableFuture/toCompletableFuture)
* [toString()](/Java/CompletableFuture/toString)

## Ejemplo
~~~java
{{ site.data.Java.C.CompletableFuture.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CompletableFuture.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
