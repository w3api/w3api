---
title: SOAPElement.createQName()
permalink: /Java/SOAPElement/createQName/
date: 2021-01-11
key: Java.S.SOAPElement
category: Java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPElement.metodos valor="createQName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
QName createQName(String localName, String prefix) throws SOAPException
~~~

## Parámetros
* **String localName**,  {% include w3api/param_description.html metodo=_dato parametro="String localName" %}
* **String prefix**,  {% include w3api/param_description.html metodo=_dato parametro="String prefix" %}

## Excepciones
[SOAPException](/Java/SOAPException/)

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
