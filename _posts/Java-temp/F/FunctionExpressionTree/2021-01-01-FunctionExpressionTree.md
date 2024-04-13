---
title: FunctionExpressionTree
permalink: /Java/FunctionExpressionTree/
date: 2021-01-11
key: Java.F.FunctionExpressionTree
category: Java
tags: ['java se', 'jdk.nashorn.api.tree', 'jdk.scripting.nashorn', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.F.FunctionExpressionTree.description }}

## Sintaxis
~~~java
public interface FunctionExpressionTree extends ExpressionTree
~~~

## Métodos
* [getBody()](/Java/FunctionExpressionTree/getBody)
* [getName()](/Java/FunctionExpressionTree/getName)
* [getParameters()](/Java/FunctionExpressionTree/getParameters)
* [isArrow()](/Java/FunctionExpressionTree/isArrow)
* [isGenerator()](/Java/FunctionExpressionTree/isGenerator)
* [isStrict()](/Java/FunctionExpressionTree/isStrict)

## Ejemplo
~~~java
{{ site.data.Java.F.FunctionExpressionTree.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FunctionExpressionTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
