---
title: DirectoryStream
permalink: Java/DirectoryStream
date: 2021-01-11
key: JavaJava.D.DirectoryStream
category: java
tags: ['java se', 'java.nio.file', 'java.base', 'interface java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DirectoryStream.description }}

## Sintaxis
~~~java
public interface DirectoryStream<T> extends Closeable, Iterable<T>
~~~

## Métodos
* [iterator()](/Java/DirectoryStream/iterator)

## Ejemplo
~~~java
{{ site.data.Java.D.DirectoryStream.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DirectoryStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
