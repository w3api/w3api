---
title: MethodInvocationTree
permalink: Java/MethodInvocationTree
date: 2021-01-11
key: JavaJava.M.MethodInvocationTree
category: java
tags: ['java se', 'com.sun.source.tree', 'jdk.compiler', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MethodInvocationTree.description }}

## Sintaxis
~~~java
public interface MethodInvocationTree extends ExpressionTree
~~~

## Métodos
* [getArguments()](/Java/MethodInvocationTree/getArguments)
* [getMethodSelect()](/Java/MethodInvocationTree/getMethodSelect)
* [getTypeArguments()](/Java/MethodInvocationTree/getTypeArguments)

## Ejemplo
~~~java
{{ site.data.Java.M.MethodInvocationTree.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MethodInvocationTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
