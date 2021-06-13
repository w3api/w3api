---
title: RecursiveTask
permalink: /Java/RecursiveTask/
date: 2021-01-11
key: Java.R.RecursiveTask
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'clase java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RecursiveTask.description }}

## Sintaxis
~~~java
public abstract class RecursiveTask<V> extends ForkJoinTask<V>
~~~

## Constructores
* [RecursiveTask()](/Java/RecursiveTask/RecursiveTask/)

## Métodos
* [compute()](/Java/RecursiveTask/compute)
* [exec()](/Java/RecursiveTask/exec)

## Ejemplo
~~~java
{{ site.data.Java.R.RecursiveTask.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RecursiveTask.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
