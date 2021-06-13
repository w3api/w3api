---
title: ClassTree
permalink: /Java/ClassTree/
date: 2021-01-11
key: Java.C.ClassTree
category: Java
tags: ['java se', 'com.sun.source.tree', 'jdk.compiler', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ClassTree.description }}

## Sintaxis
~~~java
public interface ClassTree extends StatementTree
~~~

## Métodos
* [getExtendsClause()](/Java/ClassTree/getExtendsClause)
* [getImplementsClause()](/Java/ClassTree/getImplementsClause)
* [getMembers()](/Java/ClassTree/getMembers)
* [getModifiers()](/Java/ClassTree/getModifiers)
* [getSimpleName()](/Java/ClassTree/getSimpleName)
* [getTypeParameters()](/Java/ClassTree/getTypeParameters)

## Ejemplo
~~~java
{{ site.data.Java.C.ClassTree.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ClassTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
