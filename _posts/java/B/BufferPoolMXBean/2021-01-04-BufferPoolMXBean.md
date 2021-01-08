---
title: BufferPoolMXBean
permalink: Java/BufferPoolMXBean
date: 2021-01-04
key: JavaJava.B.BufferPoolMXBean
category: java
tags: ['java se', 'java.lang.management', 'java.management', 'interface java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.B.BufferPoolMXBean.description }}

## Sintaxis
~~~java
public interface BufferPoolMXBean extends PlatformManagedObject
~~~

## Métodos
* [getCount()](/Java/BufferPoolMXBean/getCount)
* [getMemoryUsed()](/Java/BufferPoolMXBean/getMemoryUsed)
* [getName()](/Java/BufferPoolMXBean/getName)
* [getTotalCapacity()](/Java/BufferPoolMXBean/getTotalCapacity)

## Ejemplo
~~~java
{{ site.data.Java.B.BufferPoolMXBean.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BufferPoolMXBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
