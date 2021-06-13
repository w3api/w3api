---
title: PageAttributes.setPrinterResolution()
permalink: /Java/PageAttributes/setPrinterResolution/
date: 2021-01-11
key: Java.P.PageAttributes
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PageAttributes.metodos valor="setPrinterResolution" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setPrinterResolution(int printerResolution)
public void setPrinterResolution(int[] printerResolution)
~~~

## Parámetros
* **int[] printerResolution**,  {% include w3api/param_description.html metodo=_dato parametro="int[] printerResolution" %}
* **int printerResolution**,  {% include w3api/param_description.html metodo=_dato parametro="int printerResolution" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
