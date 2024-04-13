---
title: Container.applyComponentOrientation()
permalink: /Java/Container/applyComponentOrientation/
date: 2021-01-11
key: Java.C.Container
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Container.metodos valor="applyComponentOrientation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void applyComponentOrientation(ComponentOrientation o)
~~~

## Parámetros
* **ComponentOrientation o**,  {% include w3api/param_description.html metodo=_dato parametro="ComponentOrientation o" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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
