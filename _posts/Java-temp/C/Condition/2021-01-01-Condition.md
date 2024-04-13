---
title: Condition
permalink: /Java/Condition/
date: 2021-01-11
key: Java.C.Condition
category: Java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.Condition.description }}

## Sintaxis
~~~java
public interface Condition
~~~

## Métodos
* [await()](/Java/Condition/await)
* [awaitNanos()](/Java/Condition/awaitNanos)
* [awaitUninterruptibly()](/Java/Condition/awaitUninterruptibly)
* [awaitUntil()](/Java/Condition/awaitUntil)
* [signal()](/Java/Condition/signal)
* [signalAll()](/Java/Condition/signalAll)

## Ejemplo
~~~java
{{ site.data.Java.C.Condition.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.Condition.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
