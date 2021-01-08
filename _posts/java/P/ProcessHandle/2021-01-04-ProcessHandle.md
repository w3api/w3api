---
title: ProcessHandle
permalink: Java/ProcessHandle
date: 2021-01-04
key: JavaJava.P.ProcessHandle
category: java
tags: ['java se', 'java.lang', 'java.base', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.ProcessHandle.description }}

## Sintaxis
~~~java
public interface ProcessHandle extends Comparable<ProcessHandle>
~~~

## Métodos
* [allProcesses()](/Java/ProcessHandle/allProcesses)
* [children()](/Java/ProcessHandle/children)
* [compareTo()](/Java/ProcessHandle/compareTo)
* [current()](/Java/ProcessHandle/current)
* [descendants()](/Java/ProcessHandle/descendants)
* [destroy()](/Java/ProcessHandle/destroy)
* [destroyForcibly()](/Java/ProcessHandle/destroyForcibly)
* [equals()](/Java/ProcessHandle/equals)
* [hashCode()](/Java/ProcessHandle/hashCode)
* [info()](/Java/ProcessHandle/info)
* [isAlive()](/Java/ProcessHandle/isAlive)
* [of()](/Java/ProcessHandle/of)
* [onExit()](/Java/ProcessHandle/onExit)
* [parent()](/Java/ProcessHandle/parent)
* [pid()](/Java/ProcessHandle/pid)
* [supportsNormalTermination()](/Java/ProcessHandle/supportsNormalTermination)

## Ejemplo
~~~java
{{ site.data.Java.P.ProcessHandle.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.ProcessHandle.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
