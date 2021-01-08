---
title: SOAPElement.addAttribute()
permalink: Java/SOAPElement/addAttribute
date: 2021-01-04
key: JavaJava.S.SOAPElement
category: java
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
* **QName qname**,  {% include w3api/param_description.html metodo=_data parametro="QName qname" %}
* **String value**,  {% include w3api/param_description.html metodo=_data parametro="String value" %}
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
