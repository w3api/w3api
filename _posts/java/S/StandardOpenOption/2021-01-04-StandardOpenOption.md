---
title: StandardOpenOption
permalink: Java/StandardOpenOption
date: 2021-01-04
key: JavaJava.S.StandardOpenOption
category: java
tags: ['java se', 'java.nio.file', 'java.base', 'enumerado java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.StandardOpenOption.description }}

## Sintaxis
~~~java
public enum StandardOpenOption extends Enum<StandardOpenOption> implements OpenOption
~~~

## Enumerados
* [APPEND](/Java/StandardOpenOption/APPEND)
* [CREATE](/Java/StandardOpenOption/CREATE)
* [CREATE_NEW](/Java/StandardOpenOption/CREATE_NEW)
* [DELETE_ON_CLOSE](/Java/StandardOpenOption/DELETE_ON_CLOSE)
* [DSYNC](/Java/StandardOpenOption/DSYNC)
* [READ](/Java/StandardOpenOption/READ)
* [SPARSE](/Java/StandardOpenOption/SPARSE)
* [SYNC](/Java/StandardOpenOption/SYNC)
* [TRUNCATE_EXISTING](/Java/StandardOpenOption/TRUNCATE_EXISTING)
* [WRITE](/Java/StandardOpenOption/WRITE)

## Métodos
* [valueOf()](/Java/StandardOpenOption/valueOf)
* [values()](/Java/StandardOpenOption/values)

## Ejemplo
~~~java
{{ site.data.Java.S.StandardOpenOption.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StandardOpenOption.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
