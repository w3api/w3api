---
title: EnhancedForLoopTree
permalink: Java/EnhancedForLoopTree
date: 2021-01-11
key: JavaJava.E.EnhancedForLoopTree
category: java
tags: ['java se', 'com.sun.source.tree', 'jdk.compiler', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.EnhancedForLoopTree.description }}

## Sintaxis
~~~java
public interface EnhancedForLoopTree extends StatementTree
~~~

## Métodos
* [getExpression()](/Java/EnhancedForLoopTree/getExpression)
* [getStatement()](/Java/EnhancedForLoopTree/getStatement)
* [getVariable()](/Java/EnhancedForLoopTree/getVariable)

## Ejemplo
~~~java
{{ site.data.Java.E.EnhancedForLoopTree.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.EnhancedForLoopTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
