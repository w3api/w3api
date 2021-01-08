---
title: AtomicReferenceFieldUpdater
permalink: Java/AtomicReferenceFieldUpdater
date: 2021-01-04
key: JavaJava.A.AtomicReferenceFieldUpdater
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AtomicReferenceFieldUpdater.description }}

## Sintaxis
~~~java
public abstract class AtomicReferenceFieldUpdater<T,V> extends Object
~~~

## Constructores
* [AtomicReferenceFieldUpdater()](/Java/AtomicReferenceFieldUpdater/AtomicReferenceFieldUpdater/)

## Métodos
* [accumulateAndGet()](/Java/AtomicReferenceFieldUpdater/accumulateAndGet)
* [compareAndSet()](/Java/AtomicReferenceFieldUpdater/compareAndSet)
* [get()](/Java/AtomicReferenceFieldUpdater/get)
* [getAndAccumulate()](/Java/AtomicReferenceFieldUpdater/getAndAccumulate)
* [getAndSet()](/Java/AtomicReferenceFieldUpdater/getAndSet)
* [getAndUpdate()](/Java/AtomicReferenceFieldUpdater/getAndUpdate)
* [lazySet()](/Java/AtomicReferenceFieldUpdater/lazySet)
* [newUpdater()](/Java/AtomicReferenceFieldUpdater/newUpdater)
* [set()](/Java/AtomicReferenceFieldUpdater/set)
* [updateAndGet()](/Java/AtomicReferenceFieldUpdater/updateAndGet)
* [weakCompareAndSet()](/Java/AtomicReferenceFieldUpdater/weakCompareAndSet)

## Ejemplo
~~~java
{{ site.data.Java.A.AtomicReferenceFieldUpdater.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AtomicReferenceFieldUpdater.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
