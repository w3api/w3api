---
title: RunnableScheduledFuture
permalink: Java/RunnableScheduledFuture
date: 2021-01-04
key: JavaJava.R.RunnableScheduledFuture
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RunnableScheduledFuture.description }}

## Sintaxis
~~~java
public interface RunnableScheduledFuture<V> extends RunnableFuture<V>, ScheduledFuture<V>
~~~

## Métodos
* [isPeriodic()](/Java/RunnableScheduledFuture/isPeriodic)

## Ejemplo
~~~java
{{ site.data.Java.R.RunnableScheduledFuture.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RunnableScheduledFuture.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
