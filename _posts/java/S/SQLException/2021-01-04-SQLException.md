---
title: SQLException
permalink: Java/SQLException
date: 2021-01-04
key: JavaJava.S.SQLException
category: java
tags: ['java se', 'java.sql', 'java.sql', 'clase java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SQLException.description }}

## Sintaxis
~~~java
public class SQLException extends Exception implements Iterable<Throwable>
~~~

## Constructores
* [SQLException()](/Java/SQLException/SQLException/)

## Métodos
* [getErrorCode()](/Java/SQLException/getErrorCode)
* [getNextException()](/Java/SQLException/getNextException)
* [getSQLState()](/Java/SQLException/getSQLState)
* [iterator()](/Java/SQLException/iterator)
* [setNextException()](/Java/SQLException/setNextException)

## Ejemplo
~~~java
{{ site.data.Java.S.SQLException.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SQLException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
