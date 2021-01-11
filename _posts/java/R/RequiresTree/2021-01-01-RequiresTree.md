---
title: RequiresTree
permalink: Java/RequiresTree
date: 2021-01-11
key: JavaJava.R.RequiresTree
category: java
tags: ['java se', 'com.sun.source.tree', 'jdk.compiler', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RequiresTree.description }}

## Sintaxis
~~~java
public interface RequiresTree extends DirectiveTree
~~~

## Métodos
* [getModuleName()](/Java/RequiresTree/getModuleName)
* [isStatic()](/Java/RequiresTree/isStatic)
* [isTransitive()](/Java/RequiresTree/isTransitive)

## Ejemplo
~~~java
{{ site.data.Java.R.RequiresTree.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RequiresTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
