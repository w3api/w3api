---
title: FileVisitResult
permalink: Java/FileVisitResult
date: 2021-01-11
key: JavaJava.F.FileVisitResult
category: java
tags: ['java se', 'java.nio.file', 'java.base', 'enumerado java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.F.FileVisitResult.description }}

## Sintaxis
~~~java
public enum FileVisitResult extends Enum<FileVisitResult>
~~~

## Enumerados
* [CONTINUE](/Java/FileVisitResult/CONTINUE)
* [SKIP_SIBLINGS](/Java/FileVisitResult/SKIP_SIBLINGS)
* [SKIP_SUBTREE](/Java/FileVisitResult/SKIP_SUBTREE)
* [TERMINATE](/Java/FileVisitResult/TERMINATE)

## Métodos
* [valueOf()](/Java/FileVisitResult/valueOf)
* [values()](/Java/FileVisitResult/values)

## Ejemplo
~~~java
{{ site.data.Java.F.FileVisitResult.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FileVisitResult.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
