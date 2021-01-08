---
title: Throwable
permalink: Java/Throwable
date: 2021-01-04
key: JavaJava.T.Throwable
category: java
tags: ['java se', 'java.lang', 'java.base', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.Throwable.description }}

## Sintaxis
~~~java
public class Throwable extends Object implements Serializable
~~~

## Constructores
* [Throwable()](/Java/Throwable/Throwable/)

## Métodos
* [addSuppressed()](/Java/Throwable/addSuppressed)
* [fillInStackTrace()](/Java/Throwable/fillInStackTrace)
* [getCause()](/Java/Throwable/getCause)
* [getLocalizedMessage()](/Java/Throwable/getLocalizedMessage)
* [getMessage()](/Java/Throwable/getMessage)
* [getStackTrace()](/Java/Throwable/getStackTrace)
* [getSuppressed()](/Java/Throwable/getSuppressed)
* [initCause()](/Java/Throwable/initCause)
* [printStackTrace()](/Java/Throwable/printStackTrace)
* [setStackTrace()](/Java/Throwable/setStackTrace)
* [toString()](/Java/Throwable/toString)

## Ejemplo
~~~java
{{ site.data.Java.T.Throwable.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.Throwable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
