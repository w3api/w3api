---
title: CompletionService
permalink: Java/CompletionService
date: 2021-01-04
key: JavaJava.C.CompletionService
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CompletionService.description }}

## Sintaxis
~~~java
public interface CompletionService<V>
~~~

## Métodos
* [poll()](/Java/CompletionService/poll)
* [submit()](/Java/CompletionService/submit)
* [take()](/Java/CompletionService/take)

## Ejemplo
~~~java
{{ site.data.Java.C.CompletionService.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CompletionService.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
