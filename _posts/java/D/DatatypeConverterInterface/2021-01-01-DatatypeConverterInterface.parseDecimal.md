---
title: DatatypeConverterInterface.parseDecimal()
permalink: /Java/DatatypeConverterInterface/parseDecimal/
date: 2021-01-11
key: Java.D.DatatypeConverterInterface
category: Java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatatypeConverterInterface.metodos valor="parseDecimal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
BigDecimal parseDecimal(String lexicalXSDDecimal)
~~~

## Parámetros
* **String lexicalXSDDecimal**,  {% include w3api/param_description.html metodo=_dato parametro="String lexicalXSDDecimal" %}

## Excepciones
[NumberFormatException](/Java/NumberFormatException/)

## Clase Padre
[DatatypeConverterInterface](/Java/DatatypeConverterInterface/)

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
