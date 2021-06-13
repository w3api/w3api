---
title: ClassTree.getMembers()
permalink: /Java/ClassTree/getMembers/
date: 2021-01-11
key: Java.C.ClassTree
category: Java
tags: ['java se', 'com.sun.source.tree', 'jdk.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassTree.metodos valor="getMembers" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
List<? extends Tree> getMembers()
~~~

## Clase Padre
[ClassTree](/Java/ClassTree/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
