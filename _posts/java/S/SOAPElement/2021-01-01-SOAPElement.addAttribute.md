---
title: SOAPElement.addAttribute()
permalink: /Java/SOAPElement/addAttribute/
date: 2021-01-11
key: Java.S.SOAPElement
category: Java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPElement.metodos valor="addAttribute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
SOAPElement addAttribute(QName qname, String value) throws SOAPException
SOAPElement addAttribute(Name name, String value) throws SOAPException
~~~

## Parámetros
* **Name name**,  {% include w3api/param_description.html metodo=_dato parametro="Name name" %}
* **QName qname**,  {% include w3api/param_description.html metodo=_dato parametro="QName qname" %}
* **String value**,  {% include w3api/param_description.html metodo=_dato parametro="String value" %}

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
