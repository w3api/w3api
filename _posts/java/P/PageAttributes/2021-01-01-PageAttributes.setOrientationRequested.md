---
title: PageAttributes.setOrientationRequested()
permalink: /Java/PageAttributes/setOrientationRequested/
date: 2021-01-11
key: Java.P.PageAttributes
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PageAttributes.metodos valor="setOrientationRequested" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setOrientationRequested(int orientationRequested)
public void setOrientationRequested(PageAttributes.OrientationRequestedType orientationRequested)
~~~

## Parámetros
* **PageAttributes.OrientationRequestedType orientationRequested**,  {% include w3api/param_description.html metodo=_dato parametro="PageAttributes.OrientationRequestedType orientationRequested" %}
* **int orientationRequested**,  {% include w3api/param_description.html metodo=_dato parametro="int orientationRequested" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PageAttributes](/Java/PageAttributes/)

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
