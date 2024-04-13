---
title: Closeable
permalink: /Java/Closeable/
date: 2021-01-11
key: Java.C.Closeable
category: Java
tags: ['java se', 'java.io', 'java.base', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.Closeable.description }}

## Sintaxis
~~~java
public interface Closeable extends AutoCloseable
~~~

## Métodos
* [close()](/Java/Closeable/close)

## Ejemplo
~~~java
{{ site.data.Java.C.Closeable.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.Closeable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
