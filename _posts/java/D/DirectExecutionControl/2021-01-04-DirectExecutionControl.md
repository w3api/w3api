---
title: DirectExecutionControl
permalink: Java/DirectExecutionControl
date: 2021-01-04
key: JavaJava.D.DirectExecutionControl
category: java
tags: ['java se', 'jdk.jshell.execution', 'jdk.jshell', 'clase java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DirectExecutionControl.description }}

## Sintaxis
~~~java
public class DirectExecutionControl extends Object implements ExecutionControl
~~~

## Constructores
* [DirectExecutionControl()](/Java/DirectExecutionControl/DirectExecutionControl/)

## Métodos
* [classesRedefined()](/Java/DirectExecutionControl/classesRedefined)
* [clientCodeEnter()](/Java/DirectExecutionControl/clientCodeEnter)
* [clientCodeLeave()](/Java/DirectExecutionControl/clientCodeLeave)
* [findClass()](/Java/DirectExecutionControl/findClass)
* [invoke()](/Java/DirectExecutionControl/invoke)
* [stop()](/Java/DirectExecutionControl/stop)
* [throwConvertedInvocationException()](/Java/DirectExecutionControl/throwConvertedInvocationException)
* [throwConvertedOtherException()](/Java/DirectExecutionControl/throwConvertedOtherException)
* [valueString()](/Java/DirectExecutionControl/valueString)

## Ejemplo
~~~java
{{ site.data.Java.D.DirectExecutionControl.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DirectExecutionControl.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
