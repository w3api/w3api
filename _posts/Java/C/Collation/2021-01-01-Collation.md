---
title: Collation
permalink: /Java/Collation/
date: 2021-01-11
key: Java.C.Collation
category: Java
tags: ['java se', 'javafx.print', 'javafx.graphics', 'enumerado java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.Collation.description }}

## Sintaxis
~~~java
public enum Collation extends Enum<Collation>
~~~

## Enumerados
* [COLLATED](/Java/Collation/COLLATED/)
* [UNCOLLATED](/Java/Collation/UNCOLLATED/)

## Métodos
* [valueOf()](/Java/Collation/valueOf/)
* [values()](/Java/Collation/values/)

## Ejemplo
~~~java
{{ site.data.Java.C.Collation.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.Collation.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
