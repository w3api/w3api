---
title: PageFormat.setOrientation()
permalink: /Java/PageFormat/setOrientation/
date: 2021-01-11
key: Java.P.PageFormat
category: Java
tags: ['java se', 'java.awt.print', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PageFormat.metodos valor="setOrientation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setOrientation(int orientation) throws IllegalArgumentException
~~~

## Parámetros
* **int orientation**,  {% include w3api/param_description.html metodo=_dato parametro="int orientation" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PageFormat](/Java/PageFormat/)

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
