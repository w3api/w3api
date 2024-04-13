---
title: PageOrientation
permalink: /Java/PageOrientation/
date: 2021-01-11
key: Java.P.PageOrientation
category: Java
tags: ['java se', 'javafx.print', 'javafx.graphics', 'enumerado java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PageOrientation.description }}

## Sintaxis
~~~java
public enum PageOrientation extends Enum<PageOrientation>
~~~

## Enumerados
* [LANDSCAPE](/Java/PageOrientation/LANDSCAPE/)
* [PORTRAIT](/Java/PageOrientation/PORTRAIT/)
* [REVERSE_LANDSCAPE](/Java/PageOrientation/REVERSE_LANDSCAPE/)
* [REVERSE_PORTRAIT](/Java/PageOrientation/REVERSE_PORTRAIT/)

## Métodos
* [valueOf()](/Java/PageOrientation/valueOf/)
* [values()](/Java/PageOrientation/values/)

## Ejemplo
~~~java
{{ site.data.Java.P.PageOrientation.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.P.PageOrientation.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
