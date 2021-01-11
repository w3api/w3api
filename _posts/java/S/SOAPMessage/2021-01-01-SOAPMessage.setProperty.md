---
title: SOAPMessage.setProperty()
permalink: Java/SOAPMessage/setProperty
date: 2021-01-11
key: JavaJava.S.SOAPMessage
category: java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPMessage.metodos valor="setProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setProperty(String property, Object value) throws SOAPException
~~~

## Parámetros
* **String property**,  {% include w3api/param_description.html metodo=_dato parametro="String property" %}
* **Object value**,  {% include w3api/param_description.html metodo=_dato parametro="Object value" %}

## Excepciones
[SOAPException](/Java/SOAPException/)

## Clase Padre
[SOAPMessage](/Java/SOAPMessage/)

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
