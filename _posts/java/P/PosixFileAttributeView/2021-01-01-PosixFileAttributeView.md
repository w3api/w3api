---
title: PosixFileAttributeView
permalink: Java/PosixFileAttributeView
date: 2021-01-11
key: JavaJava.P.PosixFileAttributeView
category: java
tags: ['java se', 'java.nio.file.attribute', 'java.base', 'interface java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PosixFileAttributeView.description }}

## Sintaxis
~~~java
public interface PosixFileAttributeView extends BasicFileAttributeView, FileOwnerAttributeView
~~~

## Métodos
* [name()](/Java/PosixFileAttributeView/name)
* [readAttributes()](/Java/PosixFileAttributeView/readAttributes)
* [setGroup()](/Java/PosixFileAttributeView/setGroup)
* [setPermissions()](/Java/PosixFileAttributeView/setPermissions)

## Ejemplo
~~~java
{{ site.data.Java.P.PosixFileAttributeView.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PosixFileAttributeView.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
