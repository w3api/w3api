---
title: AtomicMarkableReference
permalink: Java/AtomicMarkableReference
date: 2021-01-04
key: JavaJava.A.AtomicMarkableReference
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AtomicMarkableReference.description }}

## Sintaxis
~~~java
public class AtomicMarkableReference<V> extends Object
~~~

## Constructores
* [AtomicMarkableReference()](/Java/AtomicMarkableReference/AtomicMarkableReference/)

## Métodos
* [attemptMark()](/Java/AtomicMarkableReference/attemptMark)
* [compareAndSet()](/Java/AtomicMarkableReference/compareAndSet)
* [get()](/Java/AtomicMarkableReference/get)
* [getReference()](/Java/AtomicMarkableReference/getReference)
* [isMarked()](/Java/AtomicMarkableReference/isMarked)
* [set()](/Java/AtomicMarkableReference/set)
* [weakCompareAndSet()](/Java/AtomicMarkableReference/weakCompareAndSet)

## Ejemplo
~~~java
{{ site.data.Java.A.AtomicMarkableReference.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AtomicMarkableReference.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
