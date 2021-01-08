---
title: Attributes.getValue()
permalink: Java/Attributes-org-xml-sax/getValue
date: 2021-01-04
key: JavaJava.A.Attributes-org-xml-sax
category: java
tags: ['java se', 'org.xml.sax', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Attributes-org-xml-sax.metodos valor="getValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
String getValue(int index)
String getValue(String qName)
String getValue(String uri, String localName)
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **String localName**,  {% include w3api/param_description.html metodo=_data parametro="String localName" %}
* **String qName**,  {% include w3api/param_description.html metodo=_data parametro="String qName" %}
* **String uri**,  {% include w3api/param_description.html metodo=_data parametro="String uri" %}

## Clase Padre
[Attributes](/Java/Attributes-org-xml-sax/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.Attributes-org-xml-sax.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
