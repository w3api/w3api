---
title: NamedNodeMap.getNamedItemNS()
permalink: Java/NamedNodeMap/getNamedItemNS
date: 2021-01-04
key: JavaJava.N.NamedNodeMap
category: java
tags: ['java se', 'org.w3c.dom', 'java.xml', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NamedNodeMap.metodos valor="getNamedItemNS" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Node getNamedItemNS(String namespaceURI, String localName) throws DOMException
~~~

## Parámetros
* **String localName**,  {% include w3api/param_description.html metodo=_data parametro="String localName" %}
* **String namespaceURI**,  {% include w3api/param_description.html metodo=_data parametro="String namespaceURI" %}

## Excepciones
[DOMException](/Java/DOMException/)

## Clase Padre
[NamedNodeMap](/Java/NamedNodeMap/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NamedNodeMap.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
