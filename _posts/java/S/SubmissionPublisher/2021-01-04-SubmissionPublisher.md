---
title: SubmissionPublisher
permalink: Java/SubmissionPublisher
date: 2021-01-04
key: JavaJava.S.SubmissionPublisher
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'clase java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SubmissionPublisher.description }}

## Sintaxis
~~~java
public class SubmissionPublisher<T> extends Object implements Flow.Publisher<T>, AutoCloseable
~~~

## Constructores
* [SubmissionPublisher()](/Java/SubmissionPublisher/SubmissionPublisher/)

## Métodos
* [close()](/Java/SubmissionPublisher/close)
* [closeExceptionally()](/Java/SubmissionPublisher/closeExceptionally)
* [consume()](/Java/SubmissionPublisher/consume)
* [estimateMaximumLag()](/Java/SubmissionPublisher/estimateMaximumLag)
* [estimateMinimumDemand()](/Java/SubmissionPublisher/estimateMinimumDemand)
* [getClosedException()](/Java/SubmissionPublisher/getClosedException)
* [getExecutor()](/Java/SubmissionPublisher/getExecutor)
* [getMaxBufferCapacity()](/Java/SubmissionPublisher/getMaxBufferCapacity)
* [getNumberOfSubscribers()](/Java/SubmissionPublisher/getNumberOfSubscribers)
* [getSubscribers()](/Java/SubmissionPublisher/getSubscribers)
* [hasSubscribers()](/Java/SubmissionPublisher/hasSubscribers)
* [isClosed()](/Java/SubmissionPublisher/isClosed)
* [isSubscribed()](/Java/SubmissionPublisher/isSubscribed)
* [offer()](/Java/SubmissionPublisher/offer)
* [submit()](/Java/SubmissionPublisher/submit)
* [subscribe()](/Java/SubmissionPublisher/subscribe)

## Ejemplo
~~~java
{{ site.data.Java.S.SubmissionPublisher.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SubmissionPublisher.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
