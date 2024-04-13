---
title: DocTreePath
permalink: /Java/DocTreePath/
date: 2021-01-11
key: Java.D.DocTreePath
category: Java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'clase java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DocTreePath.description }}

## Sintaxis
~~~java
public class DocTreePath extends Object implements Iterable<DocTree>
~~~

## Constructores
* [DocTreePath()](/Java/DocTreePath/DocTreePath/)

## Métodos
* [getDocComment()](/Java/DocTreePath/getDocComment/)
* [getLeaf()](/Java/DocTreePath/getLeaf/)
* [getParentPath()](/Java/DocTreePath/getParentPath/)
* [getPath()](/Java/DocTreePath/getPath/)
* [getTreePath()](/Java/DocTreePath/getTreePath/)

## Ejemplo
~~~java
{{ site.data.Java.D.DocTreePath.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DocTreePath.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
