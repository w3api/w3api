---
title: NewClassTree
permalink: /Java/NewClassTree/
date: 2021-01-11
key: Java.N.NewClassTree
category: Java
tags: ['java se', 'com.sun.source.tree', 'jdk.compiler', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.N.NewClassTree.description }}

## Sintaxis
~~~java
public interface NewClassTree extends ExpressionTree
~~~

## Métodos
* [getArguments()](/Java/NewClassTree/getArguments)
* [getClassBody()](/Java/NewClassTree/getClassBody)
* [getEnclosingExpression()](/Java/NewClassTree/getEnclosingExpression)
* [getIdentifier()](/Java/NewClassTree/getIdentifier)
* [getTypeArguments()](/Java/NewClassTree/getTypeArguments)

## Ejemplo
~~~java
{{ site.data.Java.N.NewClassTree.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NewClassTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
