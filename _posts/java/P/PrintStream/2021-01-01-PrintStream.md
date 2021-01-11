---
title: PrintStream
permalink: Java/PrintStream
date: 2021-01-11
key: JavaJava.P.PrintStream
category: java
tags: ['java se', 'java.io', 'java.base', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PrintStream.description }}

## Sintaxis
~~~java
public class PrintStream extends FilterOutputStream implements Appendable, Closeable
~~~

## Constructores
* [PrintStream()](/Java/PrintStream/PrintStream/)

## Métodos
* [append()](/Java/PrintStream/append)
* [checkError()](/Java/PrintStream/checkError)
* [clearError()](/Java/PrintStream/clearError)
* [close()](/Java/PrintStream/close)
* [flush()](/Java/PrintStream/flush)
* [format()](/Java/PrintStream/format)
* [print()](/Java/PrintStream/print)
* [printf()](/Java/PrintStream/printf)
* [println()](/Java/PrintStream/println)
* [setError()](/Java/PrintStream/setError)
* [write()](/Java/PrintStream/write)

## Ejemplo
~~~java
{{ site.data.Java.P.PrintStream.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PrintStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
