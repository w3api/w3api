---
title: PrintService.isAttributeValueSupported()
permalink: /Java/PrintService-javax-print/isAttributeValueSupported/
date: 2021-01-11
key: Java.P.PrintService-javax-print
category: Java
tags: ['java se', 'javax.print', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrintService-javax-print.metodos valor="isAttributeValueSupported" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean isAttributeValueSupported(Attribute attrval, DocFlavor flavor, AttributeSet attributes)
~~~

## Parámetros
* **Attribute attrval**,  {% include w3api/param_description.html metodo=_dato parametro="Attribute attrval" %}
* **DocFlavor flavor**,  {% include w3api/param_description.html metodo=_dato parametro="DocFlavor flavor" %}
* **AttributeSet attributes**,  {% include w3api/param_description.html metodo=_dato parametro="AttributeSet attributes" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

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
