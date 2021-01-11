---
title: PrintService.getUnsupportedAttributes()
permalink: Java/PrintService-javax-print/getUnsupportedAttributes
date: 2021-01-11
key: JavaJava.P.PrintService-javax-print
category: java
tags: ['java se', 'javax.print', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrintService-javax-print.metodos valor="getUnsupportedAttributes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
AttributeSet getUnsupportedAttributes(DocFlavor flavor, AttributeSet attributes)
~~~

## Parámetros
* **DocFlavor flavor**,  {% include w3api/param_description.html metodo=_dato parametro="DocFlavor flavor" %}
* **AttributeSet attributes**,  {% include w3api/param_description.html metodo=_dato parametro="AttributeSet attributes" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PrintService](/Java/PrintService-javax-print/)

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