---
title: DatatypeConverter.parseInteger()
permalink: /Java/DatatypeConverter/parseInteger/
date: 2021-01-11
key: Java.D.DatatypeConverter
category: Java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatatypeConverter.metodos valor="parseInteger" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static BigInteger parseInteger(String lexicalXSDInteger)
~~~

## Parámetros
* **String lexicalXSDInteger**,  {% include w3api/param_description.html metodo=_dato parametro="String lexicalXSDInteger" %}

## Excepciones
[NumberFormatException](/Java/NumberFormatException/)

## Clase Padre
[DatatypeConverter](/Java/DatatypeConverter/)

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
