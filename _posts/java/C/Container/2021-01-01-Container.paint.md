---
title: Container.paint()
permalink: /Java/Container/paint/
date: 2021-01-11
key: Java.C.Container
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Container.metodos valor="paint" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void paint(Graphics g)
~~~

## Parámetros
* **Graphics g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics g" %}

## Clase Padre
[Container](/Java/Container/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
