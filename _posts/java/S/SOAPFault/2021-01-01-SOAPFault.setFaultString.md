---
title: SOAPFault.setFaultString()
permalink: /Java/SOAPFault/setFaultString/
date: 2021-01-11
key: Java.S.SOAPFault
category: Java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPFault.metodos valor="setFaultString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setFaultString(String faultString) throws SOAPException
void setFaultString(String faultString, Locale locale) throws SOAPException
~~~

## Parámetros
* **String faultString**,  {% include w3api/param_description.html metodo=_dato parametro="String faultString" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}

## Excepciones
[SOAPException](/Java/SOAPException/)

## Clase Padre
[SOAPFault](/Java/SOAPFault/)

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
