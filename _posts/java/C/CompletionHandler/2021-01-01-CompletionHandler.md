---
title: CompletionHandler
permalink: Java/CompletionHandler
date: 2021-01-11
key: JavaJava.C.CompletionHandler
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'interface java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CompletionHandler.description }}

## Sintaxis
~~~java
public interface CompletionHandler<V,A>
~~~

## Métodos
* [completed()](/Java/CompletionHandler/completed)
* [failed()](/Java/CompletionHandler/failed)

## Ejemplo
~~~java
{{ site.data.Java.C.CompletionHandler.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CompletionHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
