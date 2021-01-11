---
title: TypeCastTree
permalink: Java/TypeCastTree
date: 2021-01-11
key: JavaJava.T.TypeCastTree
category: java
tags: ['java se', 'com.sun.source.tree', 'jdk.compiler', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.TypeCastTree.description }}

## Sintaxis
~~~java
public interface TypeCastTree extends ExpressionTree
~~~

## Métodos
* [getExpression()](/Java/TypeCastTree/getExpression)
* [getType()](/Java/TypeCastTree/getType)

## Ejemplo
~~~java
{{ site.data.Java.T.TypeCastTree.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TypeCastTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
