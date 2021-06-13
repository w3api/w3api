---
title: ParamTree
permalink: /Java/ParamTree/
date: 2021-01-11
key: Java.P.ParamTree
category: java
tags: ['java se', 'com.sun.source.doctree', 'jdk.compiler', 'interface java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.ParamTree.description }}

## Sintaxis
~~~java
public interface ParamTree extends BlockTagTree
~~~

## Métodos
* [getDescription()](/Java/ParamTree/getDescription)
* [getName()](/Java/ParamTree/getName)
* [isTypeParameter()](/Java/ParamTree/isTypeParameter)

## Ejemplo
~~~java
{{ site.data.Java.P.ParamTree.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.ParamTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
