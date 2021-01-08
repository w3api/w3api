---
title: WatchEvent
permalink: Java/WatchEvent
date: 2021-01-04
key: JavaJava.W.WatchEvent
category: java
tags: ['java se', 'java.nio.file', 'java.base', 'interface java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.W.WatchEvent.description }}

## Sintaxis
~~~java
public interface WatchEvent<T>
~~~

## Métodos
* [context()](/Java/WatchEvent/context)
* [count()](/Java/WatchEvent/count)
* [kind()](/Java/WatchEvent/kind)

## Ejemplo
~~~java
{{ site.data.Java.W.WatchEvent.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WatchEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
