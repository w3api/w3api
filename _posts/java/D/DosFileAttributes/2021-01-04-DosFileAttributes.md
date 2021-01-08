---
title: DosFileAttributes
permalink: Java/DosFileAttributes
date: 2021-01-04
key: JavaJava.D.DosFileAttributes
category: java
tags: ['java se', 'java.nio.file.attribute', 'java.base', 'interface java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DosFileAttributes.description }}

## Sintaxis
~~~java
public interface DosFileAttributes extends BasicFileAttributes
~~~

## Métodos
* [isArchive()](/Java/DosFileAttributes/isArchive)
* [isHidden()](/Java/DosFileAttributes/isHidden)
* [isReadOnly()](/Java/DosFileAttributes/isReadOnly)
* [isSystem()](/Java/DosFileAttributes/isSystem)

## Ejemplo
~~~java
{{ site.data.Java.D.DosFileAttributes.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DosFileAttributes.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
