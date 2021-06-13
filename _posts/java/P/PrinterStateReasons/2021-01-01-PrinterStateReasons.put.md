---
title: PrinterStateReasons.put()
permalink: /Java/PrinterStateReasons/put/
date: 2021-01-11
key: Java.P.PrinterStateReasons
category: java
tags: ['java se', 'javax.print.attribute.standard', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrinterStateReasons.metodos valor="put" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Severity put(PrinterStateReason reason, Severity severity)
~~~

## Parámetros
* **Severity severity**,  {% include w3api/param_description.html metodo=_dato parametro="Severity severity" %}
* **PrinterStateReason reason**,  {% include w3api/param_description.html metodo=_dato parametro="PrinterStateReason reason" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PrinterStateReasons](/Java/PrinterStateReasons/)

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
