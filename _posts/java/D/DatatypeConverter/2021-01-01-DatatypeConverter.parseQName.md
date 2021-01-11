---
title: DatatypeConverter.parseQName()
permalink: Java/DatatypeConverter/parseQName
date: 2021-01-11
key: JavaJava.D.DatatypeConverter
category: java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatatypeConverter.metodos valor="parseQName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static QName parseQName(String lexicalXSDQName, NamespaceContext nsc)
~~~

## Parámetros
* **String lexicalXSDQName**,  {% include w3api/param_description.html metodo=_dato parametro="String lexicalXSDQName" %}
* **NamespaceContext nsc**,  {% include w3api/param_description.html metodo=_dato parametro="NamespaceContext nsc" %}

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
