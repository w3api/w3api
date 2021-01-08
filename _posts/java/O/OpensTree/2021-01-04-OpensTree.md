---
title: OpensTree
permalink: Java/OpensTree
date: 2021-01-04
key: JavaJava.O.OpensTree
category: java
tags: ['java se', 'com.sun.source.tree', 'jdk.compiler', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.O.OpensTree.description }}

## Sintaxis
~~~java
public interface OpensTree extends DirectiveTree
~~~

## Métodos
* [getModuleNames()](/Java/OpensTree/getModuleNames)
* [getPackageName()](/Java/OpensTree/getPackageName)

## Ejemplo
~~~java
{{ site.data.Java.O.OpensTree.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.OpensTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
