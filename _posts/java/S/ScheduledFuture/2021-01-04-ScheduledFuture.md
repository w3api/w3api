---
title: ScheduledFuture
permalink: Java/ScheduledFuture
date: 2021-01-04
key: JavaJava.S.ScheduledFuture
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.ScheduledFuture.description }}

## Sintaxis
~~~java
public interface ScheduledFuture<V> extends Delayed, Future<V>
~~~

## Ejemplo
~~~java
{{ site.data.Java.S.ScheduledFuture.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ScheduledFuture.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
