---
title: PrintServiceLookup.lookupMultiDocPrintServices()
permalink: Java/PrintServiceLookup/lookupMultiDocPrintServices
date: 2021-01-04
key: JavaJava.P.PrintServiceLookup
category: java
tags: ['java se', 'javax.print', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrintServiceLookup.metodos valor="lookupMultiDocPrintServices" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static MultiDocPrintService[] lookupMultiDocPrintServices(DocFlavor[] flavors, AttributeSet attributes)
~~~

## Parámetros
* **DocFlavor[] flavors**,  {% include w3api/param_description.html metodo=_data parametro="DocFlavor[] flavors" %}
* **AttributeSet attributes**,  {% include w3api/param_description.html metodo=_data parametro="AttributeSet attributes" %}

## Clase Padre
[PrintServiceLookup](/Java/PrintServiceLookup/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PrintServiceLookup.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
