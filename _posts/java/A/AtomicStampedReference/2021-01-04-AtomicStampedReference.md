---
title: AtomicStampedReference
permalink: Java/AtomicStampedReference
date: 2021-01-04
key: JavaJava.A.AtomicStampedReference
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AtomicStampedReference.description }}

## Sintaxis
~~~java
public class AtomicStampedReference<V> extends Object
~~~

## Constructores
* [AtomicStampedReference()](/Java/AtomicStampedReference/AtomicStampedReference/)

## Métodos
* [attemptStamp()](/Java/AtomicStampedReference/attemptStamp)
* [compareAndSet()](/Java/AtomicStampedReference/compareAndSet)
* [get()](/Java/AtomicStampedReference/get)
* [getReference()](/Java/AtomicStampedReference/getReference)
* [getStamp()](/Java/AtomicStampedReference/getStamp)
* [set()](/Java/AtomicStampedReference/set)
* [weakCompareAndSet()](/Java/AtomicStampedReference/weakCompareAndSet)

## Ejemplo
~~~java
{{ site.data.Java.A.AtomicStampedReference.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AtomicStampedReference.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
