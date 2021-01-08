---
title: LocalVariable
permalink: Java/LocalVariable
date: 2021-01-04
key: JavaJava.L.LocalVariable
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'interface java', 'Java 1.3']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.LocalVariable.description }}

## Sintaxis
~~~java
public interface LocalVariable extends Mirror, Comparable<LocalVariable>
~~~

## Métodos
* [equals()](/Java/LocalVariable/equals)
* [genericSignature()](/Java/LocalVariable/genericSignature)
* [hashCode()](/Java/LocalVariable/hashCode)
* [isArgument()](/Java/LocalVariable/isArgument)
* [isVisible()](/Java/LocalVariable/isVisible)
* [name()](/Java/LocalVariable/name)
* [signature()](/Java/LocalVariable/signature)
* [type()](/Java/LocalVariable/type)
* [typeName()](/Java/LocalVariable/typeName)

## Ejemplo
~~~java
{{ site.data.Java.L.LocalVariable.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LocalVariable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
