---
title: DatatypeConverterInterface.parseQName()
permalink: Java/DatatypeConverterInterface/parseQName
date: 2021-01-04
key: JavaJava.D.DatatypeConverterInterface
category: java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatatypeConverterInterface.metodos valor="parseQName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
QName parseQName(String lexicalXSDQName, NamespaceContext nsc)
~~~

## Parámetros
* **NamespaceContext nsc**,  {% include w3api/param_description.html metodo=_data parametro="NamespaceContext nsc" %}
* **String lexicalXSDQName**,  {% include w3api/param_description.html metodo=_data parametro="String lexicalXSDQName" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DatatypeConverterInterface](/Java/DatatypeConverterInterface/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DatatypeConverterInterface.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
