---
title: PosixFileAttributes
permalink: Java/PosixFileAttributes
date: 2021-01-04
key: JavaJava.P.PosixFileAttributes
category: java
tags: ['java se', 'java.nio.file.attribute', 'java.base', 'interface java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PosixFileAttributes.description }}

## Sintaxis
~~~java
public interface PosixFileAttributes extends BasicFileAttributes
~~~

## Métodos
* [group()](/Java/PosixFileAttributes/group)
* [owner()](/Java/PosixFileAttributes/owner)
* [permissions()](/Java/PosixFileAttributes/permissions)

## Ejemplo
~~~java
{{ site.data.Java.P.PosixFileAttributes.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PosixFileAttributes.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
