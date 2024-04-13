---
title: ImportTree
permalink: /Java/ImportTree/
date: 2021-01-11
key: Java.I.ImportTree
category: Java
tags: ['java se', 'com.sun.source.tree', 'jdk.compiler', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.ImportTree.description }}

## Sintaxis
~~~java
public interface ImportTree extends Tree
~~~

## Métodos
* [getQualifiedIdentifier()](/Java/ImportTree/getQualifiedIdentifier)
* [isStatic()](/Java/ImportTree/isStatic)

## Ejemplo
~~~java
{{ site.data.Java.I.ImportTree.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.ImportTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
