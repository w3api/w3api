---
title: Attributes.getType()
permalink: /Java/Attributes-org-xml-sax/getType/
date: 2021-01-11
key: Java.A.Attributes-org-xml-sax
category: Java
tags: ['java se', 'org.xml.sax', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Attributes-org-xml-sax.metodos valor="getType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
String getType(int index)
String getType(String qName)
String getType(String uri, String localName)
~~~

## Parámetros
* **String uri**,  {% include w3api/param_description.html metodo=_dato parametro="String uri" %}
* **String qName**,  {% include w3api/param_description.html metodo=_dato parametro="String qName" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **String localName**,  {% include w3api/param_description.html metodo=_dato parametro="String localName" %}

## Clase Padre
[Attributes](/Java/Attributes-org-xml-sax/)

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
