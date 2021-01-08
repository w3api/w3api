---
title: ExportsTree
permalink: Java/ExportsTree
date: 2021-01-04
key: JavaJava.E.ExportsTree
category: java
tags: ['java se', 'com.sun.source.tree', 'jdk.compiler', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.ExportsTree.description }}

## Sintaxis
~~~java
public interface ExportsTree extends DirectiveTree
~~~

## Métodos
* [getModuleNames()](/Java/ExportsTree/getModuleNames)
* [getPackageName()](/Java/ExportsTree/getPackageName)

## Ejemplo
~~~java
{{ site.data.Java.E.ExportsTree.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ExportsTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
