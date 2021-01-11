---
title: PermissionCollection
permalink: Java/PermissionCollection
date: 2021-01-11
key: JavaJava.P.PermissionCollection
category: java
tags: ['java se', 'java.security', 'java.base', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PermissionCollection.description }}

## Sintaxis
~~~java
public abstract class PermissionCollection extends Object implements Serializable
~~~

## Constructores
* [PermissionCollection()](/Java/PermissionCollection/PermissionCollection/)

## Métodos
* [add()](/Java/PermissionCollection/add)
* [elements()](/Java/PermissionCollection/elements)
* [elementsAsStream()](/Java/PermissionCollection/elementsAsStream)
* [implies()](/Java/PermissionCollection/implies)
* [isReadOnly()](/Java/PermissionCollection/isReadOnly)
* [setReadOnly()](/Java/PermissionCollection/setReadOnly)
* [toString()](/Java/PermissionCollection/toString)

## Ejemplo
~~~java
{{ site.data.Java.P.PermissionCollection.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PermissionCollection.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
