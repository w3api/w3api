---
title: ModuleReader
permalink: /Java/ModuleReader/
date: 2021-01-11
key: Java.M.ModuleReader
category: Java
tags: ['java se', 'java.lang.module', 'java.base', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.ModuleReader.description }}

## Sintaxis
~~~java
public interface ModuleReader extends Closeable
~~~

## Métodos
* [close()](/Java/ModuleReader/close)
* [find()](/Java/ModuleReader/find)
* [list()](/Java/ModuleReader/list)
* [open()](/Java/ModuleReader/open)
* [read()](/Java/ModuleReader/read)
* [release()](/Java/ModuleReader/release)

## Ejemplo
~~~java
{{ site.data.Java.M.ModuleReader.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.ModuleReader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
