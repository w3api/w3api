---
title: CyclicBarrier
permalink: Java/CyclicBarrier
date: 2021-01-11
key: JavaJava.C.CyclicBarrier
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CyclicBarrier.description }}

## Sintaxis
~~~java
public class CyclicBarrier extends Object
~~~

## Constructores
* [CyclicBarrier()](/Java/CyclicBarrier/CyclicBarrier/)

## Métodos
* [await()](/Java/CyclicBarrier/await)
* [getNumberWaiting()](/Java/CyclicBarrier/getNumberWaiting)
* [getParties()](/Java/CyclicBarrier/getParties)
* [isBroken()](/Java/CyclicBarrier/isBroken)
* [reset()](/Java/CyclicBarrier/reset)

## Ejemplo
~~~java
{{ site.data.Java.C.CyclicBarrier.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CyclicBarrier.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
