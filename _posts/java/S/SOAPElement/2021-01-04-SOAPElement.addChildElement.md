---
title: SOAPElement.addChildElement()
permalink: Java/SOAPElement/addChildElement
date: 2021-01-04
key: JavaJava.S.SOAPElement
category: java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPElement.metodos valor="addChildElement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
SOAPElement addChildElement(String localName) throws SOAPException
SOAPElement addChildElement(String localName, String prefix) throws SOAPException
SOAPElement addChildElement(String localName, String prefix, String uri) throws SOAPException
SOAPElement addChildElement(QName qname) throws SOAPException
SOAPElement addChildElement(Name name) throws SOAPException
SOAPElement addChildElement(SOAPElement element) throws SOAPException
~~~

## Parámetros
* **QName qname**,  {% include w3api/param_description.html metodo=_data parametro="QName qname" %}
* **String localName**,  {% include w3api/param_description.html metodo=_data parametro="String localName" %}
* **SOAPElement element**,  {% include w3api/param_description.html metodo=_data parametro="SOAPElement element" %}
* **String prefix**,  {% include w3api/param_description.html metodo=_data parametro="String prefix" %}
* **String uri**,  {% include w3api/param_description.html metodo=_data parametro="String uri" %}
* **Name name**,  {% include w3api/param_description.html metodo=_data parametro="Name name" %}

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
{%- for _ldc in site.data.Java.S.SOAPElement.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
