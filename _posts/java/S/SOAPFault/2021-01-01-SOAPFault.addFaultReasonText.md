---
title: SOAPFault.addFaultReasonText()
permalink: /Java/SOAPFault/addFaultReasonText/
date: 2021-01-11
key: Java.S.SOAPFault
category: Java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPFault.metodos valor="addFaultReasonText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addFaultReasonText(String text, Locale locale) throws SOAPException
~~~

## Parámetros
* **String text**,  {% include w3api/param_description.html metodo=_dato parametro="String text" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [SOAPException](/Java/SOAPException/)

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
