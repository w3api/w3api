---
title: MultiDocPrintJob.print()
permalink: Java/MultiDocPrintJob/print
date: 2021-01-04
key: JavaJava.M.MultiDocPrintJob
category: java
tags: ['java se', 'javax.print', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MultiDocPrintJob.metodos valor="print" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void print(MultiDoc multiDoc, PrintRequestAttributeSet attributes) throws PrintException
~~~

## Parámetros
* **PrintRequestAttributeSet attributes**,  {% include w3api/param_description.html metodo=_data parametro="PrintRequestAttributeSet attributes" %}
* **MultiDoc multiDoc**,  {% include w3api/param_description.html metodo=_data parametro="MultiDoc multiDoc" %}

## Excepciones
[PrintException](/Java/PrintException/)

## Clase Padre
[MultiDocPrintJob](/Java/MultiDocPrintJob/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MultiDocPrintJob.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
