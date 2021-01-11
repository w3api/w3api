---
title: DocPrintJob.print()
permalink: Java/DocPrintJob/print
date: 2021-01-11
key: JavaJava.D.DocPrintJob
category: java
tags: ['java se', 'javax.print', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocPrintJob.metodos valor="print" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void print(Doc doc, PrintRequestAttributeSet attributes) throws PrintException
~~~

## Parámetros
* **PrintRequestAttributeSet attributes**,  {% include w3api/param_description.html metodo=_dato parametro="PrintRequestAttributeSet attributes" %}
* **Doc doc**,  {% include w3api/param_description.html metodo=_dato parametro="Doc doc" %}

## Excepciones
[PrintException](/Java/PrintException/)

## Clase Padre
[DocPrintJob](/Java/DocPrintJob/)

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
