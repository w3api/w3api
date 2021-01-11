---
title: ForInLoopTree
permalink: Java/ForInLoopTree
date: 2021-01-11
key: JavaJava.F.ForInLoopTree
category: java
tags: ['java se', 'jdk.nashorn.api.tree', 'jdk.scripting.nashorn', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.F.ForInLoopTree.description }}

## Sintaxis
~~~java
public interface ForInLoopTree extends LoopTree
~~~

## Métodos
* [getExpression()](/Java/ForInLoopTree/getExpression)
* [getStatement()](/Java/ForInLoopTree/getStatement)
* [getVariable()](/Java/ForInLoopTree/getVariable)
* [isForEach()](/Java/ForInLoopTree/isForEach)

## Ejemplo
~~~java
{{ site.data.Java.F.ForInLoopTree.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.ForInLoopTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
