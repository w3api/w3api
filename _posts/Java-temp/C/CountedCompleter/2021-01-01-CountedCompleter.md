---
title: CountedCompleter
permalink: /Java/CountedCompleter/
date: 2021-01-11
key: Java.C.CountedCompleter
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'clase java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CountedCompleter.description }}

## Sintaxis
~~~java
public abstract class CountedCompleter<T> extends ForkJoinTask<T>
~~~

## Constructores
* [CountedCompleter()](/Java/CountedCompleter/CountedCompleter/)

## Métodos
* [addToPendingCount()](/Java/CountedCompleter/addToPendingCount)
* [compareAndSetPendingCount()](/Java/CountedCompleter/compareAndSetPendingCount)
* [complete()](/Java/CountedCompleter/complete)
* [compute()](/Java/CountedCompleter/compute)
* [decrementPendingCountUnlessZero()](/Java/CountedCompleter/decrementPendingCountUnlessZero)
* [exec()](/Java/CountedCompleter/exec)
* [firstComplete()](/Java/CountedCompleter/firstComplete)
* [getCompleter()](/Java/CountedCompleter/getCompleter)
* [getPendingCount()](/Java/CountedCompleter/getPendingCount)
* [getRawResult()](/Java/CountedCompleter/getRawResult)
* [getRoot()](/Java/CountedCompleter/getRoot)
* [helpComplete()](/Java/CountedCompleter/helpComplete)
* [nextComplete()](/Java/CountedCompleter/nextComplete)
* [onCompletion()](/Java/CountedCompleter/onCompletion)
* [onExceptionalCompletion()](/Java/CountedCompleter/onExceptionalCompletion)
* [propagateCompletion()](/Java/CountedCompleter/propagateCompletion)
* [quietlyCompleteRoot()](/Java/CountedCompleter/quietlyCompleteRoot)
* [setPendingCount()](/Java/CountedCompleter/setPendingCount)
* [setRawResult()](/Java/CountedCompleter/setRawResult)
* [tryComplete()](/Java/CountedCompleter/tryComplete)

## Ejemplo
~~~java
{{ site.data.Java.C.CountedCompleter.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.CountedCompleter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
