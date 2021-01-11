---
title: RunnableFuture
permalink: Java/RunnableFuture
date: 2021-01-11
key: JavaJava.R.RunnableFuture
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RunnableFuture.description }}

## Sintaxis
~~~java
public interface RunnableFuture<V> extends Runnable, Future<V>
~~~

## Métodos
* [run()](/Java/RunnableFuture/run)

## Ejemplo
~~~java
{{ site.data.Java.R.RunnableFuture.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RunnableFuture.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
