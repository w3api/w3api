---
title: AttributesImpl.getType()
permalink: /Java/AttributesImpl/getType/
date: 2021-01-11
key: Java.A.AttributesImpl
category: Java
tags: ['java se', 'org.xml.sax.helpers', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttributesImpl.metodos valor="getType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String getType(int index)
public String getType(String qName)
public String getType(String uri, String localName)
~~~

## Parámetros
* **String uri**,  {% include w3api/param_description.html metodo=_dato parametro="String uri" %}
* **String qName**,  {% include w3api/param_description.html metodo=_dato parametro="String qName" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **String localName**,  {% include w3api/param_description.html metodo=_dato parametro="String localName" %}

## Clase Padre
[AttributesImpl](/Java/AttributesImpl/)

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
