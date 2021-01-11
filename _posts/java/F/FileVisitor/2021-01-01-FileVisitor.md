---
title: FileVisitor
permalink: Java/FileVisitor
date: 2021-01-11
key: JavaJava.F.FileVisitor
category: java
tags: ['java se', 'java.nio.file', 'java.base', 'interface java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.F.FileVisitor.description }}

## Sintaxis
~~~java
public interface FileVisitor<T>
~~~

## Métodos
* [postVisitDirectory()](/Java/FileVisitor/postVisitDirectory)
* [preVisitDirectory()](/Java/FileVisitor/preVisitDirectory)
* [visitFile()](/Java/FileVisitor/visitFile)
* [visitFileFailed()](/Java/FileVisitor/visitFileFailed)

## Ejemplo
~~~java
{{ site.data.Java.F.FileVisitor.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FileVisitor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
