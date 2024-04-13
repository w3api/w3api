---
title: JdiExecutionControl
permalink: /Java/JdiExecutionControl/
date: 2021-01-11
key: Java.J.JdiExecutionControl
category: Java
tags: ['java se', 'jdk.jshell.execution', 'jdk.jshell', 'clase java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.J.JdiExecutionControl.description }}

## Sintaxis
~~~java
public abstract class JdiExecutionControl extends StreamingExecutionControl implements ExecutionControl
~~~

## Constructores
* [JdiExecutionControl()](/Java/JdiExecutionControl/JdiExecutionControl/)

## Métodos
* [redefine()](/Java/JdiExecutionControl/redefine)
* [referenceType()](/Java/JdiExecutionControl/referenceType)
* [vm()](/Java/JdiExecutionControl/vm)

## Ejemplo
~~~java
{{ site.data.Java.J.JdiExecutionControl.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.J.JdiExecutionControl.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
