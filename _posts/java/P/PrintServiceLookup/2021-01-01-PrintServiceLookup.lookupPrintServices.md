---
title: PrintServiceLookup.lookupPrintServices()
permalink: /Java/PrintServiceLookup/lookupPrintServices/
date: 2021-01-11
key: Java.P.PrintServiceLookup
category: java
tags: ['java se', 'javax.print', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrintServiceLookup.metodos valor="lookupPrintServices" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static PrintService[] lookupPrintServices(DocFlavor flavor, AttributeSet attributes)
~~~

## Parámetros
* **DocFlavor flavor**,  {% include w3api/param_description.html metodo=_dato parametro="DocFlavor flavor" %}
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
