---
title: PropertyTree
permalink: /Java/PropertyTree/
date: 2021-01-11
key: Java.P.PropertyTree
category: Java
tags: ['java se', 'jdk.nashorn.api.tree', 'jdk.scripting.nashorn', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PropertyTree.description }}

## Sintaxis
~~~java
public interface PropertyTree extends Tree
~~~

## Métodos
* [getGetter()](/Java/PropertyTree/getGetter)
* [getKey()](/Java/PropertyTree/getKey)
* [getSetter()](/Java/PropertyTree/getSetter)
* [getValue()](/Java/PropertyTree/getValue)
* [isComputed()](/Java/PropertyTree/isComputed)
* [isStatic()](/Java/PropertyTree/isStatic)

## Ejemplo
~~~java
{{ site.data.Java.P.PropertyTree.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PropertyTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
