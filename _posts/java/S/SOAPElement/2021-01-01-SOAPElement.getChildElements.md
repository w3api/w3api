---
title: SOAPElement.getChildElements()
permalink: /Java/SOAPElement/getChildElements/
date: 2021-01-11
key: Java.S.SOAPElement
category: Java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPElement.metodos valor="getChildElements" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Iterator<Node> getChildElements()
Iterator<Node> getChildElements(QName qname)
Iterator<Node> getChildElements(Name name)
~~~

## Parámetros
* **QName qname**,  {% include w3api/param_description.html metodo=_dato parametro="QName qname" %}
* **Name name**,  {% include w3api/param_description.html metodo=_dato parametro="Name name" %}

## Clase Padre
[SOAPElement](/Java/SOAPElement/)

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
