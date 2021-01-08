---
title: StackFrame
permalink: Java/StackFrame
date: 2021-01-04
key: JavaJava.S.StackFrame
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.StackFrame.description }}

## Sintaxis
~~~java
public interface StackFrame extends Mirror, Locatable
~~~

## Métodos
* [getArgumentValues()](/Java/StackFrame/getArgumentValues)
* [getValue()](/Java/StackFrame/getValue)
* [getValues()](/Java/StackFrame/getValues)
* [location()](/Java/StackFrame/location)
* [setValue()](/Java/StackFrame/setValue)
* [thisObject()](/Java/StackFrame/thisObject)
* [thread()](/Java/StackFrame/thread)
* [visibleVariableByName()](/Java/StackFrame/visibleVariableByName)
* [visibleVariables()](/Java/StackFrame/visibleVariables)

## Ejemplo
~~~java
{{ site.data.Java.S.StackFrame.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StackFrame.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
