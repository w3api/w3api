---
title: PrinterResolution.PrinterResolution()
permalink: /Java/PrinterResolution/PrinterResolution/
date: 2021-01-11
key: Java.P.PrinterResolution
category: java
tags: ['java se', 'javax.print.attribute.standard', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrinterResolution.constructores valor="PrinterResolution" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PrinterResolution(int crossFeedResolution, int feedResolution, int units)
~~~

## Parámetros
* **int feedResolution**,  {% include w3api/param_description.html metodo=_dato parametro="int feedResolution" %}
* **int units**,  {% include w3api/param_description.html metodo=_dato parametro="int units" %}
* **int crossFeedResolution**,  {% include w3api/param_description.html metodo=_dato parametro="int crossFeedResolution" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PrinterResolution](/Java/PrinterResolution/)

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
