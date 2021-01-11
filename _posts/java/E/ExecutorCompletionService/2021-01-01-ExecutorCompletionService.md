---
title: ExecutorCompletionService
permalink: Java/ExecutorCompletionService
date: 2021-01-11
key: JavaJava.E.ExecutorCompletionService
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.ExecutorCompletionService.description }}

## Sintaxis
~~~java
public class ExecutorCompletionService<V> extends Object implements CompletionService<V>
~~~

## Constructores
* [ExecutorCompletionService()](/Java/ExecutorCompletionService/ExecutorCompletionService/)

## Métodos
* [submit()](/Java/ExecutorCompletionService/submit)

## Ejemplo
~~~java
{{ site.data.Java.E.ExecutorCompletionService.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ExecutorCompletionService.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
