---
title: DatatypeConverter.parseBase64Binary()
permalink: Java/DatatypeConverter/parseBase64Binary
date: 2021-01-11
key: JavaJava.D.DatatypeConverter
category: java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatatypeConverter.metodos valor="parseBase64Binary" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static byte[] parseBase64Binary(String lexicalXSDBase64Binary)
~~~

## Parámetros
* **String lexicalXSDBase64Binary**,  {% include w3api/param_description.html metodo=_dato parametro="String lexicalXSDBase64Binary" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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