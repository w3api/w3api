---
title: LockSupport
permalink: Java/LockSupport
date: 2021-01-11
key: JavaJava.L.LockSupport
category: java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.LockSupport.description }}

## Sintaxis
~~~java
public class LockSupport extends Object
~~~

## Métodos
* [getBlocker()](/Java/LockSupport/getBlocker)
* [park()](/Java/LockSupport/park)
* [parkNanos()](/Java/LockSupport/parkNanos)
* [parkUntil()](/Java/LockSupport/parkUntil)
* [unpark()](/Java/LockSupport/unpark)

## Ejemplo
~~~java
{{ site.data.Java.L.LockSupport.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LockSupport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
