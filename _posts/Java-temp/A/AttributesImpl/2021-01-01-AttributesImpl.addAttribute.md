---
title: AttributesImpl.addAttribute()
permalink: /Java/AttributesImpl/addAttribute/
date: 2021-01-11
key: Java.A.AttributesImpl
category: Java
tags: ['java se', 'org.xml.sax.helpers', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttributesImpl.metodos valor="addAttribute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void addAttribute(String uri, String localName, String qName, String type, String value)
~~~

## Parámetros
* **String localName**,  {% include w3api/param_description.html metodo=_dato parametro="String localName" %}
* **String uri**,  {% include w3api/param_description.html metodo=_dato parametro="String uri" %}
* **String value**,  {% include w3api/param_description.html metodo=_dato parametro="String value" %}
* **String qName**,  {% include w3api/param_description.html metodo=_dato parametro="String qName" %}
* **String type**,  {% include w3api/param_description.html metodo=_dato parametro="String type" %}

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
