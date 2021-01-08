---
title: AtomicReference
permalink: Java/AtomicReference
date: 2021-01-04
key: JavaJava.A.AtomicReference
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AtomicReference.description }}

## Sintaxis
~~~java
public class AtomicReference<V> extends Object implements Serializable
~~~

## Constructores
* [AtomicReference()](/Java/AtomicReference/AtomicReference/)

## Métodos
* [accumulateAndGet()](/Java/AtomicReference/accumulateAndGet)
* [compareAndExchange()](/Java/AtomicReference/compareAndExchange)
* [compareAndExchangeAcquire()](/Java/AtomicReference/compareAndExchangeAcquire)
* [compareAndExchangeRelease()](/Java/AtomicReference/compareAndExchangeRelease)
* [compareAndSet()](/Java/AtomicReference/compareAndSet)
* [get()](/Java/AtomicReference/get)
* [getAcquire()](/Java/AtomicReference/getAcquire)
* [getAndAccumulate()](/Java/AtomicReference/getAndAccumulate)
* [getAndSet()](/Java/AtomicReference/getAndSet)
* [getAndUpdate()](/Java/AtomicReference/getAndUpdate)
* [getOpaque()](/Java/AtomicReference/getOpaque)
* [getPlain()](/Java/AtomicReference/getPlain)
* [lazySet()](/Java/AtomicReference/lazySet)
* [set()](/Java/AtomicReference/set)
* [setOpaque()](/Java/AtomicReference/setOpaque)
* [setPlain()](/Java/AtomicReference/setPlain)
* [setRelease()](/Java/AtomicReference/setRelease)
* [toString()](/Java/AtomicReference/toString)
* [updateAndGet()](/Java/AtomicReference/updateAndGet)
* [weakCompareAndSet()](/Java/AtomicReference/weakCompareAndSet)
* [weakCompareAndSetAcquire()](/Java/AtomicReference/weakCompareAndSetAcquire)
* [weakCompareAndSetPlain()](/Java/AtomicReference/weakCompareAndSetPlain)
* [weakCompareAndSetRelease()](/Java/AtomicReference/weakCompareAndSetRelease)
* [weakCompareAndSetVolatile()](/Java/AtomicReference/weakCompareAndSetVolatile)

## Ejemplo
~~~java
{{ site.data.Java.A.AtomicReference.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AtomicReference.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
