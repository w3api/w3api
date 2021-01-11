---
title: FunctionCallTree
permalink: Java/FunctionCallTree
date: 2021-01-11
key: JavaJava.F.FunctionCallTree
category: java
tags: ['java se', 'jdk.nashorn.api.tree', 'jdk.scripting.nashorn', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.F.FunctionCallTree.description }}

## Sintaxis
~~~java
public interface FunctionCallTree extends ExpressionTree
~~~

## Métodos
* [getArguments()](/Java/FunctionCallTree/getArguments)
* [getFunctionSelect()](/Java/FunctionCallTree/getFunctionSelect)

## Ejemplo
~~~java
{{ site.data.Java.F.FunctionCallTree.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FunctionCallTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
