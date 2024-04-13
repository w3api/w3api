---
title: SimpleFileVisitor
permalink: /Java/SimpleFileVisitor/
date: 2021-01-11
key: Java.S.SimpleFileVisitor
category: Java
tags: ['java se', 'java.nio.file', 'java.base', 'clase java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SimpleFileVisitor.description }}

## Sintaxis
~~~java
public class SimpleFileVisitor<T> extends Object implements FileVisitor<T>
~~~

## Constructores
* [SimpleFileVisitor()](/Java/SimpleFileVisitor/SimpleFileVisitor/)

## Métodos
* [postVisitDirectory()](/Java/SimpleFileVisitor/postVisitDirectory)
* [preVisitDirectory()](/Java/SimpleFileVisitor/preVisitDirectory)
* [visitFile()](/Java/SimpleFileVisitor/visitFile)
* [visitFileFailed()](/Java/SimpleFileVisitor/visitFileFailed)

## Ejemplo
~~~java
{{ site.data.Java.S.SimpleFileVisitor.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SimpleFileVisitor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
