---
title: PrinterLocation.PrinterLocation()
permalink: /Java/PrinterLocation/PrinterLocation/
date: 2021-01-11
key: Java.P.PrinterLocation
category: Java
tags: ['java se', 'javax.print.attribute.standard', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrinterLocation.constructores valor="PrinterLocation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PrinterLocation(String location, Locale locale)
~~~

## Parámetros
* **String location**,  {% include w3api/param_description.html metodo=_dato parametro="String location" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PrinterLocation](/Java/PrinterLocation/)

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
