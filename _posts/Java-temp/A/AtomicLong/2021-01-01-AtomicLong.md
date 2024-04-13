---
title: AtomicLong
permalink: /Java/AtomicLong/
date: 2021-01-11
key: Java.A.AtomicLong
category: Java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AtomicLong.description }}

## Sintaxis
~~~java
public class AtomicLong extends Number implements Serializable
~~~

## Constructores
* [AtomicLong()](/Java/AtomicLong/AtomicLong/)

## Métodos
* [accumulateAndGet()](/Java/AtomicLong/accumulateAndGet)
* [addAndGet()](/Java/AtomicLong/addAndGet)
* [compareAndExchange()](/Java/AtomicLong/compareAndExchange)
* [compareAndExchangeAcquire()](/Java/AtomicLong/compareAndExchangeAcquire)
* [compareAndExchangeRelease()](/Java/AtomicLong/compareAndExchangeRelease)
* [compareAndSet()](/Java/AtomicLong/compareAndSet)
* [decrementAndGet()](/Java/AtomicLong/decrementAndGet)
* [doubleValue()](/Java/AtomicLong/doubleValue)
* [floatValue()](/Java/AtomicLong/floatValue)
* [get()](/Java/AtomicLong/get)
* [getAcquire()](/Java/AtomicLong/getAcquire)
* [getAndAccumulate()](/Java/AtomicLong/getAndAccumulate)
* [getAndAdd()](/Java/AtomicLong/getAndAdd)
* [getAndDecrement()](/Java/AtomicLong/getAndDecrement)
* [getAndIncrement()](/Java/AtomicLong/getAndIncrement)
* [getAndSet()](/Java/AtomicLong/getAndSet)
* [getAndUpdate()](/Java/AtomicLong/getAndUpdate)
* [getOpaque()](/Java/AtomicLong/getOpaque)
* [getPlain()](/Java/AtomicLong/getPlain)
* [incrementAndGet()](/Java/AtomicLong/incrementAndGet)
* [intValue()](/Java/AtomicLong/intValue)
* [lazySet()](/Java/AtomicLong/lazySet)
* [longValue()](/Java/AtomicLong/longValue)
* [set()](/Java/AtomicLong/set)
* [setOpaque()](/Java/AtomicLong/setOpaque)
* [setPlain()](/Java/AtomicLong/setPlain)
* [setRelease()](/Java/AtomicLong/setRelease)
* [toString()](/Java/AtomicLong/toString)
* [updateAndGet()](/Java/AtomicLong/updateAndGet)
* [weakCompareAndSet()](/Java/AtomicLong/weakCompareAndSet)
* [weakCompareAndSetAcquire()](/Java/AtomicLong/weakCompareAndSetAcquire)
* [weakCompareAndSetPlain()](/Java/AtomicLong/weakCompareAndSetPlain)
* [weakCompareAndSetRelease()](/Java/AtomicLong/weakCompareAndSetRelease)
* [weakCompareAndSetVolatile()](/Java/AtomicLong/weakCompareAndSetVolatile)

## Ejemplo
~~~java
{{ site.data.Java.A.AtomicLong.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AtomicLong.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
