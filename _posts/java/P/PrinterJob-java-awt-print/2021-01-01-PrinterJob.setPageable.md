---
title: PrinterJob.setPageable()
permalink: /Java/PrinterJob-java-awt-print/setPageable/
date: 2021-01-11
key: Java.P.PrinterJob-java-awt-print
category: Java
tags: ['java se', 'java.awt.print', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrinterJob-java-awt-print.metodos valor="setPageable" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setPageable(Pageable document) throws NullPointerException
~~~

## Parámetros
* **Pageable document**,  {% include w3api/param_description.html metodo=_dato parametro="Pageable document" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PrinterJob](/Java/PrinterJob-java-awt-print/)

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
