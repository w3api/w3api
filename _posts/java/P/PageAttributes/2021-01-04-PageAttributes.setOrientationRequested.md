---
title: PageAttributes.setOrientationRequested()
permalink: Java/PageAttributes/setOrientationRequested
date: 2021-01-04
key: JavaJava.P.PageAttributes
category: java
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
* **PageAttributes.OrientationRequestedType orientationRequested**,  {% include w3api/param_description.html metodo=_data parametro="PageAttributes.OrientationRequestedType orientationRequested" %}
* **int orientationRequested**,  {% include w3api/param_description.html metodo=_data parametro="int orientationRequested" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PageAttributes](/Java/PageAttributes/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PageAttributes.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
