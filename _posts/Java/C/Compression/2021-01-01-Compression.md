---
title: Compression
permalink: /Java/Compression/
date: 2021-01-11
key: Java.C.Compression
category: Java
tags: ['java se', 'javax.print.attribute.standard', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.Compression.description }}

## Sintaxis
~~~java
public class Compression extends EnumSyntax implements DocAttribute
~~~

## Constructores
* [Compression()](/Java/Compression/Compression/)

## Campos
* [COMPRESS](/Java/Compression/COMPRESS/)
* [DEFLATE](/Java/Compression/DEFLATE/)
* [GZIP](/Java/Compression/GZIP/)
* [NONE](/Java/Compression/NONE/)

## Métodos
* [getCategory()](/Java/Compression/getCategory/)
* [getEnumValueTable()](/Java/Compression/getEnumValueTable/)
* [getName()](/Java/Compression/getName/)
* [getStringTable()](/Java/Compression/getStringTable/)

## Ejemplo
~~~java
{{ site.data.Java.C.Compression.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.Compression.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
