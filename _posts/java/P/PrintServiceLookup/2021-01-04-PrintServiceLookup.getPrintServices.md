---
title: PrintServiceLookup.getPrintServices()
permalink: Java/PrintServiceLookup/getPrintServices
date: 2021-01-04
key: JavaJava.P.PrintServiceLookup
category: java
tags: ['java se', 'javax.print', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrintServiceLookup.metodos valor="getPrintServices" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract PrintService[] getPrintServices()
public abstract PrintService[] getPrintServices(DocFlavor flavor, AttributeSet attributes)
~~~

## Parámetros
* **DocFlavor flavor**,  {% include w3api/param_description.html metodo=_data parametro="DocFlavor flavor" %}
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
