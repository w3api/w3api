---
title: PrinterStateReasons.PrinterStateReasons()
permalink: Java/PrinterStateReasons/PrinterStateReasons
date: 2021-01-04
key: JavaJava.P.PrinterStateReasons
category: java
tags: ['java se', 'javax.print.attribute.standard', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrinterStateReasons.constructores valor="PrinterStateReasons" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PrinterStateReasons()
public PrinterStateReasons(int initialCapacity)
public PrinterStateReasons(int initialCapacity, float loadFactor)
public PrinterStateReasons(Map<PrinterStateReason,Severity> map)
~~~

## Parámetros
* **Severity&gt; map**,  {% include w3api/param_description.html metodo=_data parametro="Severity> map" %}
* **int initialCapacity**,  {% include w3api/param_description.html metodo=_data parametro="int initialCapacity" %}
* **float loadFactor**,  {% include w3api/param_description.html metodo=_data parametro="float loadFactor" %}
* **Map&lt;PrinterStateReason**,  {% include w3api/param_description.html metodo=_data parametro="Map<PrinterStateReason" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PrinterStateReasons](/Java/PrinterStateReasons/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PrinterStateReasons.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
