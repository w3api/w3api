---
title: ExecutionControl
permalink: Java/ExecutionControl
date: 2021-01-11
key: JavaJava.E.ExecutionControl
category: java
tags: ['java se', 'jdk.jshell.spi', 'jdk.jshell', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.ExecutionControl.description }}

## Sintaxis
~~~java
public interface ExecutionControl extends AutoCloseable
~~~

## Métodos
* [addToClasspath()](/Java/ExecutionControl/addToClasspath)
* [close()](/Java/ExecutionControl/close)
* [extensionCommand()](/Java/ExecutionControl/extensionCommand)
* [generate()](/Java/ExecutionControl/generate)
* [invoke()](/Java/ExecutionControl/invoke)
* [load()](/Java/ExecutionControl/load)
* [redefine()](/Java/ExecutionControl/redefine)
* [stop()](/Java/ExecutionControl/stop)
* [varValue()](/Java/ExecutionControl/varValue)

## Ejemplo
~~~java
{{ site.data.Java.E.ExecutionControl.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ExecutionControl.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
