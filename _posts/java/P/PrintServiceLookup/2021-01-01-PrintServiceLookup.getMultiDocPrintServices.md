---
title: PrintServiceLookup.getMultiDocPrintServices()
permalink: /Java/PrintServiceLookup/getMultiDocPrintServices/
date: 2021-01-11
key: Java.P.PrintServiceLookup
category: Java
tags: ['java se', 'javax.print', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrintServiceLookup.metodos valor="getMultiDocPrintServices" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract MultiDocPrintService[] getMultiDocPrintServices(DocFlavor[] flavors, AttributeSet attributes)
~~~

## Parámetros
* **DocFlavor[] flavors**,  {% include w3api/param_description.html metodo=_dato parametro="DocFlavor[] flavors" %}
* **AttributeSet attributes**,  {% include w3api/param_description.html metodo=_dato parametro="AttributeSet attributes" %}

## Clase Padre
[PrintServiceLookup](/Java/PrintServiceLookup/)

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
