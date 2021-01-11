---
title: LambdaExpressionTree
permalink: Java/LambdaExpressionTree
date: 2021-01-11
key: JavaJava.L.LambdaExpressionTree
category: java
tags: ['java se', 'com.sun.source.tree', 'jdk.compiler', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.LambdaExpressionTree.description }}

## Sintaxis
~~~java
public interface LambdaExpressionTree extends ExpressionTree
~~~

## Métodos
* [getBody()](/Java/LambdaExpressionTree/getBody)
* [getBodyKind()](/Java/LambdaExpressionTree/getBodyKind)
* [getParameters()](/Java/LambdaExpressionTree/getParameters)

## Ejemplo
~~~java
{{ site.data.Java.L.LambdaExpressionTree.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LambdaExpressionTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
