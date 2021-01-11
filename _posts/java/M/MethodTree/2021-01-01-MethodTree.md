---
title: MethodTree
permalink: Java/MethodTree
date: 2021-01-11
key: JavaJava.M.MethodTree
category: java
tags: ['java se', 'com.sun.source.tree', 'jdk.compiler', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MethodTree.description }}

## Sintaxis
~~~java
public interface MethodTree extends Tree
~~~

## Métodos
* [getBody()](/Java/MethodTree/getBody)
* [getDefaultValue()](/Java/MethodTree/getDefaultValue)
* [getModifiers()](/Java/MethodTree/getModifiers)
* [getName()](/Java/MethodTree/getName)
* [getParameters()](/Java/MethodTree/getParameters)
* [getReceiverParameter()](/Java/MethodTree/getReceiverParameter)
* [getReturnType()](/Java/MethodTree/getReturnType)
* [getThrows()](/Java/MethodTree/getThrows)
* [getTypeParameters()](/Java/MethodTree/getTypeParameters)

## Ejemplo
~~~java
{{ site.data.Java.M.MethodTree.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MethodTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
