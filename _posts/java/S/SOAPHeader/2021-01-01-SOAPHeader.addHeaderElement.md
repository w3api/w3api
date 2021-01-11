---
title: SOAPHeader.addHeaderElement()
permalink: Java/SOAPHeader/addHeaderElement
date: 2021-01-11
key: JavaJava.S.SOAPHeader
category: java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPHeader.metodos valor="addHeaderElement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
SOAPHeaderElement addHeaderElement(QName qname) throws SOAPException
SOAPHeaderElement addHeaderElement(Name name) throws SOAPException
~~~

## Parámetros
* **QName qname**,  {% include w3api/param_description.html metodo=_dato parametro="QName qname" %}
* **Name name**,  {% include w3api/param_description.html metodo=_dato parametro="Name name" %}

## Excepciones
[SOAPException](/Java/SOAPException/)

## Clase Padre
[SOAPHeader](/Java/SOAPHeader/)

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
