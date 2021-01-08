---
title: Attributes2.isDeclared()
permalink: Java/Attributes2/isDeclared
date: 2021-01-04
key: JavaJava.A.Attributes2
category: java
tags: ['java se', 'org.xml.sax.ext', 'java.xml', 'metodo java', 'Java 1.5', 'SAX 2.0 (extensions Java 1.1 alpha)']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Attributes2.metodos valor="isDeclared" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean isDeclared(int index)
boolean isDeclared(String qName)
boolean isDeclared(String uri, String localName)
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **String localName**,  {% include w3api/param_description.html metodo=_data parametro="String localName" %}
* **String qName**,  {% include w3api/param_description.html metodo=_data parametro="String qName" %}
* **String uri**,  {% include w3api/param_description.html metodo=_data parametro="String uri" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Attributes2](/Java/Attributes2/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.Attributes2.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
